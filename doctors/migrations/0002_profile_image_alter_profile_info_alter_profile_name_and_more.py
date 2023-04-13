# Generated by Django 4.2 on 2023-04-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='profile', verbose_name='الصورة الشخصيه'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='info',
            field=models.TextField(verbose_name='معلومات عن الدكتور'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(verbose_name='السعر'),
        ),
    ]
