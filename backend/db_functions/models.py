from django.db import models

class Result(models.Model):
    request_timestamp = models.DateTimeField()
    runtime = models.FloatField()
    dataset = models.TextField()
    model = models.TextField()
    input_json = models.TextField()
    stack_precision = models.FloatField()
    stack_accuracy = models.FloatField()
    stack_f1 = models.FloatField()
    stack_recall = models.FloatField()
    output_json = models.TextField()

    def format_output_json(self):
        data = {
            "request_timestamp": self.request_timestamp,
            "runtime": self.runtime,
            "dataset": self.dataset,
            "model": self.model,
            "input_json": self.input_json,
            "stack_precision": self.stack_precision,
            "stack_accuracy": self.stack_accuracy,
            "stack_f1": self.stack_f1,
            "stack_recall": self.stack_recall,
            "output_json": self.output_json
            }
        return data