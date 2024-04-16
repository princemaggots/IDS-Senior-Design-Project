from django.urls import path

from . import views

urlpatterns =   [
                    path("", views.index, name="index"),
                    path("save", views.store_entry, name="save"),
                    path("get_entry", views.get_entry, name="get_entry"),
                    path("get_history", views.get_history, name="get_history"),
                    path("delete_entry", views.delete_entry, name="delete_entry"),
                ]