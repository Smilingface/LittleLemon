from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from restaurant.views import MenuItemsView
from restaurant.models import MenuItem


class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        MenuItem.objects.create(title='IceTea', price=30, inventory=100)
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username='jacbo', email='jacbo@littlelemon.com', password='lemon@adr!')
    
    def test_list_menuitems(self):
        request = self.factory.get('/restaurant/menu/')
        request.user = self.user
        response = MenuItemsView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertContains(response, 'IceCream')