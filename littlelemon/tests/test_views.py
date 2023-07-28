from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from restaurant.models import MenuItem, Category
from restaurant.serializers import MenuItemSerializer, CategorySerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(title="Entree")
        MenuItem.objects.create(
            title="Bruschetta", price=5.99, inventory=10, category=self.category)
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        self.url = 'http://127.0.0.1:8000/restaurant/api/menu-items/'

    def test_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.get(self.url)
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        data = {
            "title": "Burger",
            "price": 8.99,
            "inventory": 30,
            "category_id": self.category.id
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 2)
        self.assertEqual(MenuItem.objects.last().title, "Burger")
