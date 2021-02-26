from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    name=serializers.CharField(required=False,max_length=25)
    age=serializers.IntegerField(required=False,min_value=5)
    email=serializers.EmailField()

    
