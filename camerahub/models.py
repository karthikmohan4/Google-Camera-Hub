from django.db import models

class Cameras(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="camerahub/images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
