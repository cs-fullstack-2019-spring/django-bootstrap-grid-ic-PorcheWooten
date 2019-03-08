from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignInForm, SignInModel, SignUpForm, SignUpModel

# Create your views here.
def index(request):
    form = SignInForm(request.POST or None)
    return render(request, 'BootstrapApp/index.html', {"form": form})

def signup(request):
    newform = SignUpForm(request.POST or None)
    return render(request, 'BootstrapApp/signup.html', {"newform": newform})