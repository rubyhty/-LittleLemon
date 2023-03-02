from django.test import TestCase
from restaurant.models import menu


class MenuViewTest(TestCase):
    def setup(self):
        item = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")