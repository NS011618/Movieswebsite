from datetime import datetime, timedelta
from django.shortcuts import render
from pyexpat import model
from statistics import mode
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader
from mvapp.models import mshow
from numpy import diff
import datetime
from mvapp import forms,models
from django.urls import reverse
# Create your views here.
def display(request):
    m_list=mshow.objects.all()
    my_dict={'m_list':m_list}
    return render(request,'mvapp/input.html',context=my_dict)


def feed(request):
    
    form=forms.stForm()
    if request.method=='POST':
        form=forms.stForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'mvapp/one.html',{'form':form})

# updating the rating of the movie
def index(request):
  mymembers = mshow.objects.all().values()  
  context = {
    'mymembers': mymembers,
  }
  return render(request,'mvapp/index.html',context)

def update(request, id):  
  mymember = mshow.objects.get(id=id) 
  context = {
    'mymember': mymember,
  }
  return render(request,'mvapp/update.html',context)
  
def updaterecord(request,id):
  first = request.POST['first']  
  member =mshow.objects.get(id=id)
  member.rating = first  
  member.save()
  return HttpResponseRedirect(reverse('index'))

#delete details if it is one year old movie
def delete(request):
  member = models.mshow.objects.all()
  count=0
  for i in member:
        print(i)
        x= member.filter().values('Releasedate')
        print(x[count]['Releasedate']) 
        k=str(x[count]['Releasedate'])
        count=count+1
        z=datetime.datetime.now()
        differnce=int(z.strftime("%Y"))-int(k[0:4])
        print("Difference",differnce,z.strftime("%Y"),k[0:4],k,z)
        if differnce>1:
          i.delete()
  return HttpResponseRedirect(reverse('index'))