from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('searchbar/', views.searchbar, name='searchbar'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('preview/<str:id>', views.preview_template, name="preview_template"),
    path('<str:id>/', views.download_to_pdf, name="download_to_pdf"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)