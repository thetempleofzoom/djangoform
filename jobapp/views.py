from django.shortcuts import render

# request automatically runs index function when website is opened
def index(request):
    return render(request, "index.html")
