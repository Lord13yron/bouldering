from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from guide.models import Profile

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('index')
        
        else:
        # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging in, Try again..."))
            return redirect('login_user')

    else:
        return render(request, 'authenticate/login_user.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("Succcesfully logged out"))
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            p = Profile(user=user)
            p.save()
            login(request, user)
            messages.success(request, ('Registration successfull'))
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })

# Create your views here.
