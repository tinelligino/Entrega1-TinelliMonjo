from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from inicio.views import home,about,post,allposts,search,postlist
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^media/(?P<path>.)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.)$', serve,{'document_root': settings.STATIC_ROOT}),
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("post/<str:slug>/", post, name="post"),
    path("postlist/<str:slug>/", postlist, name="postlist"),
    path("posts/", allposts, name="allposts"),
    path("search/", search, name="search"),
    
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)