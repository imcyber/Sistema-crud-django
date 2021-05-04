from django.db import models


class Product(models.Model):
    Descrição = models.CharField(max_length=100)
    Preço = models.DecimalField(max_digits=9, decimal_places=2)
    Quantia = models.IntegerField()

    def __str__(self):
        return self.Descrição
