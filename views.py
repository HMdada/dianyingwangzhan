from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template.response import TemplateResponse
from .models import Text


def home(request):
	a=Text.objects.get(id=1)
	d={"a":a}
	return render_to_response('index.html',d)
def index1(request):
	return render_to_response('index1.html')