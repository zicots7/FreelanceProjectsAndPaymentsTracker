from django.urls import include,path
from . import views
urlpatterns = [
path('',views.dashboard,name='client-dashboard'),
path('projects/',views.clientProjectList,name='client-project-list'),
path('clientDownloadInvoice/<int:id>',views.downloadInvoice,name='client-download-invoice'),
path('clientProjectDetails/<int:id>',views.clientProjectDetails,name='client-project-details'),
path('client_deleteLogs/<int:id>/<str:log_id>',views.client_deleteLogs,name='client-deleteLogs'),
path('client_addLogs/<int:id>',views.client_addLogs,name='client-addLogs'),
    ]