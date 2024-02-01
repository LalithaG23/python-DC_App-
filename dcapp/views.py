from django.shortcuts import render,redirect
from dcapp.forms import DCForm
from dcapp.models import DCModel

def showform(request):
    formobj = DCForm()
    userdata=DCModel.objects.all() #select * from tbl
    dt={"formobj":formobj,"data":userdata}
    return render(request,"index.html",dt)

def savedata(request):
    formobj = DCForm(request.POST)
    formobj.save()#insert into tbl values()
    return redirect("/")

def removedata(request,id):
    a=DCModel.objects.get(id=id) #dbid = user input id
    a.delete()
    return redirect("/")