from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import *
from .forms import AppsForm, PlacementForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
            adnetwork = request.POST.get('adnetwork')
            # print(adnetwork)
            adnetwork = adnetwork.split(',')
            for network in adnetwork:
                #print(network)
                data = AdNetwork(
                    title=network,
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
def create_apps(request):
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
def update_apps(request, id):
    apps = Apps.objects.get(id=id)
    if request.method == 'POST':
        form = AppsForm(request.POST, instance=apps)
        if form.is_valid():
            form.save()
            return redirect('allapps')
    else:
        form = AppsForm(instance=apps)
    return render(request, 'admin/pages/allapps/index.html', {'form': form, 'apps': apps})

@login_required
def delete_apps(request, id):
    apps = Apps.objects.get(id=id)
    apps.delete()
    return redirect('allapps')


@login_required 
def placement(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        form = PlacementForm(request.POST)
        if form.is_valid():
            print("Placement data added successfully!")
            placement = form.save(commit=False)
            placement.added_by = request.user 
            placement.save()
            return redirect('placement')
        else:
            print("Form errors:", form.errors)
    else:
        form = PlacementForm()

    placements = Placement.objects.all()
    return render(request, 'admin/pages/allapps/placement.html', {'form': form,'placements': placements})

@login_required
def update_placement(request, id):
    placement = Placement.objects.get(id=id)
    if request.method == 'POST':
        form = PlacementForm(request.POST, instance=placement)
        if form.is_valid():
            form.save()
            return redirect('placement')
    else:
        form = PlacementForm(instance=placement)
    
    return render(request, 'admin/pages/allapps/placement.html', {'form': form, 'placement': placement})

def delete_placement(request, id):
    placement = Placement.objects.get(id=id)
    placement.delete()
    return redirect('placement')
 

def AdNetwork(request):
    pass
    return HttpResponse('AdNetwork')