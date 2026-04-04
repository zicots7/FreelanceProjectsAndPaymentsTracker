from django.urls import path
from .views import login_view,logout_view,demo_login
urlpatterns = [
    path('',login_view,name='accounts'),
    path('logout',logout_view,name='logout'),
    path('demo/<str:role>/',demo_login, name='demo_login'),
]