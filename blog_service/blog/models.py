from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_id = models.IntegerField(default=0)  # Add a default value
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
