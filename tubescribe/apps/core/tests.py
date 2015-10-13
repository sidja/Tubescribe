from django.test import TestCase

# Create your tests here.

from tubescribe.apps.core.models import Video
from django.test import Client

class VideoDBTestCase(TestCase):
	def setUp(self):
		Video.objects.create(youtube_id='test_id', title='test track',\
		  url='www.youtube.com/asdhasds',video_filename='asdhasds')
		

	def test_videotable(self):
		"""Checking Video table"""

		vid = Video.objects.get(youtube_id="test_id")
		
		self.assertEqual(vid.title, 'test track')


class VideoTestCase(TestCase):

    
	def test_InvalidURL(self):
 		c = Client()
 		response = c.post('/create_post/', {'the_post': 'https://www.youtube.com/watch?v=fakeed',})
 		status = response.status_code
 		print status
 		print response.content
 		
 		assert 'is_valid: false' in response.content.replace('"','')

	def test_MaxDuration(self):
		c = Client()
		response = c.post('/create_post/', {'the_post': 'https://www.youtube.com/watch?v=Q2X7eP6d0ME',})
		status = response.status_code
		print status
		print response.content
		assert 'result: exceeds max duration' in response.content.replace('"','')

	def test_VideoDownload(self):
		c = Client()
		response = c.post('/create_post/', {'the_post': 'https://www.youtube.com/watch?v=LOnN3GSRUPQ',})
		status = response.status_code
		print status
		print response.content
		assert 'is_valid: true' in response.content.replace('"','')
