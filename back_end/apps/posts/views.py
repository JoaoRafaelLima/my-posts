from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Post, CurtidaPost
from .forms import FormPost
# Create your views here.

@login_required
def listar_posts(request):
    context = []
    tmp = {}
    posts = Post.objects.all().order_by('-created_at')
    for post in posts:
        curtidas = CurtidaPost.objects.filter(post=post)
        tmp['post'] = post
        tmp['curtidas'] = curtidas.count()
        context.append(tmp.copy())
        tmp.clear()
    print(context)
    return render(
        request,
        'posts/listar.html',
        {
            "posts": context
        }
    )
@login_required
def adicionar_post(request):
    if request.method == "POST":

        form = FormPost(request.POST)
        print(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            return redirect('/')
        else:
            return HttpResponse("erro")
    else:
        return render(request, 'posts/adicionar.html')


@login_required
def deletar(request, id):
    try:
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return redirect('/home')
    except:
        return HttpResponse("ocorreu um erro")


def curtir_post(request):
    if request.is_ajax() and request.method == "POST":
        print(request.POST)
        curtida_post = CurtidaPost()
        curtida_post.post = get_object_or_404(Post, pk=request.POST['id_post'])
        curtida_post.usuario = request.user
        print(curtida_post)
        curtida_post.save()
        
        return HttpResponse(json.dumps(request.POST))
    else:
        return HttpResponse("")


