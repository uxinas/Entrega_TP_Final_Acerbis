# Generated by Django 4.2.2 on 2023-07-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
    ]