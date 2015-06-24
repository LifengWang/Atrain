from django.db import models

# Create your models here.

class Location(models.Model):
    city = models.CharField(maxlength=50)
    state = models.CharField(maxlength=50, null=True, blank=True)
    country = models.CharField(maxlength=50)
    time = models.timezone

    def __str__(self):
        if self.state:
            return "%s, %s, %s" % (self.city, self.state, self.country)
        else:
            return "%s, %s" % (self.city, self.country)

class User(models.Model):
    pub_date = models.DateField()
    job_title = models.CharField(maxlength=50)
    job_description = models.TextField()
    location = models.ForeignKey(Location)

    def __str__(self):
        return "%s (%s)" % (self.job_title, self.location)