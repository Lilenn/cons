# Generated by Django 2.1.1 on 2018-09-11 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(null=True)),
                ('sex', models.NullBooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('code', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myApp.People')),
            ],
        ),
    ]