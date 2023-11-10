# Generated by Django 4.2.7 on 2023-11-09 20:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0007_victimprofile_approval_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="victimprofile",
            name="languages",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="victims_lang",
                to="case_interview_app.language",
            ),
        ),
    ]
