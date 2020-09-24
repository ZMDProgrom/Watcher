# Generated by Django 3.0.8 on 2020-08-04 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dns_finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dnsmonitored',
            options={'ordering': ['domain_name'], 'verbose_name': 'Monitored DNS'},
        ),
        migrations.AlterModelOptions(
            name='dnstwisted',
            options={'ordering': ['-created_at'], 'verbose_name': 'Twisted DNS'},
        ),
    ]