from django.db import models

class user(models.Model):
    id = models.CharField(max_length=36,primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
  


    
class todo(models.Model):
    id = models.CharField(max_length=36,primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    img = models.CharField(max_length=200,default=None)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
