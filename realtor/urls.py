from django.urls import path, include
from .views import AgentAPIView, AgentDetailAPIView, TopSellerListView
urlpatterns = [
    path('', AgentAPIView.as_view(), name='agentList'),
    path('<pk>/', AgentDetailAPIView.as_view(), name='agentDetails'),
    path('topseller', TopSellerListView.as_view(), name='topseller'),
]
