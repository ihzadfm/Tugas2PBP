import datetime
from dataclasses import dataclass
from todolist.models import Task
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from todolist.forms import CreateNewTask
from django.core import serializers


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user = request.user)
    context = {
    'list_todolist': data_todolist,
    'nama': 'Ihza Dafa Maulidan',
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data_todolist = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_todolist), content_type="application/json")

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
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def create_task(request): ####    
    form = CreateNewTask(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response

    context = {'form': form}
    return render(request, 'create_task.html', context)

def delete(request, pk):
    data = Task.objects.get(id=pk)
    data.delete()
    response = HttpResponseRedirect(reverse("todolist:show_todolist"))
    return response

def toggle(request, pk):
    data = Task.objects.get(id=pk)
    if data.is_finished == True:
        data.is_finished = False
    else:
        data.is_finished = True
    data.save()
    response = HttpResponseRedirect(reverse("todolist:show_todolist"))
    return response

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response