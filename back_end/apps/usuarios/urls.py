from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('login/', views.do_login, name="login"),
    path('cadastro/', views.cadastro, name="cadastrar"),
    path('logout/', views.do_logout, name="logout"),
    
]
