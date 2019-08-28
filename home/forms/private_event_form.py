from django import forms

class TestForm(forms.Form):

  name = forms.CharField(label='My test name', max_length=50)
  number = forms.IntegerField(label='Number')

  def save(self):
    print('saving form')
    print(self.cleaned_data)
    print('**********')

  