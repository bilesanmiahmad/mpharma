"""challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from diagnosis.views import CategoryViewset, DiagnosisViewset

router = DefaultRouter()
router.register(r'categories', CategoryViewset, base_name='categories')
router.register(r'diagnosis', DiagnosisViewset, basename='diagnosis')

schema_view = get_swagger_view(title='mPharma Diagnosis Code API Docs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path(r'docs/', schema_view),
]

admin.site.site_header = 'mPharma Diagnosis Codes'