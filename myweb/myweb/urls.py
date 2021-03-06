"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse
from django.template import loader

def main_page(req):
    template=loader.get_template('home.html')
    data={}
    response=template.render(data,req)
    return HttpResponse(response)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_2/',include('home_2.urls')),
    path('about/',include('product.urls')),
    path('',main_page)
]
