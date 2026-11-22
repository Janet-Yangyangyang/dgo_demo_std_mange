from django.urls import path
from . import views


urlpatterns = [
    path('tempview/', views.temp_view),
    path('usr/', views.user),
    path('usr/ls/', views.user_ls),
    path('usr/add/', views.user_add),
    path('usr/delete/', views.user_del),
    path('grp/', views.group_manage),
    path('grp/add/', views.group_add),
]