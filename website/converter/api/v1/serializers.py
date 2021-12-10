from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    """Image Serializer."""

    image = serializers.ImageField()

    def create(self, validated_data):
        """Not implemented."""
        return

    def update(self, instance, validated_data):
        """Not implemented."""
        return
