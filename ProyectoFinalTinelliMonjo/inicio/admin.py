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
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['author','timestamp','created','updated']
    list_display = ('author','title','post_categories','featured')
    ordering = ('author', 'title','featured')
    search_fields = ('author','title','featured')
    date_hierarchy = 'created'
    list_filter = ('created','author','featured')
    def post_categories(self, obj):
        return ", ".join(
            [c.title for c in obj.categories.all().order_by("title")])
    post_categories.short_description = "Categorías"
admin.site.register(Perfil)
admin.site.register(Suscripcion)
admin.site.register(PostUserColaborator)
admin.site.register(UserColaborator)
