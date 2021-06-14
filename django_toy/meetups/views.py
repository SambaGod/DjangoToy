from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    meetups = [
            {
                'title': 'A first meetup',
                'location': 'New York',
                'slug': 'a-first-meetup'
                },
            {
                'title': 'A second meetup',
                'location': 'Paris',
                'slug': 'a-second-meetup'
                }
    ]
    # path is taken directly from the templates folder
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups # This first meetups name here could be anything
    })

def meetup_details(request, meetup_slug):
    print('Slug:', meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup!'
    }
    return render(request, 'meetups/meetup_details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
    })