"""MVT_DanielPacheco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
from pipes import Template
from tempfile import template
from django.contrib import admin
from django.urls import path
from MVT_DanielPacheco.views import familiares, datosDeFamiliares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Familiares/', familiares),
    path('Datos/', datosDeFamiliares)

]
