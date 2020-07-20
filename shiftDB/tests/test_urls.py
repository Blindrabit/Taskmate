from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase
from todolist_app.urls import *
from shiftDB.views import shifts_view, shifts_add_view



class TestShiftUrls(SimpleTestCase):

    def test_shift_table_url(self):
        url = reverse('shifts')
        self.assertEqual(resolve(url).func, shifts_view)

        
    def test_shift_add_url(self):
        url = reverse('shifts_add')
        self.assertEqual(resolve(url).func, shifts_add_view)
