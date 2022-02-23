from rest_framework import serializers


class PingSerializer(serializers.Serializer):
    status = serializers.BooleanField()
    message = serializers.CharField(max_length=100)


class PongSerializer(serializers.Serializer):
    status = serializers.BooleanField()
    message = serializers.CharField(max_length=100)
