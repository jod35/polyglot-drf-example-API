from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloWorldSerializer
from .models import Subscriber

class HelloWorldView(APIView):
    def get(self,request):
        return Response({"message":"Hello"})


    def post(self,request):
        
        serializer=HelloWorldSerializer(data=request.data)

        if serializer.is_valid():
            subscriber_instance=Subscriber.objects.create(**serializer.data)

            return Response({"message":f"Created subscriber {subscriber_instance.id}"})

        else:
            return Response({"errors":serializer.errors})
