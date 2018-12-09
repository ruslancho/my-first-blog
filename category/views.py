from django.shortcuts import render
from django.http import HttpResponse

def category(request):
	return HttpResponse("<h3>This is category on My Site</h3>")
