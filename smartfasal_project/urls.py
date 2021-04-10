"""smartfasal_project URL Configuration

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
from django.contrib import admin
from django.urls import path
from smartfasal import views
urlpatterns = [



    #path('admin/', admin.site.urls),
    #path('index', views.FTP_session_view.index, name = 'index'), ## INDEX PAGE
    #path('visualise', views.FTP_session_view.visual, name = 'visualise'), ## PLOTS PAGE
    path('live', views.Plots.ftp_login, name = 'ftp_login'), ## FTP PAGE
    #path('plots/', views.FTP_session_view.make_plots, name = 'plots'), ## plots PAGE
    #path('visualising', views.visualising, name = 'visualising'), ## PLOTS PAGE
    path('Real_time_plot', views.Plots.Real_time_plot, name = 'Real_time_plot'), ## PLOTS PAGE
    path('allreadings', views.upload_readings.allreadings, name = 'allreadings'), ## PLOTS PAGE
    path('smonereadings', views.upload_readings.smonereadings, name = 'smonereadings'), ## PLOTS PAGE
    path('smtworeadings', views.upload_readings.smthreereadings, name = 'smtworeadings'), ## PLOTS PAGE
    path('smthreereadings', views.upload_readings.smthreereadings, name = 'smthreereadings'), ## PLOTS PAGE
    path('tempreadings', views.upload_readings.tempreadings, name = 'tempreadings'), ## PLOTS PAGE
    path('humidreadings', views.upload_readings.humidreadings, name = 'humidreadings'), ## PLOTS PAGE
    path('prsrreadings', views.upload_readings.prsrreadings, name = 'prsrreadings'), ## PLOTS PAGE
    path('lmnsreadings', views.upload_readings.lmnsreadings, name = 'lmnsreadings'), ## PLOTS PAGE
    path('ARIMA', views.ARIMA_code.HEroku_ARIMA_upload, name = 'ARIMA'),

]
