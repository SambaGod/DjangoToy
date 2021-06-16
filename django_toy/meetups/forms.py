from django import forms
# from .models import Participant 

# class RegistrationForm(forms.ModelForm): # Simple form that can be used with save() method
    
#     class Meta:
#         model = Participant
#         fields = ('email',)

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')