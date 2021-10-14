# Generated by Django 3.2.8 on 2021-10-14 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('data', models.DateTimeField(verbose_name='Даьа')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
            ],
        ),
    ]
