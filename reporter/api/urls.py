from django.urls import include, path
from ..frame.views import FramesView


urlpatterns = [
    path("get-frames/<int:res>", FramesView.as_view()),
]