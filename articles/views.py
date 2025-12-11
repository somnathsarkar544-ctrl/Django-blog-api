from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Article, Tag
from .serializers import ArticleSerializer, TagSerializer

class ArticleListCreateView(generics.ListCreateAPIView): # view to list all articles and create new article
    queryset = Article.objects.select_related('author').prefetch_related('tags','likes').all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = []
    search_fields = ['title','body','author_username','tags_name']
    ordering_fields = ['created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        tag = self.request.query_params.get('tag')
        author = self.request.query_params.get('author')
        sort = self.request.query_params.get('sort')
        if tag:
            qs = qs.filter(tags__name=tag)
        if author:
            qs = qs.filter(author__username=author)
        if sort == 'created_at':
            qs = qs.order_by('-created_at')
        elif sort == 'likes':
            qs = sorted(qs, key=lambda a: a.favorites_count(), reverse=True)
        return qs

    def get_serializer_context(self):
        return {'request': self.request}

class ArticleRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_serializer_context(self):
        return {'request': self.request}

    def perform_update(self, serializer):
        article = self.get_object()
        if self.request.user != article.author:
            raise permissions.PermissionDenied('You can only edit your own articles')
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise permissions.PermissionDenied('You can only delete your own articles')
        instance.delete()

class ArticleFavouriteToggle(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        article.likes.add(request.user)
        serializer = self.get_serializer(article, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        article.likes.remove(request.user)
        serializer = self.get_serializer(article, context={'request': request})
        return Response(serializer.data)

class FeedView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following = user.following.all()
        return Article.objects.filter(author__in=following).select_related('author').prefetch_related('tags','likes')

    def get_serializer_context(self):
        return {'request': self.request}

