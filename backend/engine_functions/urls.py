from django.urls import path

from . import views

urlpatterns =   [
                    path("", views.index, name="index"),
                    path("lccde_run", views.lccde_run, name="lccde_run"),
                    path("treebased_run", views.treebased_run, name="treebased_run"),
                    path("mth_run", views.mth_run, name="mth_run"),
                ]