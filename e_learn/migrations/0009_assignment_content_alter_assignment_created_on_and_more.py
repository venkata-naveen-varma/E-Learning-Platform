# Generated by Django 4.2.1 on 2023-06-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_learn', '0008_usercourserelation_is_instructor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
