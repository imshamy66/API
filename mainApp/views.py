from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from .serializers import EmployeSerializers
from .models import Employe

def home(request):
    return render(request,"index.html")

@csrf_exempt
def api(request):
    if(request.method=='GET'):
        jData = request.body
        stream = io.BytesIO(jData)
        pdata = JSONParser().parse(stream)
        id = pdata.get("id",None)
        name = pdata.get("name",None)
        email = pdata.get("email",None)
        dgs = pdata.get("dgs",None)
        city = pdata.get("city",None)
        state = pdata.get("state",None)
        if(id):
            data = Employe.objects.filter(id=id)
        elif(name):
            data = Employe.objects.filter(name=name)
        elif(email):
            data = Employe.objects.filter(email=email)
        elif(dgs):
            data = Employe.objects.filter(dgs=dgs)
        elif(city):
            data = Employe.objects.filter(city=city)
        elif(state):
            data = Employe.objects.filter(state=state)
        else:
            data = Employe.objects.all()
        employeSerializer = EmployeSerializers(data,many=True)
        jData = JSONRenderer().render(employeSerializer.data)
        return HttpResponse(jData,content_type="application/json")
    elif(request.method=='POST'):
        jData = request.body
        stream = io.BytesIO(jData)
        pdata = JSONParser().parse(stream)
        employeSerializer = EmployeSerializers(data=pdata)
        if(employeSerializer.is_valid()):
            employeSerializer.save()
            res = {"msg": "Record Has Been Submitted !!!!!"}
        else:
            res = {"msg": "Invalid Input"}
        
        jData = JSONRenderer().render(res)
        return HttpResponse(jData,content_type="application/json")
    
    elif(request.method=='PUT'):
        jData = request.body
        stream = io.BytesIO(jData)
        pdata = JSONParser().parse(stream)
        id = pdata.get("id",None)
        try:
            emp = Employe.objects.get(id=id)
            employeSerializer = EmployeSerializers(emp,data=pdata,partial=True)
            if(employeSerializer.is_valid()):
                employeSerializer.save()
                res = {"msg": "Record has been Updated !!!!!"}
            else:
                res = {"msg": "Invalid Record"}
        except:
            res = {"msg": "No Record Found to Update "}
        jData = JSONRenderer().render(res)
        return HttpResponse(jData,content_type="application/json")
    
    elif(request.method=='DELETE'):
        jData = request.body
        stream = io.BytesIO(jData)
        pdata = JSONParser().parse(stream)
        id = pdata.get("id",None)
        try:
            emp = Employe.objects.get(id=id)
            emp.delete()
            res = {"msg": "Record Has Been Deleted !!!!!"}
        except:
            res = {"msg": "No Record Found To Delete "}
        jData = JSONRenderer().render(res)
        return HttpResponse(jData,content_type="application/json")