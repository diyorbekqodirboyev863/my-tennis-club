from django.urls import path
from . import views

urlpatterns = [
    path('members/', view=views.members, name='members'),
    path('all_members/', view=views.all_members, name='all_members'),
    path('all_members/details/<slug:slug>/', view=views.details, name='details'),
    path('', view=views.main, name='main'),
    path('testing/', view=views.testing, name='testing'),
    path('table/', view=views.members_table, name='table'),
    path('add_member/', view=views.add_member, name='add_member'),
    path('update_member/<slug:slug>/', view=views.update_member, name='update_member'),
    path('delete_member/<slug:slug>/', view=views.delete_member, name='delete_member'),
    path('search_member/', view=views.search_member, name='search_member'),
]