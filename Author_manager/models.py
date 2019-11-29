from django.db import models

# Create your models here.
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey(to="Publish", on_delete = models.CASCADE)
    author = models.ManyToManyField(to="Author")

class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    tel = models.CharField(max_length=32)

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    age = models.IntegerField()
    detail = models.OneToOneField(to="Author_detail", on_delete = models.CASCADE)

class Author_detail(models.Model):
    nid = models.AutoField(primary_key=True)
    addr = models.CharField(max_length=32)
    tel = models.IntegerField()
