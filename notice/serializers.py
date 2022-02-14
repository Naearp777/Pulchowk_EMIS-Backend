from rest_framework import  serializers

from .models import notice


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = notice
        fields = '__all__'