from django.db import models
from ..usuarios.models import MyUser
# Create your models here.


class Post(models.Model):
    usuario = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    conteudo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "post"


class CurtidaPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    def __str__(self):
        return "curtida"
