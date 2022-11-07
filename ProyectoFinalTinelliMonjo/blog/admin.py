from django.contrib import admin
from .models import Author, Category, Post, Perfil, Suscripcion, PostUserColaborator, UserColaborator
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Perfil)
admin.site.register(Suscripcion)
admin.site.register(PostUserColaborator)
admin.site.register(UserColaborator)
