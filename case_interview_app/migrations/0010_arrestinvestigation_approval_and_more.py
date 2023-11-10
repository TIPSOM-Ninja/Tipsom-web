# Generated by Django 4.2.7 on 2023-11-10 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0009_arrestinvestigation_org_crime"),
    ]

    operations = [
        migrations.AddField(
            model_name="arrestinvestigation",
            name="approval",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="investigations",
                to="case_interview_app.approvalstatus",
            ),
        ),
        migrations.AddField(
            model_name="arrestinvestigation",
            name="approval_comments",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="arrestinvestigation",
            name="interviewer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="investigations",
                to="case_interview_app.interviewer",
            ),
        ),
    ]
