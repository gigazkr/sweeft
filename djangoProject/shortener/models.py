from django.db import models


class URL(models.Model):
    long_url = models.URLField(max_length=250)
    short_url = models.CharField(max_length=10, unique=True, blank=True)
    click_times = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.long_url
