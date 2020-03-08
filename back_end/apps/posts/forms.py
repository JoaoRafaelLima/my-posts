from django import forms
from .models import Post



class FormPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('conteudo',)


