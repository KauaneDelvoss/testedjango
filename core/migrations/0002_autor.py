# Generated by Django 4.0.5 on 2022-07-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=225)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
