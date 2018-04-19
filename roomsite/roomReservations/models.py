from django.db import models

# Create your models here.

class RoomStatus(models.Model):
    
    myRoom = models.CharField(max_length=20)
    myStatus = models.BooleanField(default=0)

    def __str__(self):
        return self.myStatus
    
