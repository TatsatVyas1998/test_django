# Generated by Django 3.1.5 on 2021-04-26 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictive_models', '0002_selected_stocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='created_portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_symbol', models.CharField(max_length=200)),
                ('port_weight_opt', models.CharField(max_length=200)),
            ],
        ),
    ]
