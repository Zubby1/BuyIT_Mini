# Generated by Django 2.0.3 on 2018-03-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_caption',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
