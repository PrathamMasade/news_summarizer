from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    publication_date = models.DateField()
    source = models.CharField(max_length=100)
    url = models.URLField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title