# Generated by Django 4.2.7 on 2024-03-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "case_interview_app",
            "0047_remove_somtransitroutedestination_city_village_of_dest_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="somassistance",
            name="education_assistance",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="financial_assistance",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="halfway_house",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="housing_allowance",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="im_emmigration_assistance",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="legal_assistance",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="med_rehab",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="medical_assistance",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="micro_ent_income",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="other_community_assistance",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="shelter",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="social_assistance",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="somassistance",
            name="vocational_training",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
