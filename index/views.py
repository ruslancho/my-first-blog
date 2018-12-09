from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h3>This is start page on My Site</h3>")


def about(request):
	return HttpResponse("<h3>This is about page</h3>")


def contacts(request):
	return HttpResponse("<h3>This is contacts page</h3>")