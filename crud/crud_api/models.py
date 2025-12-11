from django.db import models
from django.contrib.auth.models import User, Permission
class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_add_blog", "Can add blog"),
            ("can_change_blog", "Can change blog"),
            ("can_delete_blog", "Can delete blog"),
            ("can_view_blog", "Can view blog"),
        ]

    def __str__(self):
        return self.name
