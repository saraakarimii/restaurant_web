# Generated by Django 3.2.9 on 2022-01-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_costumuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumuser',
            name='device',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
