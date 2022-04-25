from django.db import models


class Zakaz(models.Model):
    title = models.TextField(max_length=150, verbose_name='Наименование')
    cost = models.CharField(max_length=150, verbose_name='Цена')
    cost_sale = models.CharField(max_length=150, verbose_name='Цена по скидке')
    desc = models.TextField(max_length=150, verbose_name='Описание')
    img = models.ImageField(verbose_name='Картинка',upload_to="photos/product",blank=True)
    is_published = models.BooleanField(default=True, blank=True, verbose_name='Опубликован?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
