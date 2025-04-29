from django.urls import path
from . import views

urlpatterns = [
    path('',views.club_list, name='club_list'),
    path('club', views.club_details, name='club_details'),
    path('<int:club_id>', views.club_details, name='club_details')
]
