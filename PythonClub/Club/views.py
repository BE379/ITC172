from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def resources (request):
    resource_list=Resource.objects.all()
    return render(request, 'Club/resources.html', {'resource_list': resource_list})

def getmeetings (request):
    meetings_list=Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meetings_list': meetings_list})

def meetingminutes (request, id):
    minutes=get_object_or_404(Meeting, pk=id)
    context = { 'minutes': minutes}
    return render(request, 'Club/minutes.html', context=context)