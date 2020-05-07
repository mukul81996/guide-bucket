from django.db import models


class Subject(models.Model):
    """Model to store information about a Subject"""
    name = models.CharField(max_length=255, unique=True, verbose_name="Name")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="Slug" , null = True)
    books = models.TextField(verbose_name="Books", default = "Updating soon")
    movies = models.TextField(verbose_name="Movies",default = "Updating soon")
    docs = models.TextField(verbose_name="Documentaries",default = "Updating soon")
    yt_channels = models.TextField(verbose_name="Youtube Channels",default = "Updating soon")
    websites = models.TextField(verbose_name="Websites",default = "Updating soon")
    fb_pages = models.TextField(verbose_name="Facebook Pages",default = "Updating soon")
    insta_pages = models.TextField(verbose_name="Instagram Pages",default = "Updating soon") 

    def __str__(self):
        return self.name

