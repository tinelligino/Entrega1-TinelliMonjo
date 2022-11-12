from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class Author(models.Model):
    """Author utilizando el listado de Users del sistema"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)
    def __str__(self):
        return f"""{self.user.first_name} {self.user.last_name} """
    class  Meta:
        verbose_name = "Autor"
        verbose_name_plural  =  "Author [ Autor ]"

class Category(models.Model):
    """Category que agrupa Post"""

    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    """Post"""

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)


    def __str__(self):
        return self.title

class Perfil(models.Model):
    """Perfil :  """
    name = models.CharField(max_length=50)
    createdate = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)

    def __str__(self):
        return self.name 
    class  Meta:   #new
        verbose_name_plural  =  "User Colaborator Perfils"

class Suscripcion(models.Model):
    name = models.CharField(max_length=50)
    createdate = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)

    def __str__(self):
        return self.name
    class  Meta:   #new
        verbose_name_plural  =  "User Colaborator Suscripcions"

class UserColaborator(models.Model):
    email = models.EmailField(max_length=200)
    description = models.TextField()
    profile_picture = models.ImageField(upload_to ='avatar',max_length=None, blank=True,null=True)
    perfil= models.ForeignKey(Perfil, on_delete=models.CASCADE, default=1 )
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE, default=1)
    createdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)
    linkedin = models.TextField(max_length=100, blank=True,null=True)

    def __str__(self):
        return  f""" {self.email}  """
    class  Meta:
        verbose_name_plural  =  "User colaborators"

class PostUserColaborator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True,null=True)#
    createdate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",blank=True,null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición",blank=True,null=True)

    def __str__(self):
        return self.title

    class  Meta:
        verbose_name_plural  =  "User Post colaborators"
