from django.shortcuts import render, redirect
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.forms import TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_data = Task.objects.filter(user = request.user)
    context = {
        'data' : task_data,
        'nama' : 'Nikolas Reva Bellie',
        'npm' : '2106750212'
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
           
        return redirect('todolist:show_todolist')
    context = {}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def change_status(request, pk):
    if(Task.objects.get(pk = pk).is_finished == True and Task.objects.get(pk=pk).user == request.user):
        Task.objects.filter(pk = pk).update(is_finished = False)
    else:
        if(Task.objects.get(pk = pk).user == request.user):
            Task.objects.filter(pk = pk).update(is_finished = True)
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, pk):
    if(Task.objects.get(pk = pk).user == request.user):
        Task.objects.filter(pk = pk).delete()
    return redirect('todolist:show_todolist')

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
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response