from main import models
from rest_framework import serializers

class ListStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = '__all__'

class CreateStaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Staff
        fields = ['f_name','l_name']
        