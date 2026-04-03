from django.urls import path
from . import views

urlpatterns =[
    path('admin_addLogs/<int:id>',views.admin_addLogs,name='add-logs'),
    path('logs/<int:id>',views.logs,name='logs'),
    path('admin_deleteLogs/<int:id>/<str:log_id>',views.admin_deleteLogs,name='delete-logs'),

]