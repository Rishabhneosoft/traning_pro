from django.forms import ModelForm
from .models import User
from django import forms
from django.forms import CharField, Form, PasswordInput

class RegisterForm(forms.ModelForm):
    # fullname = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # password = forms.CharField(widget=PasswordInput)
    # mobile = forms.CharField()
    # address = forms.CharField()
    username= forms.CharField(max_length=100,widget= forms.TextInput
                           (attrs={'class':'input--style-3','placeholder':"Username"}))
    class Meta:
        model = User
        fields = ["fullname","username","email", "password","mobile","address",]
        exclude = ["DOB","gender","field_type","User_type","assigned_client"]

# fullname = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
#     DOB = models.DateField(auto_now=False, auto_now_add=False)
#     gender = models.CharField(choices=STATE_CHOICE1, max_length=50)
#     password = models.CharField(max_length=50)
#     mobile = models.CharField(max_length=25, null=True, blank=True)
#     address = models.CharField(max_length=250, null=True, blank=True)
#     field_type = models.CharField(choices=STATE_CHOICE, max_length=50)
#     User_type = models.CharField(choices=STATE_CHOICE2, max_length=50)
#     assigned_client = models.CharField(max_length=100)