"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from passwording import views
from django.urls import include
from signuser.views import signupuser, logoutuser, loginuser



urlpatterns = [
    path('home/', views.generate, name='password'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('signup/', signupuser, name='signup'),
    path('mytodos/', views.currenttodos, name='currenttodos'),
    path('mytodos/create', views.createtodo, name='createtodo'),
    path('logout/', logoutuser, name='logoutuser'),
    path('login/', loginuser, name='loginuser'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.complete, name='complete'),
    path('todo/<int:todo_pk>/delete', views.delete, name='delete'),
    path('passed/', views.test, name='passed'),


]
