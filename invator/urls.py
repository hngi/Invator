from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:id>/', views.download_to_pdf, name="download_to_pdf"),
    path('preview/<str:id>', views.preview_template, name="preview_template"),
    path('searchbar/', views.searchbar, name='searchbar')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)