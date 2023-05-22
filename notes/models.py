from django.db import models
from django.conf import settings

class Folder(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    folder = models.ForeignKey(Folder, related_name='notes', on_delete=models.CASCADE)
    tags = models.CharField(max_length=200, blank=True) # tags as comma-separated values
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title