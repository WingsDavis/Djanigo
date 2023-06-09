# Generated by Django 4.2.2 on 2023-06-11 05:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_credential"),
    ]

    operations = [
        migrations.AddField(
            model_name="credential",
            name="email",
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="credential",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="credential",
            name="name",
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
