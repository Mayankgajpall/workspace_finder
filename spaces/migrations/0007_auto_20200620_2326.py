# Generated by Django 3.0.6 on 2020-06-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0006_auto_20200613_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspaces',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
