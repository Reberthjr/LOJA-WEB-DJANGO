# Generated by Django 5.0.2 on 2024-02-06 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0015_order_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cmerc_id',
            new_name='payment_intent',
        ),
    ]