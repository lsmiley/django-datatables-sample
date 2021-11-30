# Generated by Django 2.2.10 on 2021-11-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodvendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorname', models.CharField(max_length=150, unique=True)),
                ('vendorcodename', models.CharField(blank=True, max_length=150, null=True)),
                ('vendorcategory', models.CharField(blank=True, max_length=150, null=True)),
                ('numvendorproducts', models.CharField(blank=True, default='0', max_length=150, null=True)),
                ('vendornote', models.CharField(blank=True, max_length=150, null=True)),
                ('vendorweburl', models.CharField(blank=True, max_length=150, null=True)),
                ('contact1name', models.CharField(blank=True, max_length=150, null=True)),
                ('contact1phone', models.CharField(blank=True, max_length=150, null=True)),
                ('contact1email', models.CharField(blank=True, max_length=150, null=True)),
                ('contact2name', models.CharField(blank=True, max_length=150, null=True)),
                ('contact2phone', models.CharField(blank=True, max_length=150, null=True)),
                ('contact2email', models.CharField(blank=True, max_length=150, null=True)),
                ('contractnum', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'ordering': ('vendorname',),
            },
        ),
    ]
