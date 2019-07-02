from django import forms
from django.contrib.auth.models import User
from .models import Termin

class CreatTermin(forms.ModelForm):

    class Meta:
        model = Termin
        fields = ['status', 'price', 'date', 'mobile_number']