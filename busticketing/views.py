from django.shortcuts import render, render_to_response, redirect
from django.shortcuts import render
from django.db import models
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import Login
from django.template import RequestContext
def index(request): 
		# request.session['pagename'] = 'home'
		# return render_to_response(request.session['pagename'] + '.html', {}, RequestContext(request))
		return render(request, "home.html", {})
# Create your views here.
class LoginView(View):

	login_page_template = "500.html" 
	form_class = Login
	
	def get(self, request, **kwargs):
		if request.user.is_authenticated():
			return redirect("admin", request.user.id)
		print(request)
		return render(request, self.login_page_template, {'form': self.form_class})
		
	def post(self, request, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		
		authenticated_user = authenticate(username=username, password=password)
		
		if not authenticated_user:
			messages.error(request, "Username and Password mismatch")
			return render(request, self.login_page_template, {'form': self.form_class})
			
		login(request, authenticated_user)