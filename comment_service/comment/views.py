import requests
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, NotFound
from .models import Comment
from .serializers import CommentSerializer

USER_SERVICE_URL = "http://user_service:8001/validate/"  # User Service validation endpoint
BLOG_SERVICE_URL = "http://blog_service:8002/blogs/"  # Blog Service validation endpoint

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

def validate_blog_post(blog_post_id):
    """
    Validate the blog post ID with the Blog Service.
    Returns True if valid, raises NotFound otherwise.
    """
    try:
        response = requests.get(f"{BLOG_SERVICE_URL}{blog_post_id}/")
        if response.status_code == 200:
            return True
        raise NotFound("Blog post not found")
    except requests.RequestException:
        raise NotFound("Unable to connect to Blog Service")

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Extract token and validate with User Service
        token = request.headers.get("Authorization", "").split("Bearer ")[-1]
        if not token:
            raise AuthenticationFailed("Authorization token missing")

        user_id = validate_token(token)

        # Validate blog_post_id with Blog Service
        blog_post_id = request.data.get("blog_post_id")
        if not blog_post_id:
            return Response({"detail": "Blog post ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        validate_blog_post(blog_post_id)

        # Create the comment
        content = request.data.get("content")
        comment = Comment.objects.create(
            blog_post_id=blog_post_id,
            user_id=user_id,
            content=content
        )
        serializer = self.get_serializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        blog_post_id = self.request.query_params.get("blog_post_id")
        if blog_post_id:
            return Comment.objects.filter(blog_post_id=blog_post_id).order_by('-created_at')
        return Comment.objects.none()
