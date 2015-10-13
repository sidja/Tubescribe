from django.test import TestCase
from tubescribe.apps.core.models import Video
from django.test import Client

class VideoTestCase(TestCase):
    def setUp(self):
        
        
        Video.objects.create(youtube_id='test_id',title='test track',url='www.youtube.com/asdhasds',video_filename='asdhasds')

    def test_videotable(self):
        """Animals that can speak are correctly identified"""
        vid = Video.objects.get(name="test_id")
        
        self.assertEqual(vid.title(), 'test track')


class InvalidURLTestCase(TestCase):

    c = Client()
    response = c.post('/login/', {'username': 'john', 'password': 'smith'})
    status = response.status_code
    print status
        