from django.shortcuts import render

# Create your views here.

def info_page1(request):
    return render(request , "page1/page1.html")