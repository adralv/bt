from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Club
from Announcements.models import Announcements
# Create your views here.
@login_required
def club_list(request):
    clubs = Club.objects.all()
    paginator = Paginator(clubs,6)
    page = request.GET.get('page')
    paged_clubs = paginator.get_page(page)
    context = {
        'clubs' : paged_clubs
    }
    return render(request, 'club_list.html', context)
@login_required
def club_details(request,club_id):
    club= Club.objects.get(id=club_id)
    announcements=Announcements.objects.filter(club_id=club.id)
    context={
        'club':club,
        'announcements':announcements
    }
    return render(request, 'club_detail.html',context)
