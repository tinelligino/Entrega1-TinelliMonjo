# Entrega1-TinelliMonjo
CoderHouse Proyecto Entrega Final - Alumnos: Gino Tinelli-Santiago Monjo 

> #### Direcciones web y sus funciones:
>
>> */home/* 
>> ##### Muestra la pagina principal
>
>>*/about/*
>>##### Informacion acerca de los Alumnos.
>
>>*/search/*
>>##### Para buscar posts.
>
>>*/posts/*
>>##### Para ver todos los posts.
>
>>*/login/*
>>##### Para iniciar sesion.
>
>>*/perfil/*
>>##### Para ver el perfil del usuario.
>
>>*/logout/*
>>##### Para cerrar/finalizar sesion.
>
>>*/profile/update/*
>>##### Para editar datos del perfil creado.
>
>>*/password/update/*
>>##### Para cambiar la contraseña del perfil creado.


> #### Directorio de proyecto
>
>> - ProyectoFinalTinelliMonjo  *(Directorio Raiz)
>>      - urls.py (Contiene las urls)
>> - home  *(Directorio de Modulo General)
>>      - static (Directorio que contiene CSS, ADMIN, CKEDITOR, ICON, IMG, JS y MEDIA )
>>      - templates (Directorio que contiene templates de la app)
>>          - about.html (Acerca de los alumnos)
>>          - base.html (La base para todos los templates)
>>          - login.html (Para ingresar un usuario o Registrarse)
>>          - logout.html (Para cerrar sesion)
>>          - navbar.html (Botones de acceso directo a Home, Acerca de nosotros, Post, Login, Logout)
>>          - passwordupdate.html (Cambio de contraseña)
>>          - perfil.html (Informacion del usuario)
>>          - post_list.html (Lista de post creados)
>>          - post.html (Post)
>>          - profileupdate.html (Editar datos del perfil del usuario)
>>          -register.html (Para registrar un usuario)
>>          -search_bar.html (Para buscar un post y ver la informacion)
>>      - models.py (Contiene las clases Author, Category, Post, Perfil, Suscripcion, UserColaborator, PostUserColaborator)
>>      - forms.py (Contiene las clases UserRegisterForm, EditarPerfilFormulario)
>>      - urls.py (contiene urls de creacion, visualizacion, index y "acerca de" )
>>      - views.py (Contiene funciones de visualizacion, creacion y edicion de usuarios, ademas de cambio de contraseña. )
>> - db.sqlite3  (Base de datos)
>> - Requirements.txt  (Requerimientos utilizados y fundamentales para iniciar y ejecutar el proyecto, se creó utilizando el siguiente comando: pip freeze > requirements.txt)