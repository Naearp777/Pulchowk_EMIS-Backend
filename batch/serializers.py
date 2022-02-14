from rest_framework import  serializers

from .models import batch


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = batch
        fields = '__all__'