# Generated by Django 4.1.3 on 2022-12-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saveconcreate',
            options={'verbose_name': 'Таблица бетона', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterField(
            model_name='saveconcreate',
            name='object_name',
            field=models.CharField(max_length=50, verbose_name='Название объекта'),
        ),
    ]