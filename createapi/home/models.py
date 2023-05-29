from django.db import models

class Product(models.Model):
    pname=models.CharField(max_length=20)
    pcode=models.IntegerField()
    price=models.IntegerField()
    def __str__(self) -> str:
        return self.pname
