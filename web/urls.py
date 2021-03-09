"""web URL Configuration

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
from myweb import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^admin/',admin.site.urls),
    #url(r'^index/',include('myweb.urls')),
    path('index/',views.index,name='index'),
    path('about/',views.about),
    path('blog/',views.blog),
    path('contact/',views.contact),
    path('profile/',views.profile,name='profile'),
    path('recipe/',views.recipe),
    path('logi/',views.logi,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('cpass/',views.cpass,name='cpass'),
    path('c/',views.c,name='c'),
    path('userdetail/<int:id>',views.userdetail,name='userdetail'),
    path('index/emaill',views.emaill,name='emaill')

]
