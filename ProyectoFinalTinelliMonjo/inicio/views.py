from django.shortcuts import render
from .models import Author, Category, Post, Perfil, Suscripcion, PostUserColaborator, UserColaborator
from django.contrib.auth.decorators import login_required


def home(request):
    categories = Category.objects.all()[0:4]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def post(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(titleicontains=query) |
            Q(overviewicontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_bar.html', context)


def allposts(request):
    posts = Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)

def login(request):
    pass

@login_required(login_url='/login')
def perfil(request):
    userColaborator, es_NuevoUserColaborator = UserColaborator.objects.get_or_create(user = request.user)
    return render(request, 'private/perfil.html',{'formulario':{}})