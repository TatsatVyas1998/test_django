# Generated by Django 3.1.5 on 2021-04-02 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_movers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='get_topmovers',
            name='prc_change',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='get_topmovers',
            name='vol',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]