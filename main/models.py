from django.db import models


class SaveConcreate(models.Model):
    data = models.DateField('Дата заполнение', max_length=20)
    factory_name = models.CharField('Название завода', max_length=50)
    object_name = models.CharField('Название объекта', max_length=50)
    block = models.IntegerField('блок')
    mark = models.CharField('Марка бетона', max_length=50)
    constructive = models.CharField('Конструктив', max_length=50)
    floor = models.IntegerField('Этаж')
    fact_concrete = models.IntegerField('Факт')
    sum_concrete = models.IntegerField('Итого залито')
    accepted = models.CharField('Кто принимал', max_length=100)

    def __int__(self):
        return self.data

    class Meta:
        verbose_name = 'Таблица бетона'
        verbose_name_plural = 'Записи'

    def get_absolute_url(self):
        return f'/{self.id}'


