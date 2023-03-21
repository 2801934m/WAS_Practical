from django.db import models

# Create your models here.

class NewsItem(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    date = models.DateField()
    story = models.TextField()

    def __str__(self):
        return self.title
# Page 68 in textbook. Review foreign keys if not working