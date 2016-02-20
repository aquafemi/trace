# -*- coding: utf-8 -*-
from django import forms

class AudioFileForm(forms.Form):
    audio_file = forms.FileField(
        label='Select an audio file',
        help_text='max. 100mb'
    )
