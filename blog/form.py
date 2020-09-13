from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        labels = {
            'body':'leave a comment'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'cols': 10}),
        }
        help_texts = {
            'body': _('extend the text widget for more input'),
        }