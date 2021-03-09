from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms

class SignUpForm(UserCreationForm):
	password2=forms.CharField(label='Confirm Password (again)',
	widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		labels={'email':'Email',}
class EditUserProfileForm(UserCreationForm):
	password=None
	class Meta:
		model=User
		fields=['username','first_name','last_name','email','date_joined','last_login']
class EditAdminProfileForm(UserCreationForm):
	password=None
	class Meta:
		model=User
		fields='__all__'
class LoginForm(AuthenticationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))