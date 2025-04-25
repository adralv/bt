from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def club_list(request):
    return render(request, 'club_list.html')
@login_required
def club_details(request):
    return render(request, 'club_detail.html')