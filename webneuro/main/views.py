from django.shortcuts import render
from django.http import HttpResponse, FileResponse

# Create your views here.


def index(request):
    return render(request, 'main/index.html', {'title': ''})

def about(request):
    return render(request, 'main/about.html')

def neuro(request):
    return render(request, 'main/neuro-interface.html')

def graphs(request):
    return render(request, 'main/graphs.html')

def view_pdf(request):
    return render(request, 'webneuro/main/static/main/img/file_test.pdf')


