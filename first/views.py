from django.http import HttpResponse
from utsav.models import Fest,Event,User,ContactUs
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
<<<<<<< HEAD
        #fetch data from POST request and add it to database
        print "rgff"
        print request
        u= User()
        u.first_name=request.GET['first_name']
        print u.first_name
        print request.GET['first_name']
=======
        u= User()
        u.first_name=request.GET['first_name']
        print u.first_name
>>>>>>> cfafb56756810d690fe02a0ea027663ca68b5ecc
        u.last_name=request.GET['last_name']
        u.password=request.GET['password']
        u.email_id=request.GET['email']
        u.contact_number= request.GET['contact']
        u.image_url=request.GET['image_url']
        u.save()
        response = HttpResponse("data saved")
        response["Access-Control-Allow-Origin"] = "*"
        return response
    

#this is function to store details of fest created by user 
def savefest(request):
        #fetch data from GET request and add it to database
        p= Fest()
        p.fest_name=request.GET['name']
        p.fest_desc=request.GET['desc']
        p.timings= request.GET['time']
        p.place=request.GET['place']
        p.url=request.GET['url']
        p.save()
        print request.GET['name']
        fest = Fest.objects.get(fest_name=request.GET['name'])
        print fest
        response = HttpResponse(fest.id)
        response["Access-Control-Allow-Origin"] = "*"
        return response


#this is function to store details of event of fest created by user 
def saveevent(request):
        #fetch data from GET request and add it to database
        p= Event()
        p.fest_id=request.GET['fest_id']
        p.event_name=request.GET['name']
        p.event_desc=request.GET['desc']
        p.timings= request.GET['time']
        p.place=request.GET['place']
        p.image_url=request.GET['url']
        p.contact_person=request.GET['contact_name']
        p.contact_number=request.GET['contact_number']
        p.save()
        response = HttpResponse("data saved")
        response["Access-Control-Allow-Origin"] = "*"
        
        return response


#this is function to store contact us messages 
def contactus(request):
        #fetch data from GET request and add it to database
        c= ContactUs()
        c.name=request.GET['name']
        c.email=request.GET['email']
        c.message= request.GET['message']
        c.save()
        response = HttpResponse("data saved")
        response["Access-Control-Allow-Origin"] = "*"
        
        return response
    
