# -*- coding: utf-8 -*-
from django import forms

class AudioFileForm(forms.ModelForm):
    audioFile = forms.FileField(
        label='Select an audio file',
        help_text='max. 100mb'
    )
