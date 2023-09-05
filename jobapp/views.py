from django.shortcuts import render
from .forms import ContactForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

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

            # red is database column name, white are variables above
            # links database to input data
            Form.objects.create(first=first, last=last, email=email,
                                 date=date, occupation=occupation)

            #send email
            body = f'''a new job application was submitted for {first} {last} 
            with status {occupation}. '''
            email_msg = EmailMessage("form submitted", body, to=[email])
            #email_msg.send()


            # show message
            #messages.success(request, "info successfully input")
        else:
            print(form.errors)
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")