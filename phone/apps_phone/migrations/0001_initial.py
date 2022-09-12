# Generated by Django 4.1 on 2022-08-27 18:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=255)),
                ('phone_value', phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number', max_length=128, region=None, unique=True)),
            ],
        ),
    ]