import random
from datetime import datetime, timedelta
from django.http import HttpResponse  # Import HttpResponse class
from django.shortcuts import render

def members(request):
    return HttpResponse("<h1>Hello World</h1><br/><a href='https://devmap.ir'>devmap.ir</a>")

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Perform any necessary processing or data storage

        # Return a success message or redirect to a thank you page
        return render(request, 'thank_you.html')

    # If it's a GET request or the form submission is invalid, render the contact form
    return render(request, 'contact.html')

def events(request):
    events = [
        {
            'title': 'Conference',
            'description': 'Join us for an insightful conference on the latest industry trends.',
            'image': 'https://example.com/conference.jpg',
        },
        # Add other events here as dictionaries with 'title', 'description', and 'image' keys.
        # Example:
        # {
        #     'title': 'Art Exhibition',
        #     'description': 'Immerse yourself in the world of art at our Art Exhibition Event.',
        #     'image': 'https://example.com/art_exhibition.jpg',
        # },
    ]

    context = {'events': events}
    return render(request, 'events.html', context)

# Workshop, Concert, Art Exhibition, Charity Gala, and Sports Tournament views have been removed.

# Only the events and necessary views are left in the views.py file.
