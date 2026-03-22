from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name