"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from fileServer import views as fileViews
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',fileViews.login),
    url(r'^register/',fileViews.register),
    url(r'^registerBehavior',fileViews.registerBehavior),
    url(r'^loginBehavior',fileViews.loginBehavior),
    url(r'^contentPage',fileViews.contentPage),
    url(r'^saveFile',fileViews.saveFile),
    url(r'^downloadFile',fileViews.downloadFile),
]
