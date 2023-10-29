from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.http import HttpResponse

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)
        if user:
            login_django(request, user)
            return redirect('list_all_clients')
        else:
            return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos'})
           

def logout(request):
    logout_django(request)
    return render(request, 'login.html')