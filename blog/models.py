from django.db import models
from django.urls import reverse


class single_blog(models.Model):
    sb_title = models.CharField(max_length=300)
    sb_image = models.ImageField(default='catalog/01.jpg')
    sb_description = models.CharField(max_length=500)
    sb_slug = models.SlugField(default="", blank=True, db_index=True)

    def get_absolute_url(self):
        return reverse('sb_detail', args=[self.sb_slug])

    def __str__(self):
        return f'{self.sb_title} {self.sb_description}'





