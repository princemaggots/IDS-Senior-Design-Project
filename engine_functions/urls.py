from django.urls import path

from . import views

urlpatterns =   [
                    path("", views.index, name="index"),
                    path("lccde_run", views.lccde_run, name="lccde_run"),
                ]