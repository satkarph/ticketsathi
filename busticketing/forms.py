from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models  
from django.forms import extras
class RegistrationForm(forms.Form):
	ROLE = (
		('User', 'User')
	) 
	role =  forms.ChoiceField(label="Type", required=True,choices=ROLE)
	username = forms.CharField(label="Username", required=True, max_length=30)
	email = forms.EmailField()
	password1 = forms.CharField(label="Password", required=True, max_length=30, widget=forms.PasswordInput)
	password2 = forms.CharField(label="Re-Password", required=True, max_length=30, widget=forms.PasswordInput)
	
 	

	def clean_password2(self):
		password1 = self.cleaned_data['password1']
		password2  = self.cleaned_data['password2']
		
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Your password didn't match")
			
		return password2
		

class Login(forms.Form):
	username = forms.CharField(label="Username", required=True,max_length=30)
	password = forms.CharField(label="Your password",  required=True,max_length=30, widget=forms.PasswordInput)
 