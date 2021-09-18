from django.urls import path, include
from .views import ContactApiView
urlpatterns = [
    path('', ContactApiView.as_view, name='contact'),
]
