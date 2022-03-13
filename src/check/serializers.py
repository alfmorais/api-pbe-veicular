from rest_framework import serializers


class PingSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=100)


class PongSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=100)
