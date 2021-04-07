from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from rest_framework.parsers import JSONParser
from teammates.models import Departments, Teammates
from teammates.serializers import DepartmentSerializer, TeammateSerializer

@csrf_exempt
def departmentApi(request, id=0):
    # Display Departments
    if request.method == 'GET':
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)

    # Add new Departments
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Successfully added new Department.", safe=False)
        return JsonResponse("Failed to add Department, please try again.", safe=False)

    # Edit an existing Department
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Department updated successfully.", safe=False)
        return JsonResponse("Failed to update Department, please try again.", safe=False)

    # Delete an existing Department
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Department deleted successfully.", safe=False)


@csrf_exempt
def teammateApi(request, id=0):
    # Display Teammates
    if request.method == 'GET':
        teammates = Teammates.objects.all()
        teammate_serializer = TeammateSerializer(teammates, many=True)
        return JsonResponse(teammate_serializer.data, safe=False)

    # Add new Teammates
    elif request.method == 'POST':
        teammate_data = JSONParser().parse(request)
        teammate_serializer = TeammateSerializer(data=teammate_data)
        if teammate_serializer.is_valid():
            teammate_serializer.save()
            return JsonResponse("Successfully added new Teammate.", safe=False)
        return JsonResponse("Failed to add Teammate, please try again.", safe=False)

    # Edit an existing Teammate
    elif request.method == 'PUT':
        teammate_data = JSONParser().parse(request)
        teammate = Teammates.objects.get(TeammateId=teammate_data['TeammateId'])
        teammate_serializer = TeammateSerializer(teammate, data=teammate_data)
        if teammate_serializer.is_valid():
            teammate_serializer.save()
            return JsonResponse("Teammate updated successfully.", safe=False)
        return JsonResponse("Failed to update Teammate, please try again.", safe=False)

    # Delete an existing Teammate
    elif request.method == 'DELETE':
        teammate = Teammates.objects.get(TeammateId=id)
        teammate.delete()
        return JsonResponse("Teammate deleted successfully.", safe=False)

@csrf_exempt
def saveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
