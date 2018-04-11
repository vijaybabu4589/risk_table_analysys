from django.db import models

class riskdata(models.Model):
    risk=models.CharField(max_length=50,null=True,blank=True)
    riskdesc = models.CharField(max_length=50,null=True,blank=True)
    risksol = models.CharField(max_length=50,null=True,blank=True)
    consequence = models.IntegerField(null=True)
    likelihood = models.IntegerField(null=True)

