# Generated by Django 4.2.7 on 2023-11-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
