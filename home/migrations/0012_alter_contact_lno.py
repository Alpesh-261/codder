# Generated by Django 4.2.2 on 2023-07-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_contact_lno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='lno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
