# Generated by Django 4.2.7 on 2023-11-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0013_suspectedtrafficker_approval_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="country",
            name="flag",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]