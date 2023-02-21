from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import UserForm

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





def data_in(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = UserForm()
        return render(request, "model.html", {"form": userform})


