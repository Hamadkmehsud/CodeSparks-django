from . import views
from django.urls import path


urlpatterns = [
    path('create-profile/', views.create_profile, name='create-profile'),  # Ensure this matches the name used in the template
    path('login/', views.login, name='login')
]