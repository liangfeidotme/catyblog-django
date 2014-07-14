from django.db import models

# Create your models here.


class Config(models.Model):
    site_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.site_name


class Navigation(models.Model):
    display_name = models.CharField(max_length=20)
    url_name = models.CharField(max_length=10)

    def __unicode__(self):
        return '{} on {}'.format(self.display_name, self.url_name)