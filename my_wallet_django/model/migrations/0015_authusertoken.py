# Generated by Django 4.0.6 on 2022-08-06 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0014_photoandvideo_memo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUserToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token', models.TextField()),
                ('expires_in', models.DateTimeField()),
            ],
        ),
    ]
