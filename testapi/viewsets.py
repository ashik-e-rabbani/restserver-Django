from rest_framework  import viewsets
from . import models
from . import serializers

class EmployeeViewswts(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer