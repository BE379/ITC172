from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='firstmeetinga')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def test_stringOutput(self):
        meetingminutes=MeetingMinutes(minutestext='first meeting happened at start time')
        self.assertEqual(str(meetingminutes), meetingminutes.minutestext)

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='google')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='firstmeeting')
        self.assertEqual(str(event), event.eventtitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')