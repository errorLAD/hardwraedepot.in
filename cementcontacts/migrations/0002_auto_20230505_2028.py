# Generated by Django 3.1.13 on 2023-05-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cementcontacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactcement',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
