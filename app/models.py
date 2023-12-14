from django.db import models

# Create your models here.

class Book(models.Model):
    bid=models.IntegerField(primary_key=True)
    bname=models.CharField(max_length=100)
    publish=models.DateField()
    price=models.IntegerField()
    
    def __str__(self):
        return self.bname
    
class Author(models.Model):
    bid=models.ForeignKey(Book,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    DOB=models.DateField(max_length=100)
    URL=models.URLField( max_length=200) 
    
    def __str__(self):
        return self.name
