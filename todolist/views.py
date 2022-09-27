import datetime 
from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms_task import CreateNewTask


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.all()
    todolist_user = []
    current_user = request.user

    for task in data_todolist:
        if task.user == current_user:
            todolist_user.append(task)

            if task.is_finished:
                task.status = 'Selesai'
            else:
                task.status = 'Belum Selesai'


    context = {
        'todolist_user' : todolist_user,
        'last_login': request.COOKIES['last_login'],
        'name' : current_user
    }
    return render(request, 'todolist.html', context)


@login_required(login_url='/todolist/login/')
def create_task(request):
    form = CreateNewTask(request.POST)
    if request.method == 'POST':
        form = CreateNewTask(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todolist:show_todolist')

    context = {'form' : form}
    return render(request, 'create_task.html', context)

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
            response.set_cookie('last_login', str(datetime.datetime.now().strftime(("%d.%m.%Y %H:%M:%S")))) # membuat cookie last_login dan menambahkannya ke dalam response
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

def delete_task(request, id):
    task = Task.objects.filter(user = request.user).get(pk = id)
    task.delete()
    return redirect('todolist:show_todolist')

def update_status(request, id):
    task = Task.objects.filter(user = request.user).get(pk = id)
    
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return redirect('todolist:show_todolist')