from django.test import TestCase
from restaurant.models import MenuItem, Category


class MenuItemTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Dessert")

    def test_get_item(self):

        item = MenuItem.objects.create(
            title="Ice Cream", price=80, inventory=100, category=self.category)
        self.assertEqual(str(item), "Ice Cream : 80")
