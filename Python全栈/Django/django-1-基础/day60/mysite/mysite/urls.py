"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an impor # url(r'^yingying/$', views.yingying),t:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    #  --------- day60 ↓ ---------------
    url(r'^press_list/$', views.press_list),  # 展示出版社
    url(r'^add_press/$', views.add_press),  # 添加出版社
    url(r'^delete_press/$', views.delete_press),  # 删除出版社
    url(r'^edit_press/$', views.edit_press),  # 编辑出版社
]
