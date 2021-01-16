from django.db import models
# Create your models here.

class Coffee(models.Model):
    Product_Name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    price = models.DecimalField( max_digits=6 , decimal_places=2 )
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product_Name