from django.urls import path
from shiftDB import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #path('shifts', login_required(views.shifts_view), name='shifts_view'),
    #path('shifts_add', login_required(views.shifts_add_view), name='shifts_add_view'),
]