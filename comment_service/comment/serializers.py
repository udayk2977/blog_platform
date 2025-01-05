from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog_post_id', 'user_id', 'content', 'created_at']
        read_only_fields = ['id', 'user_id', 'blog_post_id', 'created_at']
