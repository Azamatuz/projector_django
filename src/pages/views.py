from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "search.html", {})

def content_view(request, *args, **kwargs):
    return render(request, "content.html", {})
