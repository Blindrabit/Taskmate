import unittest
from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase
from taskmate.urls import *
from user_app.views import profile, register


class TestCalendarUrls(SimpleTestCase):

    def test_profile_url(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
    
