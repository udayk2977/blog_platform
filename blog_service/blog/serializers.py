from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author_id', 'created_at', 'updated_at']
