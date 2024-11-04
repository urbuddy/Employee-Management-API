from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Employee


class EmployeeTests(APITestCase):
    def setUp(self):
        # Create a test user and obtain JWT token
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']

        # Set up authorization headers for authenticated requests
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Define a sample employee data payload
        self.employee_data = {
            "name": "Jacob Doe",
            "email": "jacob@example.com",
            "department": "HR",
            "role": "Recruiter"
        }

    def test_create_employee(self):
        response = self.client.post(reverse('employee-list-create'), self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.employee_data['name'])

    def test_list_employees(self):
        # Create a sample employee
        self.client.post(reverse('employee-list-create'), self.employee_data)

        # List all employees
        response = self.client.get(reverse('employee-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)  # Check pagination

    def test_retrieve_employee(self):
        # Create a sample employee and retrieve it
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.get(reverse('employee-detail', args=[employee.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], employee.name)

    def test_update_employee(self):
        # Create a sample employee
        employee = Employee.objects.create(**self.employee_data)

        # Update data, including all required fields
        update_data = {
            "name": "Jane Doe",
            "email": employee.email,  # Ensure email is included
            "department": employee.department,
            "role": employee.role
        }

        # Use PUT request with full data
        response = self.client.put(reverse('employee-detail', args=[employee.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_data['name'])

    def test_delete_employee(self):
        # Create a sample employee and delete it
        employee = Employee.objects.create(**self.employee_data)
        response = self.client.delete(reverse('employee-detail', args=[employee.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_employee_with_existing_email(self):
        # Create an employee and attempt to create another with the same email
        self.client.post(reverse('employee-list-create'), self.employee_data)
        response = self.client.post(reverse('employee-list-create'), self.employee_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)


