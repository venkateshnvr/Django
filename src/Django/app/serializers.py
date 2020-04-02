from rest_framework import serializers
from .models import UsersArray

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsersArray
        fields = (
            'id',
            'real_name',
            'tz', 
            'activity_periods'
        )