from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import *
from .forms import AppsForm, PlacementForm, NetworkForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'admin/pages/dashboard.html')

@login_required
def apps(request, id=None):
    if id:
        app = Apps.objects.get(id=id)
    if request.method == 'POST':
        if id:
            form = AppsForm(request.POST, request.FILES, instance=app)
        else:
            form = AppsForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.added_by = request.user 
            app.save()
            placements = request.POST.get('placements')
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
    elif id:
        form = AppsForm(instance=Apps.objects.get(id=id))
    else:
        form = AppsForm()
    all_apps = Apps.objects.all()
    return render(request, 'admin/pages/allapps/index.html', {'form': form,'all_apps': all_apps})

@login_required
def delete_apps(request, id):
    apps = Apps.objects.get(id=id)
    apps.delete()
    return redirect('allapps')

@login_required 
def create_placement(request, id=None):
    if id:
        placement = Placement.objects.get(id=id)
    if request.method == 'POST':
        if id:
            form = PlacementForm(request.POST, request.FILES, instance=placement)
        else:
            form = PlacementForm(request.POST, request.FILES)
            
        if form.is_valid():
            placement = form.save(commit=False)
            placement.added_by = request.user 
            placement.save()
            return redirect('placement')
    elif id:
        form = PlacementForm(instance=Placement.objects.get(id=id))
    else:
        form = PlacementForm()
    placements = Placement.objects.all()
    return render(request, 'admin/pages/allapps/placement.html', {'form': form,'placements': placements})

def delete_placement(request, id):
    placement = Placement.objects.get(id=id)
    placement.delete()
    return redirect('placement')

def create_network(request, id=None):
    if id:
        network = AdNetwork.objects.get(id=id)
    if request.method == 'POST':
        if id:
            form = NetworkForm(request.POST, request.FILES, instance=network)
        else:
            form  = NetworkForm(request.POST, request.FILES)

        if form.is_valid(): 
            network = form.save(commit=False) 
            network.added_by = request.user  
            network.save()
            return redirect('network') 
    elif id:
        form = NetworkForm(instance=AdNetwork.objects.get(id=id))
    else: 
        form = NetworkForm() 
    networks = AdNetwork.objects.all()
    return render(request, 'admin/pages/allapps/network.html', {'form': form,'networks': networks}) 
    
def delete_network(request, id):
    network = AdNetwork.objects.get(id=id)
    network.delete()
    return redirect('network')