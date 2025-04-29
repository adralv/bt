from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def index(request):
<<<<<<< HEAD
    return render(request, 'index.html')

=======
    user = request.user
    context={
        'user':user
    }
    return render(request, 'index.html',context)
>>>>>>> f6cbd5a5e914eaa1f31c871c244477d5276ba78f
@login_required
def contact(request):
    return render(request, 'contact.html')
