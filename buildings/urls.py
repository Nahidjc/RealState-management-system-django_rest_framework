from django.urls import path, include
from .views import HomeListView, HomeDetailsView, ImageView
urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('<slug>/', HomeDetailsView.as_view(),),
    path('images/<pk>/', ImageView.as_view(), name='images'),
]
