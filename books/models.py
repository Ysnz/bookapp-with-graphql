from django.db import models

# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'Publisher'
        
    def __str__(self):
        return self.p_name

class Book(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    pub = models.ForeignKey('Publisher', models.DO_NOTHING)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=30, null=True)
    quantity = models.IntegerField()
    b_format = models.CharField(max_length=40, null=True)
    prod_year = models.IntegerField()
    filesize = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'Book'
        
    def __str__(self):
        return self.title