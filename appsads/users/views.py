from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        # print('req here register')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def login(request):
    return render(request, 'login.html')
