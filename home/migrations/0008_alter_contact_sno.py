# Generated by Django 4.2.2 on 2023-07-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_contact_content_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sno',
            field=models.AutoField(default=int, primary_key=True, serialize=False),
        ),
    ]
