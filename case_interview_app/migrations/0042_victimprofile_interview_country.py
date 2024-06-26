# Generated by Django 4.2.7 on 2023-11-28 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0041_country_is_sadc"),
    ]

    operations = [
        migrations.AddField(
            model_name="victimprofile",
            name="interview_country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="victim_interview_country",
                to="case_interview_app.country",
            ),
        ),
    ]
