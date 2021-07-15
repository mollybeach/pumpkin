
from django.contrib import admin
from django.urls import path
from . import views
#from django.urls import path, include <- add this to line 17
# #if local host isnt open and is stuck on the django template and isn't showing hey welcome 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #path('', include('myapp.urls) #if local host isnt opening add this line here 
    path('counter', views.counter, name='counter') ,#at the moment we dont have any function called 
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post') ,#<--- dynamic 
    path('profile', views.profile, name='profile') 
] 
#view.counter so lets go create that so go into the views.py 
# put #about #whatever to scroll to that part with a href html tag 





"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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