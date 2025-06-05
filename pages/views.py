from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from clubs.models import Club
from users.models import UserProfile
from event.models import Event
from django.utils.timezone import now

# Create your views here.
@login_required
def index(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
        clubs = Club.objects.filter(club_members=user)
        events = Event.objects.all()
        valid_events = [
            event for event in events
            if (event.public_event or event.club in clubs) and event.end >= now()
        ]
    except UserProfile.DoesNotExist:
        user_profile = None  
        clubs = Club.objects.none()  # No clubs
        valid_events = Event.objects.filter(public_event=True, end__gte=now())  # Only public future events

    context = {
        'user': user,
        'clubs': clubs,
        'user_profile': user_profile,
        'events': valid_events,
    }
    
    return render(request, 'index.html', context)


@login_required
def contact(request):
    return render(request, 'contact.html')
