# Generated by Django 4.0.6 on 2022-08-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dcmodel',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=10),
        ),
    ]