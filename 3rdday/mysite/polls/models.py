from django.db import models

class Message(models.Model):

    def __str__(self):
        return self.text
