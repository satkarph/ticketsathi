from django.conf.urls import include, url
from busticketing import views   

from .views import (LoginView,index)
from . import views
urlpatterns = [ 
      url(r'home', views.index, name='index'),
      url(r'login', LoginView.as_view(), name='login'),
 ]