from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Venda, Curso
from .forms import VendaForm, CursoForm , CreateUserForm
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate , login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('cliente:login')

    context = {'form': form}
    return render (request, 'cliente/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username , password=password)
        
        if user is not None:
            login(request, user)
            return redirect('cliente:home')
        else:
            messages.info(request, 'Username or passoword is incorrect')
            
    context = {}
    return render (request, 'cliente/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect ('login')

@login_required(login_url='login')
def home(request):
    cursos = Curso.objects.all()  
    vendas = Venda.objects.all() 
    user = request.user #adicionado
    return render(request, "cliente/home.html", {'cursos': cursos, 'vendas': vendas})


def welcome(request):
    return render(request, "welcome.html", {'nome': 'Erica'})


def add(request, id):

    #curso1 = Curso.objects.get(pk=id)
    #curso1.sold = True
    formulario = VendaForm()
    if request.method=="POST":
        formulario = VendaForm(request.POST, request.FILES)
        formulario.save()
        return redirect ("cliente:home")
    return render(request, "cliente/add.html", {'formulario':formulario} )


def informacao(request, id):
    curso = Curso.objects.get(pk=id)
    return render(request, "cliente/informacao.html", {'curso': curso})

#novo
def pesquisar_cursos(request):
    query = request.GET.get('q')
    cursos = Curso.objects.filter(titulo__icontains=query) if query else Curso.objects.all()
    return render(request, 'cliente/home.html', {'cursos': cursos})