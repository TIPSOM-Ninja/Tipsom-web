# Generated by Django 4.2.7 on 2023-11-10 00:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0010_arrestinvestigation_approval_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="arrestinvestigation",
            name="trafficker",
        ),
    ]