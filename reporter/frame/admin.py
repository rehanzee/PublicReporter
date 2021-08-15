from django.contrib import admin

# Register your models here.
from reporter.frame.models import FrameCategory, Frame, FrameFile

admin.site.register(FrameCategory)
admin.site.register(Frame)
admin.site.register(FrameFile)
