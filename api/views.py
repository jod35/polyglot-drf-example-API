from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorldView(APIView):
    def get(self,request):
        return Response({"message":"Hello"})


    def post(self,request):
        name=request.data.get('name')

        if not name:
            return Response({"message":"NO name passed"})


        return Response({"message":f"Hello {name}"})