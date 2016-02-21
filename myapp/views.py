from django.http import (HttpResponseBadRequest, HttpResponseRedirect,
                         HttpResponse)
from django.shortcuts import redirect, render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from myapp.models import *
from myapp.forms import *
from trace import settings as SETTINGS
from transloadit.client import Client
from requests import get
import json
import shutil
import time
import urllib.request

AUTH_KEY = '90e7d490d78611e5893f9b7c82ab5693'
AUTH_SECRET = 'a9918408b27cc8eae418ee0d25019b429a13f3d0'

# Create your views here.

class HomePage(View):

    def get(self, request):
        return render(request, 'home.html')

class AudioUpload(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AudioUpload, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = AudioFileForm()
        return render(request, 'audio_upload.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # put the image in the queue or have it replace the old one

        transloadit_json = request.POST.get('transloadit', False)
        if transloadit_json:
            transloadit_dict = json.loads(transloadit_json)

            # audio output
            if transloadit_dict.get('results').get('wav'):
                print('audio')
                # get the download link
                new_audio_link = transloadit_dict.get('results').get('wav')[0].get('url')
                # download the wav file and write it to temp
                with urllib.request.urlopen(new_audio_link) as response, open('temp', 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)

                # get the length (in seconds) of the audio from the transloadit post
                length = transloadit_dict.get('results').get('wav')[0].get('meta').get('duration')

                client = Client(AUTH_KEY, AUTH_SECRET)

                # construct our files to pipe this output to the waveform robot. Open the audio file, temp
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
                    'notify_url': 'http://traced.herokuapp.com/audio-upload/'
                }
                # now we request for the waveform
                client.request(files=files, **params)

            # waveform output
            else:
                print('waveform')
                # get the image link from the transloadit post
                img_link = transloadit_dict.get('results').get('waveform')[0].get('url')
                with urllib.request.urlopen(img_link) as response, open('temp', 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)

                trace = Trace(image=out_file)
                trace.save()

            # don't return anything back to the transloadit server,
            return HttpResponse(status_code=200)
        else:
            # not a transloadit post, this is a post from a user uploading an audio file
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
                'notify_url': 'http://traced.herokuapp.com/audio-upload/'
            }
            client.request(files=files, **params)

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
