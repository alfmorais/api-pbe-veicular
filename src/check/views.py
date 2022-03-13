from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from check.serializers import PingSerializer, PongSerializer


class PongViewSet(ListAPIView):
    serializer_class = PongSerializer
    message = 'PING: The API is running!'

    def get(self, format=None):
        return Response(self.message)


class PingViewSet(ListAPIView):
    serializer_class = PingSerializer
    message = 'PONG: The API is running'

    def get(self, format=None):
        return Response(self.message)


pong_viewset = PongViewSet.as_view()
ping_viewset = PingViewSet.as_view()
