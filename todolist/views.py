import datetime
from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    current_user = request.user
    data_todolist = Task.objects.filter(user = current_user)

    for task in data_todolist:
        if task.user == current_user:

            if task.is_finished:
                task.status = 'Selesai'
            else:
                task.status = 'Belum Selesai'


    context = {
        'data_todolist' : data_todolist,
        'last_login': request.COOKIES['last_login'],
        'name' : current_user
    }
    return render(request, 'todolist.html', context)


@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        task_title = request.POST['task_title']
        description = request.POST['description']

        valid = False
        if isinstance(task_title, str) and isinstance(description, str):
            if len(task_title.strip()) == len(description.strip()) != 0:
                task = Task(title=task_title, description=description)
                task.user = request.user
                task.save()
                valid = True
                return redirect('todolist:show_todolist')
        
        if not valid:
            messages.info(request, 'Please fill both fields with letter(s) or number(s)!')
    return render(request, 'create_task.html')


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
            response.set_cookie('last_login', str(datetime.datetime.now().strftime(("%d/%m/%Y %H:%M:%S")))) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
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