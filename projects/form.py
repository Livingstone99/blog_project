from django import forms
from .models import FeedBack

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = [
            'name', 'email', 'message',
        ]
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 5, 'cols': 15}),
        }
       # you can customize django form with bootstrap, or any available static file, call the class used in you html right here
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Your name...'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Your email...'}),
        #     'message': forms.Textarea(attrs={'class': 'form-control','rows': 4, 'placeholder':'Your message...'}),
        # }