from rest_framework.generics import CreateAPIView

from apps.models import AppLog
from apps.serializers import AppLogSerializer


class CreateAppLog(CreateAPIView):
    serializer_class = AppLogSerializer

    def get_queryset(self):
        return AppLog.objects.filter(app_id=self.request.data.get('app_id'))

