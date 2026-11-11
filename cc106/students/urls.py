from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),                     # This makes http://127.0.0.1:8000/ your landing page
    path('registration/', views.register_student, name='registration'), # This keeps your form at /registration/
]