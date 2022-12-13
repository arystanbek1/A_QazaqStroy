from django.db import models
from .choice import FactoryChoice, ConstructiveChoice, CustomUserRoleChoice, MarkConcreteChoice, ObjectNameChoice


class Registration(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    object = models.ForeignKey('Object', verbose_name='Название объекта', on_delete=models.CASCADE)
    phone = models.IntegerField('Телефон номер', unique=True)
    sms = models.IntegerField('введите СМС')
    job = models.CharField('Должность', choices=CustomUserRoleChoice.choices, max_length=22, null=True)

    def __str__(self):
        return str(self.surname) + " " + str(self.name)


class Object(models.Model):
    object_name = models.CharField('Название объекта', choices=ObjectNameChoice.choices, max_length=30, null=True)

    def __str__(self):
        return self.object_name


class SaveConcrete(models.Model):
    data = models.DateField('Дата заполнение', max_length=20)
    factory_name = models.CharField('Название завода', choices=FactoryChoice.choices, max_length=50)
    object_name = models.ForeignKey('Object', verbose_name='Название объекта', on_delete=models.CASCADE)
    block = models.IntegerField('блок')
    mark = models.CharField('Марка бетона', choices=MarkConcreteChoice.choices, max_length=50)
    constructive = models.CharField('Конструктив', choices=ConstructiveChoice.choices, max_length=50)
    floor = models.IntegerField('Этаж')
    fact_concrete = models.IntegerField('Факт')
    sum_concrete = models.IntegerField('Итого залито')
    accepted = models.ForeignKey('Registration', verbose_name='Принял', on_delete=models.CASCADE)

    def __int__(self):
        return self.data

    class Meta:
        verbose_name = 'Таблица бетона'
        verbose_name_plural = 'Записи'

    def get_absolute_url(self):
        return f'/{self.id}'


class Block(models.Model):
    object = models.ForeignKey('Object', verbose_name='Объект', on_delete=models.CASCADE)
    name_block = models.CharField('Название блока', max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        return self.name_block


class Floor(models.Model):
    object = models.ForeignKey('Object', verbose_name='Объект', on_delete=models.CASCADE)
    block = models.ForeignKey('Block', verbose_name='Блок', on_delete=models.CASCADE)
    floor = models.CharField('Этаж', max_length=10)

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'

    def __str__(self):
        return self.floor






