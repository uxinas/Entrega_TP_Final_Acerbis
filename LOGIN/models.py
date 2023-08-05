from django.db import models
from django.contrib.auth.models import User

class Login(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

"""
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario=AvatarFormulario()
        
    return render(request, "AppCoder/agregarAvatar.html", {'miFormulario': miFormulario})
    """