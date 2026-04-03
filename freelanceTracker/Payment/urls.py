from django.urls import path
from . import views

urlpatterns = [
path('addPayment/<int:id>/',views.addPayment,name='add-payment'),
path('updatePayment/<int:id>/',views.updatePayment,name='update-payment'),
path('deletePayment/<int:id>/',views.deletePayment,name='delete-payment'),
]