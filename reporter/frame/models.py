from django.core.validators import FileExtensionValidator
from django.db import models
from django_enumfield import enum


# Create your models here.
class FrameCategory(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    thumb = models.ImageField(upload_to='cat_thumb')
    active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "frame_categories"


class TextPos(enum.Enum):
    TOP = 0
    BOTTOM = 1
    BOTH = 2


class Frame(models.Model):
    category = models.ForeignKey(FrameCategory, on_delete=models.CASCADE, related_name='frame')
    title = models.CharField(max_length=30)
    thumb = models.ImageField(default='thumb.jpg', upload_to='frame_thumb')
    is_text = models.BooleanField(default=0)
    text_pos = enum.EnumField(TextPos, default=TextPos.BOTTOM)
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "frames"


class FrameFile(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, related_name='frame_file')
    resolution = enum.EnumField()
    frame_media = models.FileField(
        default='frame.mov',
        upload_to='frames',
        validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "frame_files"
