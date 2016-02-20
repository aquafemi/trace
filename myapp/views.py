from django.http import (HttpResponseBadRequest, HttpResponseRedirect,
                         HttpResponse)
from django.shortcuts import redirect, render, render_to_response
from django.views.generic.base import View
from myapp.models import *
from myapp.forms import *
from trace import settings as SETTINGS
from transloadit.client import Client
from mutagen.mp3 import MP3
from requests import get
import os.path
import time
import urllib

AUTH_KEY = '90e7d490d78611e5893f9b7c82ab5693'
AUTH_SECRET = 'a9918408b27cc8eae418ee0d25019b429a13f3d0'

# Create your views here.

class HomePage(View):

    def get(self, request):
        # ask person if they want to create a trace or upload a trace
        return render(request, 'home.html')

class AudioUpload(View):

    def get(self, request):
        form = AudioFileForm()
        return render(request, 'audio_upload.html', {'form': form})

    def post(self, request):
        # put the image in the queue or have it replace the old one

        form = AudioFileForm(request.POST, request.FILES)
        if not form.is_valid():
            form = AudioFileForm()
            return render(request, 'audio_upload.html', {'form': form})

        audio_file = request.FILES['audio_file']
        sound = AudioFile(audio_file=audio_file)
        sound.save()

        client = Client(AUTH_KEY, AUTH_SECRET)
        media_location = SETTINGS.MEDIA_ROOT
        files = {'file': open(media_location + '/' +
                              sound.audio_file.name, 'rb')}
        params = {
            'steps': {
                'wav': {
                    'use': ":original",
                    'robot': "/audio/encode",
                    'preset': "wav",
                    'ffmpeg_stack': "v2.2.3"
                },
            },
            'notify_url': ''
        }
        result = client.request(files=files, **params)
        new_audio_link = result['results']['wav'][0]['url']
        with open('temp', 'wb') as temp_file:
            response = get(new_audio_link)
            temp_file.write(response.content)


        length = result['results']['wav'][0]['meta']['duration']
        print(length)
        files = {'file': open('temp', 'rb')}
        params = {
            'steps': {
                'waveform': {
                    'robot': "/audio/waveform",
                    'use': ":original",
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
        result = client.request(files=files, **params)
        img_link = result['results']['waveform'][0]['url']
        with open('temp', 'wb') as temp_file:
            response = get(img_link)
            temp_file.write(response.content)

        trace = Trace(image=open(temp_file))
        trace.save()

        # return them home
        print("here2")
        return HttpResponseRedirect('status.html')

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
