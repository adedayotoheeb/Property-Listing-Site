from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm, AuthenticationForm
from django.core import validators
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .options import STATUS


class CreateUserForm(UserCreationForm):
    botcatcher = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'botcatcher']

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("Please Fill The Form Manually")
        return botcatcher
        

class PropertyForm(forms.ModelForm):

    street_name = forms.CharField(label="Street Name", widget=forms.TextInput(attrs={'placeholder':'Enter the name of the Street'}))
    city = forms.CharField( label="City", widget=forms.TextInput(attrs={'placeholder':'Enter City Name'}))
    bedroom = forms.IntegerField(label='Bedroom',initial= 1, widget= forms.NumberInput(),validators=[validators.MinValueValidator(1)])
    garage = forms.IntegerField(label='Garage', initial= 1, widget= forms.NumberInput(),validators=[validators.MinValueValidator(1)])
    bathroom = forms.IntegerField(label='Bathroom', initial= 1, widget= forms.NumberInput(),validators=[validators.MinValueValidator(1)])
    property_status = forms.ChoiceField(widget=forms.Select(),choices=STATUS)
    property_size = forms.IntegerField(label="Property Size",validators=[validators.MinValueValidator(1)])
    cat = forms.ModelMultipleChoiceField(label= "Property Category",  queryset=Category.objects.all(), widget=forms.Select())
    prop_pic = forms.ImageField(label= "Property Picture")
    botcatcher = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    

    class Meta:
        model = Property
        fields = ('street_name', 'city', 'bedroom', 'garage', 'bathroom', 'prop_pic', 'cat','property_status','property_size', 'botcatcher')


class UserProfileForm(forms.ModelForm):
    profile_picture= forms.ImageField()
    title = forms.ChoiceField(choices=tit, widget= forms.Select())
    description = forms.Textarea()
    class Meta:
        model = UserProfile
        fields='__all__'
        exclude =['user']

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old Password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

class PasswordReset(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Email'}))


class SetPassword(SetPasswordForm):
    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'New Password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':'Confirm Password'}))