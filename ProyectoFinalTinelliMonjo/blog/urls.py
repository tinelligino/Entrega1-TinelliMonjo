from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from blog.views import home,about,post,allposts,search,login,perfil
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^media/(?P<path>.)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.)$', serve,{'document_root': settings.STATIC_ROOT}),
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("post/<str:slug>/", post, name="post"),
    path("posts/", allposts, name="allposts"),
    path("search/", search, name="search"),
    path("login/", login, name="login"),
    path("perfil/", perfil, name="perfil"),
    path("logout",LogoutView.as_view(template_name="logout.html"),name="logout"),
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)