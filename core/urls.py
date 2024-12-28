from django.urls import path
from . import views
from.views import home
from.views import culture
from.views import signup
from.views import login

urlpatterns = [
    path('Homepage/', home, name='Homepage'),
    path('Culture/', culture, name='culture'),
     path('Signup/', signup, name='signup'),
    path('login/',   login , name='login')

    
    ]