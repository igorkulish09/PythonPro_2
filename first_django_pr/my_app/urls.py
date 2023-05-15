
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index' ),
    path("login/", views.login, name="login"), # додав
    path("grade/", views.grade, name="grade"),#додав
    path("course/", views.course, name="course"),# додав
]