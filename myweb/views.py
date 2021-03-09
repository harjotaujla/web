from django.shortcuts import render,loader
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.conf import settings


def index(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			if request.user.is_superuser==True:
				fm=EditAdminProfileForm(request.POST,instance=request.user)
				users=User.objects.all()
			else:
				fm=EditUserProfileForm(request.POST,instance=request.user)
				users=None
			if fm.is_valid():
				fm.save()
		else:
			if request.user.is_superuser==True:
				fm=EditAdminProfileForm(instance=request.user)
				users=User.objects.all()
			else:
				fm=EditUserProfileForm(instance=request.user)
				users=None
		return render(request,'index.html',{'name':request.user,'form':fm,'users':users})
	else:
		return HttpResponseRedirect('/logi/')



def contact(request):
	if request.user.is_authenticated:
		return render(request,'contact.html',{'name':request.user})
	else:
		return HttpResponseRedirect('/logi/')


def about(request):
	if request.user.is_authenticated:
		return render(request,'about.html',{'name':request.user})
	else:
		return HttpResponseRedirect('/logi/')


def blog(request):
	if request.user.is_authenticated:
		return render(request,'blog.html',{'name':request.user})
	else:
		return HttpResponseRedirect('/logi/')

def recipe(request):
	if request.user.is_authenticated:
		return render(request,'recipe.html',{'name':request.user})
	else:
		return HttpResponseRedirect('/logi/')


def register(request):
	if request.method=='POST':
		fm=SignUpForm(request.POST)
		if fm.is_valid():
			#messages.success(request,"User successfully created Welcome")#
			fm.save()
			return HttpResponseRedirect('/register/')
	else:
		fm=SignUpForm()
	return render(request,'register.html',{'form':fm,'name':request.user})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/logi/')

def cpass(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			fm=PasswordChangeForm(user=request.user,data=request.POST)
			if fm.is_valid():
				fm.save()
				update_session_auth_hash(request,fm.user)
				return HttpResponseRedirect('/index/')
		else:

			fm=PasswordChangeForm(user=request.user)
			return render(request,'cpass.html',{'form':fm})
	else:
		return HttpResponseRedirect('/login/')

def c(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			fm=SetPasswordForm(user=request.user,data=request.POST)
			if fm.is_valid():
				fm.save()
				update_session_auth_hash(request,fm.user)
				return HttpResponseRedirect('/index/')
		else:

			fm=SetPasswordForm(user=request.user)
			return render(request,'c.html',{'form':fm,'name':request.user})
	else:
		return HttpResponseRedirect('/logi/')


def logi(request):
	if not request.user.is_authenticated:
		if request.method=='POST':
			fm=AuthenticationForm(request=request,data=request.POST)
			if fm.is_valid():
				uname=fm.cleaned_data['username']
				upass=fm.cleaned_data['password']
				user=authenticate(username=uname,password=upass)
				if user is not None:
					login(request,user)
					return HttpResponseRedirect('/index/')
		else:
			fm=AuthenticationForm()
	else:
		return HttpResponseRedirect('/index/')
	return render(request,'logi.html',{'form':fm})
def userdetail(request,id):
	if request.user.is_authenticated:
		pi=User.objects.get(pk=id)
		fm=EditAdminProfileForm(instance=pi)
		return render(request,'userdetail.html',{'form':fm,'name':request.user})
	else:
		return HttpResponseRedirect('/logi')
def emaill(request):
	if request.method=='POST':
		to=request.POST.get('Email')
		con=request.POST.get('Message')
		sub=request.POST.get('Name')
		send_mail(sub,con,settings.EMAIL_HOST_USER,[to])
		return HttpResponseRedirect('/index/')
	else:
		return HttpResponseRedirect('/index/')


def profile(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			if request.user.is_superuser==True:
				fm=EditAdminProfileForm(request.POST,instance=request.user)
				users=User.objects.all()
			else:
				fm=EditUserProfileForm(request.POST,instance=request.user)
				users=None
			if fm.is_valid():
				fm.save()
		else:
			if request.user.is_superuser==True:
				fm=EditAdminProfileForm(instance=request.user)
				users=User.objects.all()
			else:
				fm=EditUserProfileForm(instance=request.user)
				users=None
		return render(request,'profile.html',{'name':request.user,'form':fm,'users':users,'name':request.user})
	else:
		return HttpResponseRedirect('/logi/')




# Create your views here.
