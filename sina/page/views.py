from django.shortcuts import render

# Create your views here.

def info_page(request):
    return render (request , "page/page.html")