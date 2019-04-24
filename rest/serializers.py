from rest_framework.serializers import ModelSerializer
from .models import UrlModel


class UrlSerializer(ModelSerializer):
    class Meta:
        model = UrlModel
        fields = ("url","pk")
