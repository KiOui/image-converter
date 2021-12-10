from rest_framework.renderers import BaseRenderer


class BinaryFileRenderer(BaseRenderer):
    """Binary File Renderer."""

    media_type = "application/octet-stream"
    format = None
    charset = None
    render_style = "binary"

    def render(self, data, media_type=None, renderer_context=None):
        """Render a binary file."""
        return data
