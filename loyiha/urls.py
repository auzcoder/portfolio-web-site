from django.urls import path
from loyiha.views import ProjectList

urlpatterns = [
    path('', ProjectList, name='projects'),
]
