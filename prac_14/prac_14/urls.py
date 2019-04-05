"""prac_14 URL Configuration

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
from django.urls import path
from firstapp.views import (BlogCreateView,BlogListView,
                            BlogDetailView,IndexView,UserLogin,
                            UserLogout,register,BlogUpdateView,BlogDeleteView)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('signhere/',register,name='register'),
    path('login/',UserLogin.as_view(),name='Login'),
    path('Logout/',UserLogout.as_view(),name='logout'),
    path('lists/',BlogListView.as_view(),name='blog-list'),
    path('lists/<int:pk>/',BlogDetailView.as_view(),name='blog-detail'),
    path('create/',login_required(BlogCreateView.as_view()),name='blog-create'),
    path('admin/', admin.site.urls),
    path('update/<int:pk>',login_required(BlogUpdateView.as_view()),name='update'),
    path('delete/<int:pk>',login_required(BlogDeleteView.as_view()),name='delete'),
]
