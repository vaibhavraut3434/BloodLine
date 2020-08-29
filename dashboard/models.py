from django.db import models

class testing1(models.Model):
    dest = models.CharField(max_length=20)
    marks = models.CharField(max_length=50)

    def getdata(self):
        obj = testing1.objects.all() 
        return obj
    