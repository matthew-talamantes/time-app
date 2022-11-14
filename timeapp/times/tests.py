from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from .models import Client

# Create your tests here.

#########################
# Model Tests
#########################
class ClientModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@test.com', password='i2!aD452k')
        login = self.client.login(username='testuser', email='test@test.com', password='i2!aD452k')
        Client.objects.create(user=self.user, name='test client')

    def test_client_name(self):
        client1 = Client.objects.filter(name='test client')[0]
        self.assertEqual(str(client1), 'test client')

#########################
# Endpoint Tests
#########################
class ClientEndpointTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='endpointtester', email='test2@test.com', password='12345')
        login = self.client.login(username='endpointtester', email='test2@test.com', password='12345')
    
    def test_client_create(self):
        url = reverse('client-create')
        data = {'name': 'Endpoint Test', 'company': 'Endpoint Tests unlimited'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get(name='Endpoint Test').company, 'Endpoint Tests unlimited')
