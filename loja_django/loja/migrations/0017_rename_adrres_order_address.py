# Generated by Django 3.2.12 on 2024-02-21 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0016_rename_cmerc_id_order_payment_intent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adrres',
            new_name='address',
        ),
    ]
