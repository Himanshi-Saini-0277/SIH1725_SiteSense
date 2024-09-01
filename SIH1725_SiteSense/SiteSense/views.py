from django.shortcuts import render

# Create your views here.
def entrance(request):
    return render(request, 'entrance.html')

def errorCheckpoint(request):
    return render(request, 'errorCheckpoint.html')

def home(request):
    return render(request, 'home.html')

def imagehub(request):
    return render(request, 'imagehub.html')

def login(request):
    return render(request, 'login.html')

def progress(request):
    return render(request, 'progress.html')

def register(request):
    return render(request, 'register.html')

def stageInsight(request):
    return render(request, 'stageInsight.html')