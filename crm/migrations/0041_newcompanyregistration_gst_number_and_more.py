# Generated by Django 5.0.4 on 2024-10-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0040_alter_arivaltable_amt_recev'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcompanyregistration',
            name='gst_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='newcompanyregistration',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
