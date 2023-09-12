# Generated by Django 4.2.4 on 2023-09-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='matn_email',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]