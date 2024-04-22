from django.db import models

# Create your models here.
class IpAddress(models.Model):
    ip = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.ip

class Command(models.Model):
    command = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.command
    
class Output(models.Model):
    output = models.TextField(default='')
    def __str__(self) -> str:
        return self.output[:10]
    
