# Generated by Django 5.0.1 on 2024-01-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_note_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='back_img',
            field=models.ImageField(upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='note',
            name='front_img',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
