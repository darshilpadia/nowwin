"""kiosk URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .settings import BASE_DIR, TEMPLATE_DIR, STATICFILES_DIRS
from UI.views import *

print('bd', BASE_DIR)
print('td', TEMPLATE_DIR)
print('sd', STATICFILES_DIRS)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/kiosk/', include('API.urls')),
    url(r'^login$', login, name='login'),
    url(r'^$', login, name='login'),
    url(r'^brandmaster$', brandmaster, name='brandmaster'),
    url(r'^brandmaster/(?P<brand_id>\d+)/$', brandmasterbyid, name='brandmasterupdate'),
    url(r'^devicemaster$', devicemaster, name='devicemaster'),
    url(r'^brandmaster/(?P<brand_id>\d+)/$', brandmasterbyid, name='brandmasterupdate'),
    url(r'^modelmaster/(?P<model_id>\d+)/$', modelmasterbyid, name='modelmasterupdate'),
    url(r'^devicemaster/(?P<device_id>\d+)/$', devicemasterbyid, name='devicemasterupdate'),
    url(r'^modelmaster-del/(?P<model_id1>\d+)/$', del_modelmasterbyid, name='modelmasterdelete'),
    url(r'^modelmaster$', modelmaster, name='modelmaster'),
    url(r'^brandview$', brandview, name='brandview'),
    url(r'^modelview$', modelview, name='modelview'),
    url(r'^deviceview$', deviceview, name='deviceview'),
    url(r'^dashboard$', dashboard, name='dashboard'),
    url(r'^reports$', reportview, name='reports'),
    url(r'^generalreport$', generalreport, name='generalreport'),
# url(r'^userview$', userview, name='userview'),


url(r'^forgotpassword$', forgotpassword, name='forgotpassword')

]
urlpatterns += staticfiles_urlpatterns()
