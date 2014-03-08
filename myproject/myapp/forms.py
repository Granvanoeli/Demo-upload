# -*- coding: utf-8 -*-
from django import forms
from myproject.myapp.models import Document



class DocumentForm(forms.ModelForm):

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


    docfile = forms.FileField(label='Select a file')
    genre = forms.ChoiceField(choices=GENRE, label="Select a genre")
    img = forms.ImageField(label='Select an image')
    title = forms.CharField(label='Input the Demo title:')
    up = forms.IntegerField(widget=forms.HiddenInput, initial=0)
    down = forms.IntegerField(widget=forms.HiddenInput, initial=0)


    class Meta:
        model = Document
        fields = ('docfile', 'genre', 'title', 'img')


# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Select an image')
#
#     class Meta:
#         model = Image
#         fields = ('image',)
#
