
from django.contrib import admin
from django.urls import path, include
from registration import views as v
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('register/', v.register, name="register"),
    path('register_user/', v.register_u, name="register user"),
    path('login/', v.login, name="login"),
    path('dashboard/', v.dashboard, name="Dashboard"),
    path('logout/', v.logout, name="logout"),
    # path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
