from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def home(request):
      #Create Color Query and send it to main page
      queryset = Color.objects.all()
      context = {'colors' : queryset}
      print(context)
      return render(request,"index.html",context)


def homePost(request):
      global context
      print(request.method)
      if request.method == "POST":
         data = request.POST
         #get values from all inputs
         length = data.get('length')
         width = data.get('width')
         color = data.get('color')

         try:
                  #Create 3 queries for Note, Color and Country and send it to details page
                  notequery = Note.objects.filter(length = length,width = width, color_id=color).first()
                  countryId = notequery.country_id
                  colorId = notequery.color_id
                  if(notequery):
                      context = {'color' : colorId, 'note': notequery, 'country':countryId}
                      return render(request,"details.html",context)
                  else:
                  # If Note is not Found Send Error Message
                      queryset = Color.objects.all()
                      messages.error(request,'No Data Found! Please use correct parameters')
                      return redirect('/')
         except:
                  #For any type of error send Error Message
                  queryset = Color.objects.all()
                  messages.error(request,'No Data Found! Please use correct parameters')
                  return redirect('/')

      else:
         #If data is not sent return back to same page
         queryset = Color.objects.all()
         context = {'colors' : queryset}

      print(context)
      return render(request,"index.html",context)


