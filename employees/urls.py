from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView, EmployeeRetrieveUpdateView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-detail'),
path('employees/<int:pk>/', EmployeeRetrieveUpdateView.as_view(), name='employee-detail')
]
