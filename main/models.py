from django.db import models
from .choice import FactoryChoice, ConstructiveChoice, CustomUserRoleChoice, MarkConcreteChoice, ObjectNameChoice


class Registration(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    phone = models.IntegerField('Телефон номер', unique=True)
    sms = models.IntegerField('введите СМС')
    object = models.CharField('Объект', choices=ObjectNameChoice.choices, max_length=20, null=True)
    job = models.CharField('Должность', choices=CustomUserRoleChoice.choices, max_length=22, null=True)

    def __str__(self):
        return str(self.surname) + " " + str(self.name)

    def lo(self):
        return str(self.object)


class SaveConcrete(models.Model):
    data = models.DateField('Дата заполнение', max_length=20)
    factory_name = models.CharField('Название завода', choices=FactoryChoice.choices, max_length=50)
    object_name = models.CharField('Объект',  max_length=50)
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







