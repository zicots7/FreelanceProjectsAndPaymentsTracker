from django.urls import path
from .views import Client_list,add_client,delete_client,update_client

urlpatterns = [
    path('list/',Client_list,name='client_list'),
    path('add/',add_client,name='add_client'),
    path('remove/<int:id>/',delete_client,name='delete_client'),
    path('update/<int:id>/',update_client,name='update_client'),

]
