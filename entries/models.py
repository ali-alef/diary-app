from django.db import models
from django.utils import timezone


class Entry(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(defualt=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"
