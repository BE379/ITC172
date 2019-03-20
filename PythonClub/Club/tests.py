from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse

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

class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/index.html')

class TestLogin(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/loginmessage.html')

class TestLogout(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('logoutmessage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/logoutmessage.html')

class TestMeetingsView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getmeetings'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getmeetings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/meetings.html')

class TestMinutesView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingminutes'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetingminutes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/minutes.html')

class TestNewMeeting(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('newMeeting'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('newMeeting'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newmeeting.html')

class TestNewResource(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('newResource'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('newResource'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/newresource.html')

class TestResourceView(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Club/resources.html')
