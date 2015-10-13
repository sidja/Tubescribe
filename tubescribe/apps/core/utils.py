from __future__ import unicode_literals
import youtube_dl

from django.conf import settings

import sys 
import os

from django.utils.text import slugify
from django.conf import settings

import sys
from django.http import HttpResponse
from models import ActivityLog, Video





class MyError(Exception):
    pass




def download(url):
	
	video={}

	info = get_video_info(url)

	if info is None:
		print "url not valid"
		#return "url not valid"
		
		raise MyError ({"message":"Provided url is invalid",\
		 "code":"invalid_url"})

	print info['title']
	print info['duration']
	print info['id']
	print slugify(info['title']) + info['id'] 

	if info['duration'] <= settings.MAX_DURATION_SECONDS:


		# Designate file video file path and file name 

		video_title = slugify(info['title'])
		filename = video_title +"-"+ info['id']+".mp4"
		output_filepath = os.path.join(settings.MEDIA_ROOT, filename )


		# Save information about video 

		video["id"]			= info['id']
		video["filename"] 	= filename
		video["duration"] 	= info['duration']
		video["title"] 	  	= info['title']

		#filepath = os.path.join(settings.MEDIA_ROOT, filename)
		
		# Check if file exits in filesystem
		
		file_exists = os.path.exists(output_filepath)
		
		ydl_opts = {
			
			'outtmpl': output_filepath,
			}
			
		try:
			
			# Check if video has been saved on db

			video_obj = Video.objects.get(youtube_id=video["id"])

			if not file_exists:


				video_obj = None

				# Download file
				with youtube_dl.YoutubeDL(ydl_opts) as ydl:
					ydl.download([url])

		except Video.DoesNotExist:

			# If it doesn't exist createa
			video_obj = Video(youtube_id=video["id"],title=video["title"],url=url,video_filename=filename)
			video_obj.save()
			
			
			

			# If file does not exits
			if not file_exists:


				video_obj = None

				# Download file
				with youtube_dl.YoutubeDL(ydl_opts) as ydl:
					ydl.download([url])

		# if video_dbobj and file_exists:
		# 	ActivityLog.objects.create(
		# 	    video=video,
		# 	    action=ActivityLog.DOWNLOAD,
		# 	    client_ip=get_client_ip(request),
		# 	)

		# 	video_dbobj.download_count += 1
		# 	video_dbobj.last_download_date = datetime.datetime.now()
		# 	video_dbobj.save()


		return video

	else:
		print "##################################"
		print
		print "Video length is above Maximum allowed duration"
		print 
		print "##################################"

		#return "exceeds max duration"
		#raise MyError("exceeds max duration")
		raise MyError ({"message":"Video length is above Maximum allowed duration",\
		 "code":"exceeds_max_duration"})


def print_http_response(f):
    """ Wraps a python function that prints to the console, and
    returns those results as a HttpResponse (HTML)"""

    class WritableObject:
        def __init__(self):
            self.content = []
        def write(self, string):
            self.content.append(string)

    def new_f(*args, **kwargs):
        printed = WritableObject()
        sys.stdout = printed
        f(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return HttpResponse(['<BR>' if c == '\n' else c for c in printed.content ])
    return new_f


def get_video_info(url):
    """
    Retrieve the YouTube videos' information without downloading it.
    Source: http://stackoverflow.com/questions/18054500/how-to-use-youtube-dl-\
            from-a-python-programm/18947879#18947879
    """
    ydl = youtube_dl.YoutubeDL()
    ydl.add_default_info_extractors()

    try:
        return ydl.extract_info(url, download=False)
    except youtube_dl.DownloadError:
        return None


def get_client_ip(request):
    """
    Retrieve the client's IPv4 address from the request object.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip