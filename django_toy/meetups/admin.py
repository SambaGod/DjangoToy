from django.contrib import admin
from .models import Meetup, Location, Participant
# Register your models here.
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug') # Display fields as columns in admin area
    list_filter = ('location',) # Ability to filter through data (The comma needs to be there!)
    prepopulated_fields = {'slug':('title',)} # Auto generate slug
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)