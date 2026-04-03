from django.urls import path
from . import views

urlpatterns = [
    path('projectList/',views.projectList,name="project-list"),
    path('addProject/',views.addProject,name="project-add"),
    path('updateProject/<int:id>/',views.updateProject,name="project-update"),
    path('deleteProject/<int:id>/',views.deleteProject,name="project-delete"),
    path('detailsProject/<int:id>/',views.projectDetails,name="project-details"),
]