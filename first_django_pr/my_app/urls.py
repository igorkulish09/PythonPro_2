from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index' ),
    path("login/", views.login, name="login"),
    path("grade/", views.grade, name="grade"),
    path("course/", views.course, name="course"),
    path("week/", views.my_week, name="my_week")
]
