from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

class AppsForm(forms.ModelForm):
    class Meta:
        model = Apps
        fields = ['name', 'icons', 'package', 'platform', 'links']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'icons': forms.FileInput(attrs={'class': 'form-select'}),
            'package': forms.TextInput(attrs={'class': 'form-control'}),
            'platform': forms.Select(attrs={'class': 'form-select'}),
            'links': forms.URLInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'name': _('Name'),
            'icons': _('Icons'),
            'package': _('Package'),
            'platform': _('Platform'),
            'links': _('Links'),
            'adnetwork': _('Ad Network'),
            'placements': _('Placements'),
        }

class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = ['title', 'added_by', 'app']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'added_by': forms.Select(attrs={'class': 'form-select'}),
            'app': forms.Select(attrs={'class': 'form-select'}),
        }

        labels = {
            'title': _('Title'),
            'added_by': _('Added By'),
            'app': _('App'),
        }


class NetworkForm(forms.ModelForm):
    class Meta:
        model = AdNetwork
        fields = ['title', 'added_by', 'app']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'added_by': forms.Select(attrs={'class': 'form-select'}),
            'app': forms.Select(attrs={'class': 'form-select'}),
        }

        labels = {
            'title': _('Title'),
            'added_by': _('Added By'),
            'app': _('App'),
        }

class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ['app', 'network', 'placement', 'data']

        widgets = {
            'app': forms.Select(attrs={'class': 'form-select'}),
            'network': forms.Select(attrs={'class': 'form-select'}),
            'placement': forms.Select(attrs={'class': 'form-select'}),
            'data': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'app': _('App'),
            'network': _('Network'),
            'placement': _('Placement'),
            'data': _('data'),
        }