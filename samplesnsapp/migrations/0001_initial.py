# Generated by Django 4.2.1 on 2023-06-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('poster', models.CharField(max_length=100)),
                ('sns_image', models.ImageField(upload_to='')),
                ('good', models.IntegerField()),
                ('read', models.IntegerField()),
                ('read_text', models.TextField()),
            ],
        ),
    ]