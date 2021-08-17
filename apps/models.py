from django.db import models


class App(models.Model):
    app_id = models.CharField(max_length=200)


class AppLog(models.Model):
    app_id = models.CharField(max_length=200)
    message = models.CharField(max_length=400, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'APP_ID_{self.app_id} LOG_{self.pk}'
