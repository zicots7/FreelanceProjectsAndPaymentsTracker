from django.urls import path
from .views import *
urlpatterns = [
    path('requestInvoice/<int:id>/',clientinvoiceDownload,name='invoice-request'),
    path('invoiceDownload/<int:id>/',invoiceDownload,name='invoice-download'),
]