from django.urls import path
from . import views


urlpatterns = [
path('addMilestone/<int:id>/',views.addMilestone,name='add-milestone'),
path('deleteMilestone/<int:id>/',views.deleteMilestone,name='delete-milestone'),
path('updateMilestone/<int:id>/',views.updateMilestone,name='update-milestone'),
]