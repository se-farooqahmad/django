from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=20)
    roll = serializers.IntegerField()
    