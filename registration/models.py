from django.conf import settings
from django.db import models

class MyModel(models.Model):
    # Добавьте другие поля здесь, если они вам нужны
    name = models.CharField(max_length=100)  # Пример дополнительного поля

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,  # Ссылка на пользовательскую модель
        on_delete=models.CASCADE,     # Удалить связанные записи при удалении пользователя
        verbose_name='Пользователь'
    )
