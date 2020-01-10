"""chilequiere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = DefaultRouter()
router.register(r'infofam', views.InfoFamViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),                             # admin view
    url(r'^$', views.index, name='home'),                        # index view
    url(r'^simulacion', views.simulation_result, name='simulation'),# fam result
    # url(r'^min', views.mininc_result, name='min_income'),      # phase 2

    # ==================== REST FRAMEWORK URLS =========================== #
    path('', include(router.urls))
    # path('api/app/', include('app.api.urls', 'app_api'))


]


urlpatterns += staticfiles_urlpatterns()
