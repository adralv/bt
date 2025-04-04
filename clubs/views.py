from django.shortcuts import render

# Create your views here.
def club_list(request):
    return render(request, 'club_list.html')