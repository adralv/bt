from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def index(request):
    user = request.user
    context={
        'user':user
    }
    return render(request, 'index.html',context)
@login_required
def contact(request):
    return render(request, 'contact.html')
