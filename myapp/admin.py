from django.contrib import admin
from myapp.models import Trace, AudioFile

class TraceAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('image',)

class AudioFileAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('audio_file', 'length', 'trace',)

# Register your models here.
admin.site.register(Trace, TraceAdmin)
admin.site.register(AudioFile, AudioFileAdmin)
