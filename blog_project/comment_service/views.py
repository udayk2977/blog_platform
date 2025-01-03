from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Comment
from blog_service.models import BlogPost
from .serializers import CommentSerializer

class CommentCreateView(generics.CreateAPIView):
    """
    POST /comments/
    Request body: {"post_id": <blog_post_id>, "content": "..."}
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        content = request.data.get('content')

        blog_post = get_object_or_404(BlogPost, pk=post_id)

        comment = Comment.objects.create(
            blog_post=blog_post,
            user=request.user,
            content=content
        )
        serializer = self.get_serializer(comment)
        return Response(serializer.data)


class CommentListView(generics.ListAPIView):
    """
    GET /comments?post_id=<id>
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        if post_id:
            return Comment.objects.filter(blog_post_id=post_id).order_by('-created_at')
        return Comment.objects.none()
