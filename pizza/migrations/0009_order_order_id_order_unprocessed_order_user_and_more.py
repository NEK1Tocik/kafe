# Generated by Django 4.2.4 on 2023-12-21 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0008_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(auto_created=True, default=0, unique=True, verbose_name='номер заказа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='unprocessed',
            field=models.BooleanField(default=True, verbose_name='необработан'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.order')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.pizzaitem')),
            ],
        ),
    ]