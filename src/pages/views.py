from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "base.html", {})

def prov_view(request, *args, **kwargs):
    context = {
        'my_text': "My text",
        'my_mun': 1234
    }
    return render(request, "province.html", context)
