# Generated by Django 4.2 on 2023-05-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adressuser',
            name='adress',
            field=models.TextField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='adressuser',
            name='city',
            field=models.CharField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adressuser',
            name='code_postal',
            field=models.CharField(default=2, max_length=34, unique=True),
            preserve_default=False,
        ),
    ]
