# -*- coding: utf-8 -*-
from django.db import models

# confirmation text

class Document(models.Model):

    GENRE = (
        ('Chillout', 'Chillout'),
        ('Happy', 'Happy'),
        ('Mood', 'Mood'),
        ('Romantic', 'Romantic'),
        ('Party', 'Party'),
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Indie', 'Indie'),
        ('Hip-Hop', 'Hip-Hop'),
         )

    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    genre = models.CharField(max_length=128, choices=GENRE)
    title = models.CharField(max_length=128)

    img = models.ImageField(upload_to='artwork')
    user = models.CharField(max_length=128)
    up = models.IntegerField(editable=False, default=0)
    down = models.IntegerField(editable=False, default=0)


    def __unicode__(self):
        return self.user
