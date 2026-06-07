from django.db import models

class SentimentHistory(models.Model):

    text = models.TextField()

    result = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result
