# Generated by Django 4.0.6 on 2022-08-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0013_alter_configuration_name_alter_configuration_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoandvideo',
            name='memo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
