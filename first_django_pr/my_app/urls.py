from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index' ),
    path("week/", views.my_week, name="my_week"),
    #path("day/<int:week_day_id>/note/<int:note_id>", views.my_day, name="week_day"),
    path("day/<int:week_day_id>/", views.my_day, name="week_day"),
    #path("note/<int:note_id>/", views.my_day, name="note_detail"),
    path('note/<int:week_day_id>/', views.my_day, name='note_detail')

]
