from django.db import models


class Result(models.Model):
    request_timestamp = models.DateTimeField("request timestamp")
    entry_id = models.IntegerField()
    runtime = models.FloatField()