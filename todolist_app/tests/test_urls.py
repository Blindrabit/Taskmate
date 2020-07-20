import unittest
from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase
from taskmate.urls import *
from todolist_app.urls import *
from todolist_app.views import *

class TestCalendarUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)


    def test_todolist_url(self):
        url = reverse('todolist')
        self.assertEquals(resolve(url).func, todolist)
