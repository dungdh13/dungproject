from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserLoginForm
from .forms import TodoForm
from .models import Todo, Router
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def login_user(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {'form':UserLoginForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.success(request, f'Tên đăng nhập hoặc mật khẩu không không đúng!')
            return render(request, 'users/login.html', {'form':UserLoginForm()})
        else:
            login(request, user)
            return redirect('currenttodos')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_active = False
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Đây là website khai báo cho nhân viên y tế bệnh viện K, nếu bạn là nhân viên bệnh viện hãy gọi điện lên phòng CNTT để xác thực. Nếu bạn là người bệnh và người nhà người bệnh xin mời khai báo tại địa chỉ www.khaibaoyte-bvk.com. Trân trọng cảm ơn')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Cập nhật thông tin thành công!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def sk(request):
    if request.method == 'GET':
        return render(request, 'users/sk.html', {'form':TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'users/sk.html', {'form':TodoForm(), 'error':'Bad data passed in. Try again.'})


@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user).order_by('-id')
    todo_last = Todo.objects.filter(user=request.user).last()
    context = {
        'todos':todos,
        'todo_last':todo_last
    }
    return render(request, 'users/currenttodos.html', context)


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'users/viewtodo.html', {'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'users/viewtodo.html', {'todo':todo, 'form':form, 'error':'Bad ifo'})


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')


@login_required
def download(request):
    dl= Router.objects.all().order_by('-id')
    context={
        'dl':dl
    }
    return render(request, 'users/dl.html',context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })