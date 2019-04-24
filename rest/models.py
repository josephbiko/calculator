from django.db import models


class UrlModel(models.Model):
    url = models.URLField()

