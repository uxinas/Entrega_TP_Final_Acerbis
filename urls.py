from django.urls import path
from MAIN import views 
from .views import *



urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('about', views.about, name='sobre_mi'),
    path('blogs', views.blogs, name='blogs'),
    path('blog_1', views.blog_1, name='blog_1'),
    path('blog_2', views.blog_2, name='blog_2'),
    path('blog_3', views.blog_3, name='blog_3'),
    path("entradas/list/", Entradas_list.as_view(), name="entradas_list"),
    path('entradas/creacion/', Entradas_creacion.as_view(), name='entradas_creacion'),
    path('entradas/<pk>', Entradas_detalle.as_view(), name='entradas_detalle'),
    path('entradas/editar/<pk>', Entradas_update.as_view(), name='entradas_update'),
    path('entradas/borrar/<pk>', Entradas_delete.as_view(), name='entradas_delete'),
    #path('signup', views.signup, name='signup'),
    #path('login', views.login, name='login'),
    #path('LOGIN/loginFormulario', views.LoginFormulario, name='loginFormulario'),
   # path('loginFormulario', views.loginFormulario, name='loginFormmulario'),
    #path('loginFormulario', views.loginFormulario_vista, name='loginFormulario_vista'),
    ]