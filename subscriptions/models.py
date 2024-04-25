from django.db import models

class Packets(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name="Цена")
    duration = models.IntegerField(default=0, verbose_name='Продолжительность')

    class Meta:
        db_table = 'subscriptions'
        verbose_name = 'subscription'
        verbose_name_plural = 'subscriptions'
    def __str__(self):
        return self.name

# class UserSubscriptions(models.Model):
#     user_id = models.IntegerField()
#     subscription_id = models.IntegerField()
#     start_date = models.DateField()
#     end_date = models.DateField()

#     class Meta:
#         db_table = 'user_subscriptions'
#         verbose_name = 'user subscription'
#         verbose_name_plural = 'user subscriptions'
#     def __str__(self):
#         return self.user_id