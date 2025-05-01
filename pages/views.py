from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from clubs.models import Club
from users.models import UserProfile
# Create your views here.
@login_required
def index(request):
    user = request.user
    clubs = Club.objects.all()
    
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None  
    
    context = {
        'user': user,
        'clubs': clubs,
        'user_profile': user_profile
    }
    return render(request, 'index.html', context)

@login_required
def contact(request):
    return render(request, 'contact.html')
