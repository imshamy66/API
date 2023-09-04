from rest_framework import serializers
from .models import Employe

class EmployeSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=20)
    dgs = serializers.CharField(max_length=30)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=40)

    def create(self,validatedData):
        return Employe.objects.create(**validatedData)
    
    def update(self, instance, validatedData):
        if("name" in validatedData and validatedData["name"]!=""):
            instance.name = validatedData["name"]
        if("email" in validatedData and validatedData["email"]!=""):
            instance.email = validatedData["email"]
        if("dgs" in validatedData and validatedData["dgs"]!=""):
            instance.dgs = validatedData["dgs"]
        if("salary" in validatedData and validatedData["salary"]!=""):
            instance.salary = validatedData["salary"]
        if("city" in validatedData and validatedData["city"]!=""):
            instance.city = validatedData["city"]
        if("state" in validatedData and validatedData["state"]!=""):
            instance.state = validatedData["state"]
        instance.save()
        return instance