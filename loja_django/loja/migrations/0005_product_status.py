# Generated by Django 5.0.1 on 2024-01-31 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('sketh', 'sketh'), ('waiting for approval', 'waiting for approval'), ('active', 'activated'), ('deleted', 'deleted')], default='active', max_length=50),
        ),
    ]
