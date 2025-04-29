from django.urls import path
from . import views

urlpatterns = [
    path('',views.club_list, name='club_list'),
<<<<<<< HEAD
    path('club', views.club_details, name='club_details'),
    path('<int:club_id>', views.club_details, name='club_details')
]
=======
    path('<int:club_id>', views.club_details, name='club_details')
    ]
>>>>>>> f6cbd5a5e914eaa1f31c871c244477d5276ba78f
