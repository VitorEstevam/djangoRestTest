from django.urls import include, path

from rest_framework import routers
from . import views

api_router = routers.DefaultRouter()
api_router.register(r"musics", views.MusicList)

urlpatterns = [
     path("api/", include(api_router.urls)),
]