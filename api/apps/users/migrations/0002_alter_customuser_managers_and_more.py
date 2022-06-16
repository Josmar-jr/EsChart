# Generated by Django 4.0.5 on 2022-06-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=120, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=14, unique=True, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/user'),
        ),
    ]
