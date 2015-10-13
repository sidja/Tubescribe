from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from braces.views import JSONResponseMixin, AjaxResponseMixin
from django.views.generic import TemplateView, View
from django.template import RequestContext
import json

from utils import download
from utils import print_http_response
from utils import MyError, get_client_ip
from models import ActivityLog, Video

# Create your views here.

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def test(request):
	return render_to_response('test.html', context_instance=RequestContext(request))


def test_get_video(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = CheckoutFormCustomerName(request.POST, request.FILES)
		#if form.is_valid(): # is the form valid?
			#form.save(commit=True) # yes? save to database
		return "howdy sailor"
		#else:
		#	print form.errors # no? display errors to end user
	#else:
	#	form = CheckoutFormCustomerName()
	return render_to_response('test.html', {'form': form}, context)


class AjaxView(JSONResponseMixin, AjaxResponseMixin, View):
    """
    Ajax view to start the video conversion.
    """

    def post_ajax(self, request, *args, **kwargs):

		#url = self.parse_url(request.POST.get('url', '').strip())
		data = { 'task_id': task.id,}
		
		data['url'] = "url"
		
		data['message'] = 'Conversion successful!'
		data['is_ready'] = True
		data['youtube_id'] = "youtube_id"
		data['title'] = "Title"
		data['filename'] = "filename"
		data['download_link'] = "download_link"
		
		
		
		

		return self.render_json_response(data, status=200)

    	#return HttpResponse("Hows it going")


    def parse_url(self, url):
        """
        Remove the list parameter from the URL as we currently don't support
        conversion of an entire playlist.
        """
        qs = parse_qs(urlparse(url).query)
        if qs.get('list', None):
            del(qs['list'])
            parts = urlsplit(url)
            return urlunsplit([
                parts.scheme,
                parts.netloc,
                parts.path,
                urllib.urlencode(qs, True),
                parts.fragment
            ])

        return url




       # if valid 		--------------------> Check
 		# if it does not exist in db
		  # if duration  (10 min)
		   # download   --------------------> Check
		    # slugify	--------------------> Check
		     # rename	--------------------> Check
		      # relay file to user
		       # log in db	
		        # respond with url



def create_post(request):

	

	if request.method == 'POST':
		post_text = request.POST.get('the_post')
		response_data = {}

		#post = Post(text=post_text, author=request.user)
		#post.save()


		
		# response_data['postpk'] = "post.pk"
		# response_data['text'] = "post.text"
		# response_data['created'] = "post.created.strftime()"
		# response_data['author'] = "post.author.username"


		try:

			video = download(post_text)


		except MyError as e:
			
			details = e.args[0]
			
			print details["code"]  

			if details["code"] == "exceeds_max_duration":
				response_data['is_valid'] = 'false'
				response_data['result'] = "exceeds max duration"

			elif details["code"] == "invalid_url":
				response_data['is_valid'] = 'false'
				response_data['result'] = "invalid url"

		

			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"		
				)

		

		if isinstance(video["filename"], str) and not video["filename"]:
			response_data['is_valid'] = 'true'
			response_data['result'] = post_text
			response_data['filename'] = video["filename"]
			response_data['message'] = "all good"


			client_ip = get_client_ip(request)

			video = video["id"]

			activity =  ActivityLog.objects.create(
            video=video["filename"],
            client_ip=client_ip,
            action=ActivityLog.DOWNLOAD,
       )

			activity.save()

		else:

			response_data['is_valid'] = 'true'
			response_data['result'] = post_text
			response_data['message'] = "Filename error"
			response_data['filename'] = video["filename"]

	else:
		response_data['is_valid'] = 'false'
		response_data['result'] ="invalid request"

	return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"		
				)



@print_http_response
def my_view(request):
   print "some output here"
   for i in [1, 2, 3]:
      print i