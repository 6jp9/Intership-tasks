from rest_framework.serializers import ModelSerializer
from .models import Test
class TestSerializer(ModelSerializer):

    class Meta:
        model = Test
        fields = '__all__'
    def create(self,validated_data):
        return Test.objects.create(**validated_data)