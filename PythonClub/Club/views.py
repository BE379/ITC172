from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting
from .forms import ResourceForm, MeetingForm

# Create your views here.
def index (request):
    return render(request, 'Club/index.html')

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

def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'Club/newresource.html', {'form': form})

def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'Club/newmeeting.html', {'form': form})