# Generated by Django 4.2.7 on 2023-11-15 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0016_accesspermission_victimpermissions"),
    ]

    operations = [
        migrations.AddField(
            model_name="prosecution",
            name="verdict",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prosecutions",
                to="case_interview_app.verdict",
            ),
        ),
    ]
