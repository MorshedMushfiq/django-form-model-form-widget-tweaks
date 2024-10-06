
from django.urls import path
from authApp.views import loginPage, register, home, logoutPage, add_student


urlpatterns = [
    path('', loginPage,  name='loginPage'),
    path('register/', register,  name='register'),
    path('home/', home,  name='home'),
    path('add_student/', add_student,  name='add_student'),
    path('logout/', logoutPage,  name='logoutPage'),
]
