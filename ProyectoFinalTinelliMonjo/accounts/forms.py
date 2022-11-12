from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from inicio.models import Suscripcion,Perfil
from django import forms
from ckeditor.fields import RichTextField


class UserRegisterForm(UserCreationForm):

    
    email = forms.EmailField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Re Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        help_texts = {key:'' for key in fields} 

def ListarSuscripcion():
    
    result = Suscripcion.objects.all().values_list("id", "name")
    
    return list(result)


class EditarPerfilFormulario(forms.Form):
    profile_picture = forms.ImageField( label='Avatar', 
        
                                        required=False
    )
    first_name = forms.CharField(   label='Nombre'  ,
                                    widget=forms.TextInput(attrs={
        'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light',
        'placeholder': 'Ingresa tus Nombres(s) : eg John Luis',        
        })
    )
    last_name = forms.CharField(    label='Apellido',
                                    widget=forms.TextInput(attrs={
        'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light',
        'placeholder': 'Ingresa tus Apellidos(s) : eg Snow Sanchez',        
        })
    )
    email = forms.EmailField(   label='Email Principal: ',
                                widget=forms.TextInput(attrs={
        'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light',
        'placeholder': 'Ingresa tu Email : eg Jhon.Snow@CoderHouse.info',
        })
    )
    email_colaborator = forms.EmailField(   label='Email Secundario (Colaborador):',
                                widget=forms.TextInput(attrs={
        'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 ,dark:shadow-sm-light',
        'placeholder': 'Ingresa tu Email : eg Jhon.Snow@CoderHouse.info',
        })                                         
    )
    description = forms.CharField(  widget=forms.Textarea(attrs={
        'class':'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg shadow-sm border border-gray-300 focus:ring-primary-500 focus:border-primary-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500',
        'rows':'8',
        }), 
    )
    perfil =  forms.ChoiceField(    label='Perfil', 
                                    widget=forms.Select(attrs={
        'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }), 
                                    choices=list(Perfil.objects.all().values_list("id", "name") ) ,
                                    required = True,
                                )
    suscripcion = forms.ChoiceField(    label='Suscripcion', 
                                        widget=forms.Select(attrs={
        'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        }), 
                                    choices=ListarSuscripcion(),
                                    required = True,                                        
    )
    linkedin = forms.CharField(   label='LinkedIn: ',
                                widget=forms.TextInput(attrs={
        'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500 dark:shadow-sm-light',
        'placeholder': 'Ingresa tu LinkedIn : eg www.linkedin/jhon.snow',
        })
    )