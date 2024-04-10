from django.db import models

class Packets(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='Описание')
    data = models.DateTimeField(verbose_name="DataTime")
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name="Цена")

    class Meta:
        db_table = 'subscriptions'
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'
    def __str__(self):
        return self.name

