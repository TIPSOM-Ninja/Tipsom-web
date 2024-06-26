# Generated by Django 4.2.7 on 2023-11-08 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0004_interviewer_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApprovalStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="interviewer",
            name="approval_comments",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="interviewer",
            name="approval",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="interviewers",
                to="case_interview_app.approvalstatus",
            ),
        ),
    ]
