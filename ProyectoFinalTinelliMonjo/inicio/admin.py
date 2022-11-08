from django.contrib import admin
from .models import Author, Category, Post, Perfil, Suscripcion, PostUserColaborator, UserColaborator
#admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    list_display = ['__str__']
    ordering = ['user']
    search_fields = ['user']
    date_hierarchy = 'created'
    list_filter = ('created','user')

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Perfil)
admin.site.register(Suscripcion)
admin.site.register(PostUserColaborator)
admin.site.register(UserColaborator)
