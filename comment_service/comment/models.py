from django.db import models

class Comment(models.Model):
    blog_post_id = models.IntegerField()  # Store blog post ID
    user_id = models.IntegerField()  # Store user ID
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"User {self.user_id} - {self.content[:20]}"
