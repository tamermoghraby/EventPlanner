from multiprocessing import context
from django.forms import SlugField
from django.shortcuts import render

from EventPlanner.models import Event

# Create your views here.
def home(request):
    events = Event.objects.all()
    context = { 'events':events }
    return render(request, 'eventhome.html', context)

def eventpost(request, slug):
    event = Event.objects.filter(slug=slug).first()
    context = {'event':event}
    return render(request, 'eventpost.html', context)