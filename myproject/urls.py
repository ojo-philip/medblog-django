"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include
from userprofile.views import search_query
from userprofile.forms import MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', include('blog.urls')),
    path('register', include('userprofile.urls')),
    path('search/', search_query, name='search_query'),
    path('reset-password/', auth_view.PasswordResetView.as_view(template_name='userprofile/password_reset.html', form_class=MyPasswordResetForm),
         name='reset_password'),
    path('reset-password/done/', auth_view.PasswordResetDoneView.as_view(template_name='userprofile/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='userprofile/password_reset_confirm.html', form_class=MySetPasswordForm),
         name='password_reset_confirm'),
    path('reset-password-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='userprofile/password_reset_complete.html'),
         name='password_reset_complete'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
