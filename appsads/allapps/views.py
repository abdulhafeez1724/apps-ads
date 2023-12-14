from django.shortcuts import redirect, render
from .models import *
from .forms import AppsForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'admin/pages/dashboard.html')

@login_required
def index(request):
    if request.method == 'POST':
        form = AppsForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.added_by = request.user 
            app.save()
            placements = request.POST.get('placements')
            # print(placements)
            placements = placements.split(',')
            for placement in placements:
                # print(placement)
                data = Placement(
                    title=placement,
                    added_by=request.user,
                    app = app
                )
                data.save()
            return redirect('allapps')
        else:
            print(form.errors)
    else:
        form = AppsForm()
    all_apps = Apps.objects.all()
    return render(request, 'admin/pages/allapps/index.html', {'all_apps': all_apps,'form': form})

@login_required
def create(request):
    if request.method == 'POST':
        form = AppsForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.added_by = request.user 
            app.save()
            return redirect('allapps')
        else:
            print(form.errors)
    else:
        form = AppsForm()
    
    return render(request, 'admin/pages/allapps/index.html', {'form': form})

@login_required
def delete(request, id):
    apps = Apps.objects.get(id=id)
    apps.delete()
    return redirect('allapps')

@login_required
def update(request, id):
    apps = Apps.objects.get(id=id)
    if request.method == 'POST':
        form = AppsForm(request.POST, instance=apps)
        if form.is_valid():
            form.save()
            return redirect('allapps')
    else:
        form = AppsForm(instance=apps)
    return render(request, 'admin/pages/allapps/index.html', {'form': form, 'apps': apps})
