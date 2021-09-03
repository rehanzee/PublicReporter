from rest_framework.views import APIView
from ..controller.FrameController import FrameController


class FramesView(APIView):

    def get(self, request, res):
        return FrameController.frames(request, res)
