# Generated by Django 3.2.6 on 2021-08-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0005_alter_emailtemplate_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtemplate',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Имя шаблона'),
        ),
    ]
