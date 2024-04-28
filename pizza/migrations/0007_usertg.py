# Generated by Django 4.2.4 on 2023-12-17 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0006_basketitem_readiness_alter_pizzaitem_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TG_id', models.TextField(default=None, verbose_name='телеграм ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]