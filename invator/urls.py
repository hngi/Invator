from django.urls import path, include
from . import views
from .views import InvoiceSearch
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('invoice/', views.invoice, name="invoice"),
    #path('invoice/<int:pk>/', views.invoice_detail_view, name="invoice_detail"),
    #path('invoice/update/<int:pk>/', views.invoice_update_view, name="invoice_update"),
    path('contact/', views.contact_page, name="contact"),
    path('searchbar/', InvoiceSearch.as_view(), name='searchbar'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('invoice-data/', views.invoice_data, name="invoice_data"),
    path('preview/<str:id>', views.preview_template, name="preview_template"),
    path('download/<str:id>/', views.download_to_pdf, name="download_to_pdf"),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
