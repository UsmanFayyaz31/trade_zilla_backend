# Generated by Django 3.2.2 on 2022-06-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adpost',
            name='product_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
