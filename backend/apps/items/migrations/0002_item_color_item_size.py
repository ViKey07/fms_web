# Generated by Django 4.2 on 2023-04-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(blank=True, choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green')], max_length=10, null=True, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1, null=True, verbose_name='Size'),
        ),
    ]
