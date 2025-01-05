import requests
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import BlogPost
from .serializers import BlogPostSerializer

USER_SERVICE_URL = "http://user_service:8001/validate/"  # User Service validation endpoint

def validate_token(token):
    """
    Validate the JWT token with the User Service.
    Returns the user ID if valid, or raises an AuthenticationFailed exception.
    """
    try:
        response = requests.post(
            USER_SERVICE_URL,
            headers={"Authorization": f"Bearer {token}"}
        )
        if response.status_code == 200:
            return response.json().get("user_id")
        raise AuthenticationFailed("Invalid or expired token")
    except requests.RequestException:
        raise AuthenticationFailed("Unable to connect to User Service")

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Extract token from the request header
        token = self.request.headers.get("Authorization", "").split("Bearer ")[-1]
        if not token:
            raise AuthenticationFailed("Authorization token missing")

        # Validate the token and get the user ID
        author_id = validate_token(token)

        # Save the blog post with the author_id
        serializer.save(author_id=author_id)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        token = self.request.headers.get("Authorization", "").split("Bearer ")[-1]
        if not token:
            return Response({'detail': 'Authorization token missing'}, status=status.HTTP_403_FORBIDDEN)

        # Validate the token and get the user ID
        author_id = validate_token(token)

        if author_id != instance.author_id:
            return Response({'detail': 'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        token = self.request.headers.get("Authorization", "").split("Bearer ")[-1]
        if not token:
            return Response({'detail': 'Authorization token missing'}, status=status.HTTP_403_FORBIDDEN)

        # Validate the token and get the user ID
        author_id = validate_token(token)

        if author_id != instance.author_id:
            return Response({'detail': 'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
