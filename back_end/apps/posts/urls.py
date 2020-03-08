from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_posts, name="listar"),
    path('adicionar', views.adicionar_post, name="adicionar"),
    path('deletar/<int:id>', views.deletar, name="deletar"),
    path('curtir/', views.curtir_post, name="curtir"),
   
]

