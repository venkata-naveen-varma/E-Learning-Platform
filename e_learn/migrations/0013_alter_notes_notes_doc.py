# Generated by Django 4.2.1 on 2023-06-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_learn', '0012_assignment_grade_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='notes_doc',
            field=models.FileField(upload_to='notes<django.db.models.fields.related.ForeignKey>'),
        ),
    ]
