# Generated by Django 5.1.3 on 2025-02-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.TextField(default='pending'),
        ),
    ]
