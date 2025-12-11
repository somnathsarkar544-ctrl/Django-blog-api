from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from articles.models import Article
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        slug = self.kwargs['slug']
        article = get_object_or_404(Article, slug=slug)
        return article.comments.all()

    def perform_create(self, serializer):
        slug = self.kwargs['slug']
        article = get_object_or_404(Article, slug=slug)
        serializer.save(author=self.request.user, article=article)

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied('You can only delete your own comments')
        instance.delete()