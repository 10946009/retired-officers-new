from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from .admin import *
from .models import *

class MyModelAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.model_admin = MyModelAdmin(MyModel, self.site)

    def test_model_admin_should_register_model(self):
        self.assertIn(MyModel, self.site._registry)

    def test_model_admin_should_display_correct_fields(self):
        expected_fields = ['field1', 'field2', 'field3']
        self.assertEqual(self.model_admin.fields, expected_fields)

    def test_model_admin_should_display_correct_list_display(self):
        expected_list_display = ['field1', 'field2', 'field3']
        self.assertEqual(self.model_admin.list_display, expected_list_display)

    # Add more tests as needed

# Add more test classes for other models and admin classes if necessary