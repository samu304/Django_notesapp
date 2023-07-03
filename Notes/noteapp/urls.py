from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("newnote/", views.new_note, name="new_notes"),
    path("update/<int:id>", views.update_note, name="update_notes"),
    path("delete/<int:id>", views.delete_note, name="delete_notes"),
    path("search/", views.search_note, name="search_notes"),
]
