from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    blog_post_id = serializers.IntegerField(source='blog_post.id', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'blog_post_id', 'user_id', 'content', 'created_at']
        read_only_fields = ['id', 'user_id', 'blog_post_id', 'created_at']
