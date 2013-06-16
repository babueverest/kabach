from django.http import HttpResponse
from mymap.models import complaint 
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
def push_in_db(request):
		code=request.GET.get('text')
		Location=code[0]
		Type=code[1]
		Category=code[2]
		Message=code[3]
		#Published=request.GET.get('published')
		b=complaint(Location=Location,Type=Type,Category=Category,Message=Message)
		b.save()
		print "Thanks for your query, we will contact soon."
		return
		return HttpResponseRedirect("/")

def index(request):
		location=[]
		q=complaint.objects.filter(Published=True)
		for i in q:
			print(i.Location)
			location.append(i.Location)
		print location
		return render_to_response("index.html",{'location':location})
 

