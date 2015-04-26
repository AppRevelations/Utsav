from django.http import HttpResponse
from utsav.models import Fest,Event,User
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


        response = HttpResponse(json.dumps(responseArray), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

#function to return details of a particular fest i.e descrption of its events
def fest_details(request,offset):
	#fetch all events of a fest

        #offset is id of the fest 
	id= int(offset)
	print id
	responseArray = []
	for event in Event.objects.filter(fest_id= id):
	    data = {}
	    data['id']=event.id
	    data['event_name'] = event.event_name
	    data['event_desc'] = event.event_desc
	    data['timings'] = event.timings
	    data['place'] = event.place
	    data['url'] = event.image_url
	    data['contact_person'] = event.contact_person
	    data['contact_number'] = event.contact_number
	    responseArray.append(data)
	
	response = HttpResponse(json.dumps(responseArray), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response


#this is function to store details of user 
def saveuser(request):
        #fetch data from POST request and add it to database
        u= User()
        u.first_name=request.POST.get('first_name','name')
        u.last_name=request.POST.get('last_name','name')
        u.password=request.POST.get('password','123456789')
        u.email_id=request.POST.get('email','abc@example.com')
        u.contact_number= request.POST.get('contact','1234567890')
        u.image_url=request.POST.get('image_url','abc.com')
        u.save()
        return HttpResponse("data saved")
    

#this is function to store details of fest created by user 
def savefest(request):
        #fetch data from POST request and add it to database
        p= Fest()
        p.fest_name=request.POST.get('name','name1')
        p.fest_desc=request.POST.get('desc','This is a fest')
        p.timings= request.POST.get('time','10-5')
        p.place=request.POST.get('place','Delhi')
        p.url=request.POST.get('url','abc.com')
        p.save()
        print request.POST.get('name','name')
        fest = Fest.objects.get(fest_name=request.POST.get('name','name1'))
        print fest
        return HttpResponse(fest.id)


#this is function to store details of event of fest created by user 
def saveevent(request):
        #fetch data from POST request and add it to database
        p= Event()
        p.fest_id=request.POST.get('fest_id','1')
        p.event_name=request.POST.get('name','name')
        p.event_desc=request.POST.get('desc','This is a fest')
        p.timings= request.POST.get('time','10-5')
        p.place=request.POST.get('place','Delhi')
        p.image_url=request.POST.get('url','abc.com')
        p.contact_person=request.POST.get('contact_name','name')
        p.contact_number=request.POST.get('contact_number','1234567890')
        p.save()
        
        return HttpResponse('Data Saved')

    
    
