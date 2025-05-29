from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Club
from Announcements.models import Announcements
from django.contrib.auth.models import User
from event.models import Event
# Create your views here.
@login_required
def club_list(request):
    clubs = Club.objects.all()
    paginator = Paginator(clubs,8)
    page = request.GET.get('page')
    paged_clubs = paginator.get_page(page)
    context = {
        'clubs' : paged_clubs
    }
    return render(request, 'club_list.html', context)
@login_required
def club_details(request,club_id):
    club= Club.objects.get(id=club_id)
    events= Event.objects.filter(club_id=club_id)
    announcements=Announcements.objects.filter(club=club)
    context={
        'club':club,
        'announcements':announcements,
        'events':events
    }
    return render(request, 'club_detail.html',context)

@login_required
def join_club(request, club_id):
    club= Club.objects.get(id=club_id)
    club.club_members.add(request.user)
    return redirect('club_details',club_id=club_id)
@login_required
def leave_club(request, club_id):
    club= Club.objects.get(id=club_id)
    club.club_members.remove(request.user)
    return redirect('club_details',club_id=club_id)
