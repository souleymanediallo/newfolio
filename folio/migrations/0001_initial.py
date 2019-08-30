# Generated by Django 2.2.4 on 2019-08-30 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='folio.jpg', upload_to='images_pic')),
                ('description', models.TextField()),
            ],
        ),
    ]