# Generated by Django 4.2.7 on 2024-05-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "case_interview_app",
            "0056_somcase_interview_country_somcase_interview_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="interviewer",
            name="som_multi_victims",
            field=models.ManyToManyField(
                blank=True, null=True, to="case_interview_app.sommultivictimprofile"
            ),
        ),
    ]