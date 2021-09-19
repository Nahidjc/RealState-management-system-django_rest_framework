from django.urls import path, include
from .views import AgentAPIView, AgentDetailAPIView
urlpatterns = [
    path('', AgentAPIView.as_view(), name='agentList'),
    path('<pk>/', AgentDetailAPIView.as_view(), name='agentDetails'),
]
