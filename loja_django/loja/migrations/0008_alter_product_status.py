# Generated by Django 5.0.1 on 2024-01-31 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Sketh', 'Sketh'), ('Waiting for approval', 'Waiting for approval'), ('Active', 'Activated'), ('Disabla', 'Disable'), ('Deleted', 'Deleted')], default='Active', max_length=50),
        ),
    ]
