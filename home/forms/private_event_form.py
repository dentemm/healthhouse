from django import forms

from ..models.helpers.events import EventVisitor

class EventVisitorForm(forms.ModelForm):
    
    class Meta:
        model = EventVisitor
        fields = ['first_name', 'last_name', 'company', 'email']
