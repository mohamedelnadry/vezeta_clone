# Generated by Django 4.2 on 2023-04-13 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_profile_slug_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='السعر'),
        ),
    ]