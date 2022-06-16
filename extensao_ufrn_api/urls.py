from django.contrib import admin

from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/extensao_ufrn_api/', include('users.urls')),
]
