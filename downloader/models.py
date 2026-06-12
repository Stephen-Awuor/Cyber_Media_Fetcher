from django.db import models

class DownloadHistory(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=500)
    platform = models.CharField(max_length=100)
    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title