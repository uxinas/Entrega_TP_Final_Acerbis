from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from LOGIN import views

#from MAIN import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('loginFormulario', views.loginFormulario, name='loginFormulario'),
    #path('loginFormulario_vista', views.loginFormulario_vista, name='loginFormulario_vista'),
    #path('login', views.login, name='login'),
    path('panelCrud', views.panelCrud, name='panelcrud'),
    path('leer_usuarios', views.leerUsuarios, name='leer_usuarios'),
    path('eliminarusuarios/<usuario_nombre>', views.eliminarUsuarios, name='eliminarUsuarios'),
    path('editarusuarios/<usuario_nombre>', views.editarUsuarios, name='editarUsuarios'),
    path('login_profile', views.login_request, name='login_profile'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    #path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    ]