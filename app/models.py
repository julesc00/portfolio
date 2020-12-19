from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    technology = models.CharField(max_length=20, null=True)
    image = models.FilePathField(path=settings.MEDIA_URL)

    def __str__(self):
        return self.title
