from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import * 
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
import json

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
    apps = Apps.objects.filter(added_by=request.user)
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
    return render(request, 'admin/pages/allapps/placement.html', {'form': form,'placements': placements, 'apps': apps})


@login_required
def get_placement(request):
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        app_instance = get_object_or_404(Apps, id=app_id)
        placements = Placement.objects.filter(app=app_instance)
        placement_list = [{'id': placement.id, 'title': placement.title, 'index': placement.index} for placement in placements]
        return JsonResponse({'placement': placement_list})

@login_required
@require_POST
def save_sorted_placement(request):
    sorted_placements_id = request.POST.get('sorted_placements')
    data = json.loads(sorted_placements_id)
    for index, sorted_placements_id in enumerate(data, start=1):
        placement = Placement.objects.get(id=sorted_placements_id)
        placement.index = index
        placement.save()
    return JsonResponse({'success': True})

@login_required
def delete_placement(request, id):
    placement = Placement.objects.get(id=id)
    placement.delete()
    return redirect('placement')
@login_required
def create_network(request, id=None):
    apps = Apps.objects.filter(added_by=request.user)
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
    return render(request, 'admin/pages/allapps/network.html', {'form': form,'networks': networks, 'apps': apps}) 


@login_required
def get_network(request):
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        app_instance = get_object_or_404(Apps, id=app_id)
        networks = AdNetwork.objects.filter(app=app_instance)
        network_list = [{'id': network.id, 'title': network.title, 'index': network.index} for network in networks]
        return JsonResponse({'network': network_list})

@login_required
@require_POST
def save_sorted_network(request):
    sorted_networks_id = request.POST.get('sorted_networks')
    
    if sorted_networks_id is not None:
        data = json.loads(sorted_networks_id)
        for index, sorted_network_id in enumerate(data, start=1):
            network = AdNetwork.objects.get(id=sorted_network_id)
            network.index = index
            network.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'sorted_networks not found in POST data'}, status=400)

@login_required
def delete_network(request, id):
    network = AdNetwork.objects.get(id=id)
    network.delete()
    return redirect('network')


@login_required
def create_source(request, id=None):
    print("Entering create_source view")

    apps = Apps.objects.filter(added_by=request.user)
    if id:
        print(f"Fetching source with id={id}")
        source = Source.objects.get(id=id)

    if request.method == 'POST':
        print("POST request received")
        if id:
            form = SourceForm(request.POST, request.FILES, instance=source)
        else:
            form = SourceForm(request.POST, request.FILES)

        if form.is_valid():
            print("Form is valid")
            source = form.save(commit=False)
            source.added_by = request.user
            source.save()
            return redirect('source')
        else:
            print("Form is not valid")
            print(form.errors)

    if id:
        print(f"Rendering form for editing source with id={id}")
        form = SourceForm(instance=Source.objects.get(id=id))
    else:
        print("Rendering empty form for creating a new source")
        form = SourceForm()

    sources = Source.objects.all()
    return render(request, 'admin/pages/allapps/priority_network.html', {'form': form, 'sources': sources, 'apps': apps})

@login_required
def get_source(request):
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        placement_id = request.POST.get('placement_id')
        sources = Source.objects.filter(app=app_id, placement=placement_id)
        source_list = [
            {'id': source.id, 'title': source.network.title, 'index': source.index}
            for source in sources
        ]
        return JsonResponse({'source': source_list})


@login_required
@require_POST
def save_sorted_source(request):
    sorted_sources_id = request.POST.get('sorted_sources')
    
    if sorted_sources_id is not None:
        data = json.loads(sorted_sources_id)
        for index, sorted_source_id in enumerate(data, start=1):
            source = Source.objects.get(id=sorted_source_id)
            source.index = index
            source.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'sorted_sources not found in POST data'}, status=400)

@login_required
def delete_source(request, id):
    source = Source.objects.get(id=id)
    source.delete()
    return redirect('source')

@login_required
def get_network_options(request):
    app_id = request.GET.get('app_id')
    networks = AdNetwork.objects.filter(app_id=app_id).values('id', 'title')
    placements = Placement.objects.filter(app_id=app_id).values('id', 'title')
    return JsonResponse({'networks': list(networks), 'placements': list(placements)}, safe=False)