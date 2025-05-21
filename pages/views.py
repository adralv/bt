from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from clubs.models import Club
from users.models import UserProfile
from event.models import Event
# Create your views here.
@login_required
def index(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
        clubs = Club.objects.filter(club_members=user)
        events = Event.objects.all()
    except UserProfile.DoesNotExist:
        user_profile = None  
    
    context = {
        'user': user,
        'clubs': clubs,
        'user_profile': user_profile,
        'events': events,
        # 'length': len(events)
    }
    
    return render(request, 'index.html', context)

@login_required
def contact(request):
    return render(request, 'contact.html')
