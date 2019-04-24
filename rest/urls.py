from rest_framework.routers import DefaultRouter
from .views import UrlViewset
from django.urls import re_path
urlpatterns = [
    re_path("(?P<pk>\w*)",UrlViewset.as_view(),name="url"),
]