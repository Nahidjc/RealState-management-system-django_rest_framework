from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions
from .models import Agent
from .serializers import AgentSerializer
# Create your views here.


class AgentAPIView(ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None


class AgentDetailAPIView(RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class TopSellerListView(ListAPIView):
    print("Top seller")
    queryset = Agent.objects.filter(top_seller=True)
    serializer_class = AgentSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = None
