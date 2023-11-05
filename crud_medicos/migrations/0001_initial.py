# Generated by Django 4.2.6 on 2023-11-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
                ('E_mail', models.CharField(max_length=100)),
                ('Senha', models.CharField(max_length=100)),
                ('Data_de_Criacao', models.DateTimeField()),
            ],
        ),
    ]