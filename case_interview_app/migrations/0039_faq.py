# Generated by Django 4.2.7 on 2023-11-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0038_search_data_entry_purpose"),
    ]

    operations = [
        migrations.CreateModel(
            name="Faq",
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
                ("question", models.CharField(blank=True, null=True)),
                ("answer", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
