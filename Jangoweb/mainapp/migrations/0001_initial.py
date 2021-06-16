# Generated by Django 3.2.3 on 2021-06-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namecode1', models.CharField(max_length=300)),
                ('namecode2', models.CharField(max_length=300)),
                ('align_sequence', models.TextField(null=True)),
                ('image', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('namecode', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('sequence', models.TextField()),
            ],
        ),
    ]