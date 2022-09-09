from django.db import models


class Project(models.Model):
    """Model representing a project"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
