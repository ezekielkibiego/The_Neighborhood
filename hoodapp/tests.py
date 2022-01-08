from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Test Location')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

   
