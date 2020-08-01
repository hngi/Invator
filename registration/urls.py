
from django.contrib import admin
from django.urls import path, include
from registration import views as v
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.conf import settings

urlpatterns = [
    path('register/', v.register, name="register"),
    path('register_user/', v.register_u, name="register user"),
    path('login/', v.login, name="login"),
   # path('dashboard/', v.dashboard, name="Dashboard"),
    path('logout/', v.logout, name="logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path('reset_form/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/reset_form.html"), name="password_reset_confirm"),
    path('reset_password_completed/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_completed.html"), name="password_reset_complete"),

    # path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
