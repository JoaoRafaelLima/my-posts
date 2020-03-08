from django.shortcuts import render, redirect, get_object_or_404
# from ...utils.form import com_autenticacao
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import MyUser
from ..posts.models import Post
from ..posts.models import CurtidaPost
# Create your views here.



@login_required
def home(request):
    posts = None
    print(request.session.items())
    print(request.session['_auth_user_id'])
    usuario = get_object_or_404(MyUser, pk=request.session['_auth_user_id'])

    try:
        posts = Post.objects.filter(usuario=usuario).order_by('-created_at')
        context = []
        tmp = {}
        for post in posts:
            curtidas = CurtidaPost.objects.filter(post=post)
            tmp['post'] = post
            tmp['curtidas'] = curtidas.count()
            context.append(tmp.copy())
            tmp.clear()
        
    
    except:
        print("Ainda nao tem posts")
    return render(
        request,
        'usuarios/home.html',
        {
        "usuario": usuario,
        "u_posts": context
        }
    )

def do_login(request):
    
    if request.method == "POST":
        # print("dados")
        # print(request.POST['login'])
        # print(request.POST['password'])
        #user = authenticate(request, login=request.POST["login"], password=request.POST["password"])
        user = get_object_or_404(MyUser, login=request.POST['login'])
        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("usuario nao encontrado")
    else:
        return render(request, 'usuarios/login.html')

def do_logout(request):
    logout(request)
    print("logout")
    return redirect("/login")




