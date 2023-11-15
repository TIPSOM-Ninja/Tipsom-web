# Generated by Django 4.2.7 on 2023-11-10 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "case_interview_app",
            "0012_remove_arrestinvestigation_how_traffickers_org_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="suspectedtrafficker",
            name="approval",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="traffickers",
                to="case_interview_app.approvalstatus",
            ),
        ),
        migrations.AddField(
            model_name="suspectedtrafficker",
            name="approval_comments",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="suspectedtrafficker",
            name="interviewer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="traffickers",
                to="case_interview_app.interviewer",
            ),
        ),
    ]