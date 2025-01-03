from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import BlogPost
from .serializers import BlogPostSerializer

from rest_framework import status, generics, permissions
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogListCreateView(generics.ListCreateAPIView):
    """
    GET /blogs/  -> list all blog posts (paginated)
    POST /blogs/ -> create a new blog post
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Set the author to the currently logged-in user
        # This ensures only authenticated users can create a post.
        serializer.save(author=self.request.user)



class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /blogs/<pk>/
    PUT /blogs/<pk>/
    DELETE /blogs/<pk>/
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # Only the author or staff can update
        if request.user != instance.author and not request.user.is_staff:
            return Response({'detail': 'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Only the author or staff can delete
        if request.user != instance.author and not request.user.is_staff:
            return Response({'detail': 'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
