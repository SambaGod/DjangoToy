from django.urls import path
from . import views
# urlpatterns needs to be named exactly this way so Django can find it
urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), # if our-domain/meetups is requested, fire index view
    path('meetups/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail' )
]
