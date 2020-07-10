
from django.urls import path
from .views import user_registration, user_profile


app_name = 'userprofile'
urlpatterns = [
    path('', user_registration, name='user_registration'),
    path('profile/', user_profile, name='user_profile'),
]
