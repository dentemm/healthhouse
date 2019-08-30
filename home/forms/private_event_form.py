from django import forms

from ..models.helpers.events import EventVisitor

class TestForm(forms.Form):

    name = forms.CharField(label='My test name', max_length=50)
    number = forms.IntegerField(label='Number')

    def save(self):
        print('saving form')
        print(self.cleaned_data)
        print('**********')

class EventVisitorForm(forms.ModelForm):
    
    class Meta:
        model = EventVisitor
        fields = '__all__'

    def save(self):
        print('saving form')
        print(self.cleaned_data)
        print('**********')
