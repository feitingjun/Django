from django.urls import path
from . import index

urlpatterns = [
  # path('create', index.create),
  path('', index.query),
]
