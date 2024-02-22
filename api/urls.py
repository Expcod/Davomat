from django.urls import path
from . import views

urlpatterns = [
    path('staff-list', views.list_staff),
    path('staff-create', views.staff_create),
    path('attendance-create', views.attendance_create),
    path('attendance-day', views.attendance_day),

]
