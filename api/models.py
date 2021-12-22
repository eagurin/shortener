from hashlib import md5

from core.settings import BASE_URL
from django.core.exceptions import ValidationError
from django.db import models

from .utils import hashed


class Url(models.Model):
    url = models.URLField(max_length=320)
    shorten = models.SlugField(unique=True)
    count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)

    def clicked(self):
        self.count += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.shorten:
            self.shorten = hashed()
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def get_short_url(self):
        return BASE_URL + self.shorten
