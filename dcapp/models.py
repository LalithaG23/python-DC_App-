from django.db import models
GENDER=(
    ("M", "MALE"),
    ("F", "FEMALE")
    )
class DCModel(models.Model):
    name=models.CharField(max_length=20,blank=False)
    mobile=models.BigIntegerField(unique=True,blank=False)
    gender=models.CharField(max_length=10,choices = GENDER)
    
class Meta:
    db_tables="userinfo"
