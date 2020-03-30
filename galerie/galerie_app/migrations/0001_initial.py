# Generated by Django 3.0.4 on 2020-03-30 10:44

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('nom', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
                ('nb_telechargement', models.IntegerField()),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
