from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def users(request):
    return render(request,'users.html')