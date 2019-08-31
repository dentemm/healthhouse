from django import forms

from ..models.helpers.events import EventVisitor

class EventVisitorForm(forms.ModelForm):
    
    class Meta:
        model = EventVisitor
        fields = ['first_name', 'last_name', 'company', 'brings_guest', 'email']

    # def save(self, commit=True):
    #     print('saving form')
    #     print(self.cleaned_data)
    #     print('**********')

    #     # TODO

    #     super(EventVisitorForm, self).save(commit=commit)
