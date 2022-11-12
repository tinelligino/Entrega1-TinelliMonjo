from django.urls import path
from django.conf import settings
from .views import register, login, perfil, profileupdate, Passwordupdate
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("register", register,name="register"),
    path("login/", login, name="login"),
    path("perfil/", perfil, name="perfil"),
    path("logout",LogoutView.as_view(template_name="logout.html"),name="logout"),
    path("profile/update/", profileupdate, name="profileupdate"),
    path("password/update/", Passwordupdate.as_view(),name="passwordupdate"),
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)