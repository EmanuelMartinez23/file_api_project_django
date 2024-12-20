# Generated by Django 5.1.4 on 2024-12-20 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='archivos/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]