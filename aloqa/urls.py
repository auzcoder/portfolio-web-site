from django.urls import path
from aloqa.views import contact_views


urlpatterns = [
    path('', contact_views, name='contact'),
]
