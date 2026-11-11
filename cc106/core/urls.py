from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('students.urls')),
    path('', RedirectView.as_view(url='registration/students/', permanent=False)), # Redirects root URL to the student directory
]