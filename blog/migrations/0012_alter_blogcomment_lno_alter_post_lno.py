# Generated by Django 4.2.2 on 2023-07-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_blogcomment_lno_alter_post_lno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='lno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='lno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
