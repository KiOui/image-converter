from django.urls import path
from rest_framework.schemas import get_schema_view

from converter.api.openapi import OpenAPISchemaGenerator
from .views import ConvertAPIView

app_name = "converter"

urlpatterns = [
    path("convert", ConvertAPIView.as_view(), name="convert"),
    path(
        "schema",
        get_schema_view(
            title="API v1",
            url="/api/v1/",
            version=1,
            urlconf="converter.api.v1.urls",
            generator_class=OpenAPISchemaGenerator,
        ),
        name="schema-v1",
    ),
]
