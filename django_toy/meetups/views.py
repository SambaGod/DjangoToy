from django.shortcuts import render, redirect
from .models import Meetup, Participant
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
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug) 
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                # participant = registration_form.save() # Does not allow repition of email on other events either
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email) # If exists get, else create
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

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

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration_success.html', {
        'organizer_email': meetup.organizer_email
    })