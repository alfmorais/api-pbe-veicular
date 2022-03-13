from django.urls import path

from . import views

urlpatterns = [
    path("pong/", views.pong_viewset, name="pong_viewset"),
    path("ping/", views.ping_viewset, name="ping_viewset"),
]
