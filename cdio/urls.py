from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
  

    path('check', views.check),
    path('', views.home,name="home"),
    path('register', views.signup,name= 'register'),
    path('dashbord', views.dashbord,name= 'dashbord'),
    path('loginform', views.sign_in,name='login'),
    path('logout', views.sign_out, name='logout'),
    path('syllubus', views.syll),
    
    
]
