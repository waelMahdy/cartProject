# Generated by Django 3.1 on 2024-04-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payer_email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='payer_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
