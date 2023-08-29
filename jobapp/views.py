from django.shortcuts import render
from .forms import ContactForm
import datetime

# request automatically runs index function when website is opened
def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # names correspond to index names
            first = form.cleaned_data['first']
            last = form.cleaned_data['last']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            print(first)
        else:
            print(form.errors)
    return render(request, "index.html")
