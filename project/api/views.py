from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
# model object - single student data

def student_detail(request,pk):
    stu = Student.objects.get(id=pk) #getting a single object of model instance with id = 1 and storing it in stu variable to serialize it i.e converting this complex data of model instance into python object which will further be converted into json by using render or directly rendering it into json
    # make a serializer variable with any name
    #we will name it serialiser here
    #print(stu)
    serialized_data = StudentSerializer(stu) # this is a serialis=zer in which the complex data of model instance of a single object with id = 1 is passed
    #serializer will convert the data into python data which is stored in this serializer variale (data in python data object like dict)
    #now we need to convert this python object i.e serializer into json data for that we will use json rendere
    #json variable stored in json_data variable name
    #print(serialized_data)
    #print(serialized_data.data)
    json_data = JSONRenderer().render(serialized_data.data)
    #now we need to send this json to the client in the form of response 
    #send this json data to client in the form of http response
    #print(json_data)
    return HttpResponse(json_data, content_type='application/json')
    #now add it into url

    #now lets get all the data altogther i.e query set (complex data)
def all_student_detail(request):
    stu = Student.objects.all() 
    serialized_data = StudentSerializer(stu, many = True)
    # json_data = JSONRenderer().render(serialized_data.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serialized_data.data, safe = False)
    #now add it into url


