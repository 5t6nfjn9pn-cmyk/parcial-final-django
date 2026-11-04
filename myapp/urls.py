from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile_list, name="profile_list"),
    path("new/", views.profile_create, name="profile_create")
]