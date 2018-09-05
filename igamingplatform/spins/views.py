from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from spins.models import User, Wallet

def index(request):
    return HttpResponse("Index page.")

def signup(request):
	form_fields = ["Username", "Password"]
	template = loader.get_template("spins/signup.html")
	context = {
		"form_fields" : form_fields,
	}	
	return HttpResponse(template.render(context, request))
	
def register(request):
	pass#user = User(username