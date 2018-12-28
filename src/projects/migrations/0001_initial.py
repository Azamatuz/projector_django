# Generated by Django 2.0.7 on 2018-12-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(blank=True, max_length=10)),
                ('institution', models.CharField(blank=True, max_length=100)),
                ('leader', models.CharField(blank=True, max_length=50)),
                ('fund', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField()),
                ('keywords', models.CharField(blank=True, max_length=200)),
                ('sector', models.CharField(blank=True, max_length=50)),
                ('discipline', models.CharField(blank=True, max_length=100)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
