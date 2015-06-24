from django.db import models

# Create your models here.

class Quote(models.Model):
    date = models.DateField()
    currencies = models.TextField()
    ratio = models.TextField()

    def __str__(self):
        return "%s (%s)" % (self.currencies, self.ratio)
