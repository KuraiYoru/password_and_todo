# Generated by Django 4.1 on 2022-08-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
