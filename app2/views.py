from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def vinod(request):
    return HttpResponse('<marquee>this is our second fbv</marquee>')
def ravi(request):
    return HttpResponse('<marquee>this is our third fbv</marquee>')