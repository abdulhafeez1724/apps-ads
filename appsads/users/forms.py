from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label=_('Username'), max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
    class Meta:
        model = NewUser
        fields = ['name', 'username', 'email', 'platform']