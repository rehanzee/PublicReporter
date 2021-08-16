from django.core.validators import FileExtensionValidator
from django.db import models
from django_enumfield import enum


# Create your models here.
class FrameCategory(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    thumb = models.ImageField(default='thumb.jpg', upload_to='upload/cat_thumb')
    active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "frame_categories"


class TextPos(enum.Enum):
    TOP = 0
    BOTTOM = 1
    BOTH = 2


class Frame(models.Model):
    category = models.ForeignKey(FrameCategory, on_delete=models.CASCADE, related_name='frame')
    frame_sku = models.CharField(max_length=30)
    thumb = models.ImageField(default='thumb.jpg', upload_to='upload/frame_thumb')
    is_text = models.BooleanField(default=0)
    text_pos = enum.EnumField(TextPos, default=TextPos.BOTTOM)
    is_active = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.frame_sku

    class Meta:
        db_table = "frames"


class FrameAspectRatio(enum.Enum):
    R16X9 = 0
    R9X16 = 1
    R1X1 = 2
    R4X3 = 3
    R3X4 = 4
    R5X4 = 5
    R4X5 = 6


class FrameFile(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, related_name='frame_file')
    resolution = enum.EnumField(FrameAspectRatio, default=FrameAspectRatio.R16X9)
    frame_media = models.FileField(
        default='frame.mov',
        upload_to='upload/frames',
        validators=[FileExtensionValidator(allowed_extensions=['mov', 'gif', 'png'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "frame_files"
