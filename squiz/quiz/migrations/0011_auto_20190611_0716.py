# Generated by Django 2.2.2 on 2019-06-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20190611_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='selected_option',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
