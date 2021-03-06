from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from calendar_app.models import Event
from user_app.models import Profile
from django.forms.models import model_to_dict
from datetime import datetime

from django.db.models import F

class Shifts(models.Model):

    class Meta:
        ordering = ['start_time']

    nurse_type = (
        ('AE', 'A&E Nurse'),
        ('DR', 'Doctor')
    )

    
    hospital_list = (
        (1 , 'London - Atkinson Morley Hospital'),
        (2 , 'London - Banstead Hospital'),
        (3 , 'London - Barnes Hospital, London'),
    )

    area = MultiSelectField(choices=nurse_type, default = 'Blank')
    hospital = MultiSelectField(choices=hospital_list, default = 'Blank')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.area) + " - " + str(self.start_time) + " - " + str(self.end_time)





