from django.urls import path

from . import views

urlpatterns = [
    path('new', views.new_poll, name='new-poll'),
    path('delete/<int:id>', views.delete_poll, name='delete-poll'),
    path('edit/<int:id>', views.edit_poll, name='edit-poll'),
    path('end/<int:id>', views.end_poll, name='end-poll'),
]
