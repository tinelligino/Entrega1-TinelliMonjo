# Entrega1-TinelliMonjo
CoderHouse Proyecto Entrega Final - Alumnos: Gino Tinelli-Santiago Monjo 


>>*Video con la demostracion de la funcionalidad del proyecto*
>>##### https://drive.google.com/drive/folders/1r5RGgo6y6xo0j-3wGlS_-q14_LijDmlL?usp=share_link
>
> ### Direcciones web y sus funciones segun la vista del usuario (publico o logueado):
> #### Vista de un usuario publico (no logueado):
>
>>*/login/*
>>##### Para iniciar sesion.
>
>> */home/* 
>> ##### Muestra la pagina principal con los post creados por demas usuarios.
>
>>*/about/*
>>##### Informacion acerca de los Alumnos que trabajaron en este proyecto.
>
>>*/posts/*
>>##### Para ver todos los posts creados por demas usuarios.
>
>>*/search/*
>>##### Para buscar los posts deseados.
>
> #### Vista de un usuario que se esta logueando o ya lo esta:
>
>> */home/* 
>> ##### Muestra la pagina principal con los post creados por demas usuarios.
>
>>*/about/*
>>##### Informacion acerca de los Alumnos que trabajaron en este proyecto.
>
>>*/posts/*
>>##### Para ver todos los posts creados por demas usuarios.
>
>>*/search/*
>>##### Para buscar los posts deseados.
>
>>*/mensajeria/CoderHouse/*
>>##### Para poder chatear con demas usuarios ya logueados.
>
>>*/perfil/*
>>##### Para ver el perfil del usuario.
>
>>*/profile/update/*
>>##### Para editar datos del perfil creado.
>
>>*/password/update/*
>>##### Para cambiar la contraseña del perfil creado.
>
>>*/logout/*
>>##### Para cerrar/finalizar sesion.
>
> #### Vista de un admin:
>
>>*/admin/login/*
>>##### Para iniciar sesion con un usuario administrador.
>
>>*/admin/*
>>##### Interfaz con todas las opciones validas para un administrador que inicio sesion correctamente.
>
> #### Directorio de proyecto:
>
>> - EntregaFinalTinelliMonjo  *(Directorio Raiz)
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
>>          -room.html (Contiene el chat y toda su estructura)
>>      - models.py (Contiene las clases Author, Category, Post, Perfil, Suscripcion, UserColaborator, PostUserColaborator, en el models.py de mensajeria se encuentran las clases Room y Message)
>>      - forms.py (Contiene las clases UserRegisterForm, EditarPerfilFormulario)
>>      - urls.py (contiene urls de creacion, visualizacion, index y "acerca de", en el urls de mensajeria podemos encontrar las urls del chat)
>>      - views.py (Contiene funciones de visualizacion, creacion y edicion de usuarios, ademas de cambio de contraseña. En el views de mensajeria se encuentran las funciones del chat, envio de mensaje y su guardado)
>> - db.sqlite3  (Base de datos)
>> - Requirements.txt  (Requerimientos utilizados y fundamentales para iniciar y ejecutar el proyecto, se creó utilizando el siguiente comando: pip freeze > requirements.txt)
>
>>*Datos de ADMIN para poder iniciar sesion*
>>##### Usuario: admin - Contraseña: contraseña