# Generated by Django 3.1.5 on 2021-04-26 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictive_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='selected_stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('stock_symbol', models.CharField(max_length=100)),
            ],
        ),
    ]
