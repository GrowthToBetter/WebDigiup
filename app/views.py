from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Fasilitas, Kamar
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import UserSession

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'home/index.html')
def fasilitas(request):
    feat= Fasilitas.objects.all()
    kamar= Kamar.objects.all()
    context={'feats': feat, 'rooms': kamar}
    return render(request, 'fasilitas/index.html', context=context)



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user, created = User.objects.get_or_create(username=username)
            if created:
                # Buat pengguna baru dengan password
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect('/')
            else:
                # Autentikasi pengguna
                user = authenticate(request, username=username, password=password)
                if not user:
                    # Jika password salah, kembalikan pesan error
                    return render(request, 'login.html', {'error': 'Password salah!'})
                login(request, user)
                return redirect('/')  # Redirect ke halaman profil
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)  # Hapus sesi pengguna
    return redirect('login')  # Redirect ke halaman login
