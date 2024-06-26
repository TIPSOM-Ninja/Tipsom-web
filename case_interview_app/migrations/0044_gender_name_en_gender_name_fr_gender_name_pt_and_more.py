# Generated by Django 4.2.7 on 2024-01-02 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0043_alter_interviewer_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="gender",
            name="name_en",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="gender",
            name="name_fr",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="gender",
            name="name_pt",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="language",
            name="name_en",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="language",
            name="name_fr",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="language",
            name="name_pt",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="race",
            name="name_en",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="race",
            name="name_fr",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="race",
            name="name_pt",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
