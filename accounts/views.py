
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(request, 'login.html', {
            'error': 'Incorrect username or password.'
        })

    return render(request, 'login.html')

@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'dashboard.html')

def signout(request):
    logout(request)
    return redirect('signin')