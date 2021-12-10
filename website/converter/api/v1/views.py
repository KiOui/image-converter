import io

from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from converter.api.v1.renderers import BinaryFileRenderer
from converter.api.v1.serializers import ImageSerializer
from PIL import Image, UnidentifiedImageError
from pathlib import Path


class ConvertAPIView(APIView):
    """Convert API View."""

    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ["read", "write"]
    serializer_class = ImageSerializer
    renderer_classes = [BinaryFileRenderer]

    def post(self, request):
        """Convert image to webp format."""
        try:
            image = Image.open(request.data["image"])
            filename = Path(request.data["image"].name)
            new_filename = filename.with_suffix(".webp")
            webp_buffer = io.BytesIO()
            image.save(webp_buffer, format="webp")
            webp_buffer.name = request.data["image"].name
            webp_buffer.seek(0)
            return Response(
                status=HTTP_200_OK,
                data=webp_buffer,
                headers={"Content-Disposition": 'attachment; filename="{}"'.format(new_filename)},
            )
        except UnidentifiedImageError:
            return Response(status=HTTP_400_BAD_REQUEST)
