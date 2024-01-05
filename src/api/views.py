from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from taskmanager.models import models


class GetData(ListAPIView):
    def get(self):
        person = {"name": "kevin", "Age": 24}
        return Response(person)
