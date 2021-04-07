from rest_framework import serializers
from teammates.models import Departments, Teammates

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = (
            'DepartmentId', 
            'DepartmentName'
        )

class TeammateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammates
        fields = (
            'TeammateId', 
            'TeammateName',
            'Department',
            'JoinDate',
            'ProfilePicFileName'
        )