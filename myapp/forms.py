# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from myapp.models import AudioFile

class AudioFileForm(ModelForm):
    class Meta:
        model = AudioFile
        fields = ['audio_file']
    audio_file = forms.FileField(
        label='Select an audio file'
    )
