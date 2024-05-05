# Generated by Django 4.2.7 on 2024-05-05 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0057_interviewer_som_multi_victims"),
    ]

    operations = [
        migrations.AddField(
            model_name="somarrestinvestigation",
            name="national_legislation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="som_investigations",
                to="case_interview_app.country",
            ),
        ),
    ]
