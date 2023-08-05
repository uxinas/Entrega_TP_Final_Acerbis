#from LOGIN.models import Login
#from django.views.generic import ListView
from django.http import HttpResponse
from LOGIN.forms import LoginFormulario
from django.shortcuts import render
from LOGIN.models import Login
from SIGNUP.models import Usuario_nuevo
from SIGNUP.views import Usuario_nuevo_Formulario_vista
from SIGNUP.forms import Usuario_nuevo_Formulario
from django.contrib.auth.decorators import login_required
from SIGNUP.models import Usuario_nuevo
from PROFILE.forms import UserRegisterForm, UserEditForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm 
from django.contrib.auth.models import User



#def login(request):
#    return render(request,'login.html')




def panelCrud(request):
    return render(request,'leer_usuarios.html')


def loginFormulario_vista(request):
    return render(request,'loginFormulario.html')


def loginFormulario(request):
    if request.method == "POST":
        miFormulario = LoginFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            usuario = Login(nombre=informacion['nombre'], 
                            email=informacion['email'],
                            password=informacion['password'])
            usuario.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = LoginFormulario()
        return render(request, 'loginFormulario.html', {'miFormulario':miFormulario})

@login_required
def leerUsuarios(request):
    usuarios = Usuario_nuevo.objects.all()
    contexto = {'Usuarios':usuarios}
    return render(request, 'leer_usuarios.html', contexto)

 

def eliminarUsuarios(request, usuario_nombre):
    usuario = Usuario_nuevo.objects.get(nombre=usuario_nombre)
    usuario.delete()

    usuarios = Usuario_nuevo.objects.all()
    contexto = {'Usuarios':usuarios}

    return render(request, 'leer_usuarios.html', contexto )


def editarUsuarios(request, usuario_nombre):
    usuario = Usuario_nuevo.objects.get(nombre=usuario_nombre)
    
    if request.method == "POST":
        miFormulario = Usuario_nuevo_Formulario (request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            usuario.nombre = informacion['nombre']
            usuario.email = informacion['email']
            usuario.password = informacion['password']

            usuario.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = Usuario_nuevo_Formulario(initial={'nombre': usuario.nombre, 'email':usuario.email , 
                                                         'password':usuario.password})
    return render(request, 'editarUsuarios.html', {'miFormulario':miFormulario, 'usuario_nombre':usuario_nombre}) 




def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "msj_usuario_logueado.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "msj_usuario_logueado.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "msj_usuario_logueado.html", {"mensaje":"El usuario ingresado no es válido."})

    form = AuthenticationForm()

    return render(request, "loginc23.html", {"form": form})




def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"msj_usuario_creado.html" ,  {"mensaje":"Usuario creado con exito!"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})
