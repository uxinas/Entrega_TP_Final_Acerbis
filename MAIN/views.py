from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from MAIN.models import Entradas_Blog
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


#from LOGIN.models import Login
#from LOGIN.forms import LoginFormulario
#from LOGIN import *

@login_required
def inicio(request):
    return render(request,'inicio.html')


#def signup(request):
    #return render(request,'signup.html')

def about(request):
    return render(request,'about.html')

def blogs(request):
    return render(request,'blogs.html')

def blog_1(request):
    return render(request,'blog_1.html')

def blog_2(request):
    return render(request,'blog_2.html')

def blog_3(request):
    return render(request,'blog_3.html')



class Entradas_list(ListView):
    model =Entradas_Blog
    template_name = 'blogs_list.html'



class Entradas_creacion(CreateView):
    model = Entradas_Blog
    template_name = "blog_creacion.html"
    success_url = reverse_lazy("entradas_list")
    fields = '__all__'


class Entradas_detalle(DetailView):
    model = Entradas_Blog
    template_name = 'blogs_detalle.html'


class Entradas_delete(DeleteView):
    model = Entradas_Blog
    success_url = reverse_lazy("entradas_list")


class Entradas_update(UpdateView):
    model = Entradas_Blog
    success_url = reverse_lazy('entradas_list')
    fields = ['Nombre', 'Fecha', 'Titulo', 'Subtitulo', 'Post']




#def login(request):
    #return render(request,'login.html')

#def loginFormulario_vista(request):
    #return render(request,'loginFormulario.html')

"""
def LoginFormulario(request):
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

"""
"""
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
        return render(request, 'login.html', {'miFormulario':miFormulario})
    """