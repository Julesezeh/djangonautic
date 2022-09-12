from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets
from ass1.models import Member


class Reg(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['balance']
        widgets = {
            'password': forms.PasswordInput(),
            
        }