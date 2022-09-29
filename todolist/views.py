import datetime
from unicodedata import name
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from todolist.models import Task
from todolist.forms import CreateTask


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.all()
    pengguna = request.user
    context = {
    'data_todolist': data_todolist,
    'nama': 'Rikza Kurnia',
    'npm' : '2106701293',
    'pengguna' : pengguna,
    }
    return render(request, "todolist.html", context)

#function untuk form
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


def create_task(request):
    form = CreateTask()

    if request.method == "POST":
        form = CreateTask(request.POST)
        if form.is_valid():
            pengguna = request.user
            judul = request.POST.get("judul")
            deskripsi = request.POST.get("deskripsi")
            new_task = Task(pengguna=pengguna, judul=judul, deskripsi=deskripsi)
            new_task.save()
            return redirect('todolist:show_todolist')

    context = {'form':form}
    return render(request, 'create_task.html', context)


def change_status(request, id):
    task = Task.objects.get(id=id)
    task.status = not task.status
    task.save()
    return redirect('todolist:show_todolist')

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist')