from django.urls import path
from . import views
# urlpatterns needs to be named exactly this way so Django can find it
urlpatterns = [
    path('', views.index, name='all-meetups'), # if our-domain/meetups is requested, fire index view
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail' )
]
