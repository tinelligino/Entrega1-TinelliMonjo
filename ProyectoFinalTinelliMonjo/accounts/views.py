from django.shortcuts import render,redirect
from inicio.models import User, UserColaborator, Suscripcion, Perfil
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth import login as django_login
from .forms import EditarPerfilFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView


def register(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = User.objects.filter(username=f"{ request.POST['username']}").first()
            userColaborator, es_NuevoUserColaborator = UserColaborator.objects.get_or_create(user = user)
            return redirect('home')    
    else: 
        formulario = UserRegisterForm()
    return render(request, 'register.html',{'formulario':formulario})

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        formulario = AuthenticationForm()
        result =  lambda a=1,b=2: str(random.randint(a,b)) +'.jpg'
        context = {
                'formulario':formulario,
                'result': {'image': result(1,3)},
        }
        return render(request, 'login.html',context)
    if request.method == 'POST':
        formulario = AuthenticationForm(request,data= request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            django_login(request,user)
            return redirect('home')
        else:
            result =  lambda a=1,b=2: str(random.randint(a,b)) +'.jpg'
            context = {
                'formulario':formulario,
                'result': {'image': result(1,3)},
                'error' : {'detalle':'Usuario o Contrasena errados,Re intente nuevamente ...'}
            }
            return render(request, 'login.html',context)

@login_required(login_url='/login')
def perfil(request):
    userColaborator, es_NuevoUserColaborator = UserColaborator.objects.get_or_create(user = request.user)
    return render(request, 'perfil.html',{'formulario':{}})

@login_required(login_url='/login')
def profileupdate(request):
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST,request.FILES)
        if formulario.is_valid():
            datanueva = formulario.cleaned_data
            request.user.first_name = datanueva['first_name']
            request.user.last_name = datanueva['last_name']
            request.user.email = datanueva['email']
            request.user.usercolaborator.email = datanueva['email_colaborator']
            request.user.usercolaborator.description = datanueva['description']
            request.user.usercolaborator.perfil =  Perfil.objects.filter(id=f"{datanueva['perfil']}").first()
            request.user.usercolaborator.suscripcion = Suscripcion.objects.filter(id=f"{datanueva['suscripcion']}").first()
            request.user.usercolaborator.linkedin = datanueva ['linkedin']
            if(datanueva['profile_picture'] != None ):
                request.user.usercolaborator.profile_picture = datanueva['profile_picture']
            request.user.usercolaborator.save()
            request.user.save()
            return redirect('perfil')
    else:
        formulario = EditarPerfilFormulario(
            initial={   'first_name': request.user.first_name, 
                        'last_name': request.user.last_name,
                        'email': request.user.email,
                        'email_colaborator': request.user.usercolaborator.email,
                        'description': request.user.usercolaborator.description,
                        'perfil': request.user.usercolaborator.perfil.id,
                        'suscripcion': request.user.usercolaborator.suscripcion.id,
                        'profile_picture' : request.user.usercolaborator.profile_picture,
                        'linkedin' : request.user.usercolaborator.linkedin
                    }
        )
    return render(request, 'profileupdate.html',{'formulario':formulario})

class Passwordupdate(LoginRequiredMixin,PasswordChangeView):
    template_name = 'passwordupdate.html'
    success_url = '/perfil/'
    login_url = '/login/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context