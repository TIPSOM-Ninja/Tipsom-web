# Generated by Django 4.2.7 on 2023-11-18 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0029_assistance_halfway_house_days"),
    ]

    operations = [
        migrations.AddField(
            model_name="assistance",
            name="halfway_house_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="assistance",
            name="halfway_house_providers",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="halfway_house",
                to="case_interview_app.provider",
            ),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="education_assistance_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="education_assistance_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="financial_assistance_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="financial_assistance_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name="assistance",
            name="halfway_house_days",
        ),
        migrations.AlterField(
            model_name="assistance",
            name="housing_allowance_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="housing_allowance_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="im_emmigration_assistance_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="im_emmigration_assistance_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="legal_assistance_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="legal_assistance_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="med_rehab_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="med_rehab_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="medical_assistance_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="medical_assistance_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="micro_ent_income_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="micro_ent_income_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="other_community_assistance_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="other_community_assistance_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="shelter_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="shelter_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="social_assistance_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="social_assistance_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="vocational_training_days",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="assistance",
            name="vocational_training_months",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="assistance",
            name="halfway_house_days",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
