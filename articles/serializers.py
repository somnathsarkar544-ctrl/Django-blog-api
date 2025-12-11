from rest_framework import serializers
from .models import Article,Tag
from users.serializers import ProfileSerializer


class TagSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Tag
        fields = ['name']

class ArticleSerializer(serializers.ModelSerializer): 
    author = serializers.CharField(source='author.username', read_only=True) 
    tags = serializers.ListField(child=serializers.CharField(), write_only = True ,required=False) # List of tag names for creating/updating articles
    tags_list = serializers.SerializerMethodField() # this filed is only for output representation of tags
    favorites_count = serializers.IntegerField(read_only=True) # number of likes
    liked = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'slug', 'title', 'body', 'author', 'tags','tags_list', 
                  'favorites_count', 'liked', 'created_at', 'updated_at'] 
        read_only_fields = ['slug', 'author', 'favorites_count', 'created_at', 'updated_at'] 

    def get_tags_list(self,obj): # method to get list of tag names
        return list(obj.tags.values_list('name',flat=True))

    def get_liked(self, obj): # meothd to check if the current user has liked the article
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False
        return obj.likes.filter(pk=request.user.pk).exists()

    def create(self, validated_data): 
        tags_data = validated_data.pop('tags', []) 
        user = self.context['request'].user
        article = Article.objects.create(author=user, **validated_data)

        for t in tags_data: # create or get tag instamces and asscociate with the article
            tag, created = Tag.objects.get_or_create(name=t)
            article.tags.add(tag)

        return article

    def update(self, instance, validated_data): # update article instance
        tags_data = validated_data.pop('tags', None)
        for attr, value in validated_data.items(): # update other fileds
            setattr(instance, attr, value)
        instance.save()
        if tags_data is not None: # if tags are provided , update them
            instance.tags.clear()
            for t in tags_data: 
                tag, created = Tag.objects.get_or_create(name=t)
                instance.tags.add(tag)
        return instance
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['tags'] = list(instance.tags.values_list('name', flat=True))
        return rep
    