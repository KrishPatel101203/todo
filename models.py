from django.db import models

class Tasks(models.Model):

    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    Created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
