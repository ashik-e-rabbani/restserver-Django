from testapi.viewsets import EmployeeViewswts
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewswts)