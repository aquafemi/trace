from django.http import (HttpResponseBadRequest, HttpResponseRedirect,
                         HttpResponse)
from django.shortcuts import redirect, render, render_to_response
from django.views.generic.base import View
from myapp import models
from myapp import forms
from transloadit.client import Client
from mutagen.mp3 import MP3

AUTH_KEY = '90e7d490d78611e5893f9b7c82ab5693'
AUTH_SECRET = 'a9918408b27cc8eae418ee0d25019b429a13f3d0'

# Create your views here.

class HomePage(View):

    def get(self, request):
        # ask person if they want to create a trace or upload a trace
        return render(request, 'home.html')

class AudioUpload(View):

    def get(self, request):
        # ask person to upload a audio file
        # possibly put a label on it
        return render(request, '/audio_upload.html')

    def post(self, request):
        # here is where someone uploads the audio file
        # get the audio file and store it in the back end
        # sent the audio file to transloadit. Get the image and associate it with the file
        # put the image in the queue or have it replace the old one

        form = AudioFileForm(request.POST, request.FILES)
        if not form.is_valid():
            form = AudioFileForm()
            return render('/audio_upload.html', {'form': form})

        # get length in seconds
        audio = MP3(request.POST['audio_file'].name)
        length = audio.info.length

        client = Client(AUTH_KEY, AUTH_SECRET)
        params = {
            'steps': {
                'wav': {
                    'use': ":original",
                    'robot': "/audio/encode",
                    'preset': "wav",
                    'ffmpeg_stack': "v2.2.3"
                },
                'waveform': {
                    'robot': "/audio/waveform",
                    'use': "wav",
                    'format': 'image',
                    'result': True,
                    'width': 300,
                    'height': 200,
                    'background_color': "ffffffff",
                    'outer_color': "ff0000aa",
                    'center_color': "660000aa"
                },
            },
        }

        result = client.request(**params)
        form = SoundUpload(label=request.POST['label'],
                           audio_file=request.POST['audio_file'],
                           trace=open(result))
        form.save()
        # return them home
        return HttpResponseRedirect('/status.html')

class TracePlayback(View):

    def get(self, request):
        # ask for camera
        return render(request, 'trace_playback.html')

    def post(self, request):
        # ask for camera input
        return render(request, 'trace_playback.html')

class Status(View):

    def get(self, request):
        pass

    def post(self, request):
        pass
