from django.urls import path
from . import views

urlpatterns = [
    path('members/', view=views.members, name='members'),
    path('all_members/', view=views.all_members, name='all_members'),
    path('all_members/details/<slug:slug>/', view=views.details, name='details'),
    path('', view=views.main, name='main'),
    path('testing/', view=views.testing, name='testing'),
    path('table/', view=views.members_table, name='table'),
]