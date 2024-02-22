from main import models

from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import serializers

@api_view(['POST'])
def staff_create(request):
    staff = models.Staff.objects.all()
    serializer = serializers.CreateStaffSerializer(staff, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_staff(request):
    staff = models.Staff.objects.all()
    serializer = serializers.ListStaffSerializer(staff, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def attendance_create(request):
    staff = models.Attendance.objects.all()
    serializer = serializers.ListAttendanceSerializer(staff, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def attendance_day(request):
    staff = models.Attendance.objects.all()
    serializer = serializers.ListAttendanceSerializer(staff, many=True)
    return Response(serializer.data)