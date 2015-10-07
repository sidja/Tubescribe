from __future__ import unicode_literals
import youtube_dl

from django.conf import settings

import sys 
import os

from django.utils.text import slugify



def download(url):
	
	filename = "temp.mp4"
	temp_filepath= "/home/sid/code/test/media"

	full_path = temp_filepath+filename

	output_filepath = os.path.join(settings.MEDIA_ROOT, filename  )

	
	ydl_opts = {
		
		'outtmpl': output_filepath,
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([url])


import sys
from django.http import HttpResponse

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