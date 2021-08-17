from rest_framework import serializers

from apps.models import AppLog


class AppLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppLog
        fields = (
            'app_id', 'message'
        )
