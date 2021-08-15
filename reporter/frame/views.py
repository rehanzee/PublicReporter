from rest_framework.views import APIView
from ..controller.FrameController import FrameController


class FramesView(APIView):

    def get(self, request):
        return FrameController.frames(request)
