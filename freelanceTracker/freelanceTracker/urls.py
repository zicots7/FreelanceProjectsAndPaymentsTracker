"""
URL configuration for freelanceTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("accounts.urls")),
    path('client/',include("Client.urls")),
    path('milestone/',include("Milestone.urls")),
    path('payment/',include("Payment.urls")),
    path('project/',include("Project.urls")),
    path('Invoice/',include("Invoice.urls")),
    path('client_portal/',include("client_portal.urls")),
    path('admin_portal/',include("admin_portal.urls")),
    path('logs/',include("Logs.urls")),
    # Path to download the schema file (YAML/JSON)
    #path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Path to view the interactive Swagger UI
    #path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]



"""
each apps views urls are handled within their own url
separately within their url each time their names are called 
"""