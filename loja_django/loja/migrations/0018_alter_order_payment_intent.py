# Generated by Django 3.2.12 on 2024-02-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0017_rename_adrres_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
