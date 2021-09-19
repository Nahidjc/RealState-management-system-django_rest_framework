from django.urls import path, include
from .views import HomeListView, HomeDetailsView
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('<slug>/', HomeDetailsView.as_view(),)
]
