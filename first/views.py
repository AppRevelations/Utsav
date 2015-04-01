from django.http import HttpResponse
from utsav.models import Fest,Event
import json

def hello(request):
    return HttpResponse(request)
	
#this function is called when index.html is started or utsav.com is hit	
def home(request):
	#fetch all images with fest name from db and send json response in return

        #json array for respose
	responseArray = []
	for fest in Fest.objects.all():
            #json object, add fest detaila like id,name,desc,place,timings,url in respose 
	    data = {}
	    data['id']=fest.id
	    data['fest_name'] = fest.fest_name
	    data['fest_desc'] = fest.fest_desc
	    data['timings'] = fest.timings
	    data['place'] = fest.place
	    data['url'] = fest.image_url

	    #append json object in json array
	    responseArray.append(data)
	    #print fest.id
	    #print fest.fest_name
	    #print fest.image_url
	
	return HttpResponse(json.dumps(responseArray), content_type="application/json")


#function to return details of a particular fest i.e descrption of its events
def fest_details(request,offset):
	#fetch all events of a fest

        #offset is id of the fest 
	id= int(offset)
	responseArray = []
	for event in Event.objects.filter(fest_id= id):
	    data = {}
	    data['id']=fest.id
	    data['event_name'] = event.event_name
	    data['event_desc'] = event.event_desc
	    data['timings'] = fest.timings
	    data['place'] = fest.place
	    data['url'] = fest.image_url
	    data['contact_person'] = fest.contact_person
	    data['contact_number'] = fest.contact_number
	    responseArray.append(data)
	
	return HttpResponse(json.dumps(responseArray), content_type="application/json")


#this is function to store details of fest created by user 
def savefest(request):
        #fetch data from POST request and add it to database
        p= Fest()
        p.fest_name='name'
        p.fest_desc='desc'
        p.timings= 'time'
        p.place='place'
        p.url='abc.com'
        p.save()
        return HttpResponse("data saved")
    
