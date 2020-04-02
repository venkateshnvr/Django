from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import UsersArray
from django.http import Http404
from rest_framework import status
from django.db.models.query import QuerySet
# Create your views here.

class Users(APIView):

    def get(self, request):
        users = UsersArray.objects.all()
        serializer = UsersSerializers(users, many=True)
        # print('serializer: ', serializer.data.activity_periods)
        return Response({
                "ok": True,
                "members": serializer.data
            })

