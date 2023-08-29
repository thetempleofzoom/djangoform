from django import forms

class ContactForm(forms.Form):
    first = forms.CharField(max_length=80)
    last = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField(required = False)
    occupation = forms.CharField(max_length=80)