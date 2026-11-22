from django.urls import path
from . import views


urlpatterns = [
    path('idx/', views.indx),
    path('info/', views.info),
    path('svccent/', views.svt_cent),
    path('prodls/', views.prodls),
    path('prodadd/', views.prodadd),
    path('baidu/', views.redir),
    path('login/', views.login),
    path('userlist/', views.usr_ls_orm),
]