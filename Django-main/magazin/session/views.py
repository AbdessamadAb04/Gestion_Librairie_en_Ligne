from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from operator import itemgetter
from .models import Utilisateur
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logouts
from django.contrib import messages

# Create your views here.

 

from django.contrib.auth.decorators import login_required

def conx(request):
    
    if request.method == 'POST':
        email = request.POST.get('mail')
        password = request.POST.get('psswd')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = email
            return redirect('/product/home')
        else:
            messages.error(request, "Bad credentials")
            return render(request, "session.html")

    return render(request, "session.html")

@login_required(login_url='/session/')
def some_protected_view(request):
    # Example protected view to demonstrate login required
    return render(request, "some_protected_page.html")

from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("mail")
        cin = request.POST.get("cin")
        password = request.POST.get("psswd")
        if not all([name, email, cin, password]):
            # Handle missing fields gracefully
            return render(request, "registration.html", {"error": "Please fill in all fields."})
        if User.objects.filter(username=email).exists():
            return render(request, "registration.html", {"error": "User already exists."})
        user = User.objects.create_user(username=email, password=password, first_name=name)
        # Save additional info like cin if needed in a profile model
        user.save()
        return redirect('connexion')
    return render(request, "registration.html")

def logout(request):
    logouts(request)
    if 'username' in request.session:
        del request.session['username']
    return redirect('connexion')
