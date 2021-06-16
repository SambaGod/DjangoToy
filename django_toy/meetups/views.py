from django.shortcuts import render
from .models import Meetup
from .forms import RegistrationForm
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    meetups = Meetup.objects.all() # Get all data from the Meetup object
    # path is taken directly from the templates folder
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups # This first meetups name here could be anything
    })

def meetup_details(request, meetup_slug):
    print('Slug:', meetup_slug)
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug) 
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.participants.add(participant)  
                 
        return render(request, 'meetups/meetup_details.html', {
        # 'meetup_title': selected_meetup['title'], # In case of static data
        'meetup_found': True,
        # 'meetup_title': selected_meetup.title,
        'meetup': selected_meetup,
        'form': registration_form
        })
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
            'meetup_found': False,
        })