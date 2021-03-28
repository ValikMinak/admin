from django.db import models
from django.utils.safestring import mark_safe

from albums.models import Album


class Image(models.Model):
    name = models.CharField(max_length=200)
    image_width = models.CharField(max_length=100)
    image_height = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    album = models.ForeignKey(Album, related_name='images', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width=100px>')
        else:
            return '(No image)'
