# Generated by Django 4.1.4 on 2023-01-11 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ah', '0003_case_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='case_user_id', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]