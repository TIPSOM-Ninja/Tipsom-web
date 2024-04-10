# Generated by Django 4.2.7 on 2024-04-10 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0054_sommultivictimprofile_victimquestions_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="somarrestinvestigation",
            name="victim",
        ),
        migrations.RemoveField(
            model_name="somassistance",
            name="victim",
        ),
        migrations.RemoveField(
            model_name="somprosecution",
            name="victim",
        ),
        migrations.RemoveField(
            model_name="somsuspectedtrafficker",
            name="victim",
        ),
        migrations.RemoveField(
            model_name="somtransitroutedestination",
            name="victim",
        ),
        migrations.AddField(
            model_name="somarrestinvestigation",
            name="case",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="som_investigations",
                to="case_interview_app.somcase",
            ),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="case",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="som_assistance",
                to="case_interview_app.somcase",
            ),
        ),
        migrations.AddField(
            model_name="somprosecution",
            name="case",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="som_prosecutions",
                to="case_interview_app.somcase",
            ),
        ),
        migrations.AddField(
            model_name="somsocioeconomic",
            name="case",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="som_socio_economic",
                to="case_interview_app.somcase",
            ),
        ),
        migrations.AddField(
            model_name="somsuspectedtrafficker",
            name="case",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="som_traffickers",
                to="case_interview_app.somcase",
            ),
        ),
        migrations.AddField(
            model_name="somtransitroutedestination",
            name="case",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="som_transit",
                to="case_interview_app.somcase",
            ),
        ),
    ]
