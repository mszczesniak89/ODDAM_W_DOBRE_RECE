# Generated by Django 3.2.9 on 2021-11-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('type', models.IntegerField(choices=[(1, 'Fundacja'), (3, 'Zbiórka lokalna'), (2, 'Organizacja pozarządowa')], default=1)),
                ('categories', models.ManyToManyField(to='main.Category')),
            ],
        ),
    ]
