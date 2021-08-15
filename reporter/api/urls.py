from django.urls import include, path
from ..frame.views import FramesView


urlpatterns = [
    path("get-frames/", FramesView.as_view()),
]