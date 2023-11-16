# Generated by Django 4.2.7 on 2023-11-16 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("case_interview_app", "0019_alter_victimpermissions_victim_exploitation"),
    ]

    operations = [
        migrations.CreateModel(
            name="AffirmOption",
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
        migrations.CreateModel(
            name="BodyPart",
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
        migrations.CreateModel(
            name="BridePrice",
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
        migrations.CreateModel(
            name="BridePriceRecipient",
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
        migrations.CreateModel(
            name="ChildMarriageReason",
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
        migrations.CreateModel(
            name="CriminalActivityType",
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
        migrations.CreateModel(
            name="ExploitationAge",
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
        migrations.CreateModel(
            name="ForcedLabourIndustry",
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
        migrations.CreateModel(
            name="FreedMethod",
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
        migrations.CreateModel(
            name="MarriageViolenceType",
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
        migrations.CreateModel(
            name="MilitaryActivity",
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
        migrations.CreateModel(
            name="MilitaryType",
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
        migrations.CreateModel(
            name="OperationLocation",
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
        migrations.CreateModel(
            name="OrganPaidTo",
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
        migrations.CreateModel(
            name="RecruiterRelationship",
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
        migrations.CreateModel(
            name="RecruitmentType",
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
        migrations.CreateModel(
            name="TraffickingMean",
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
            model_name="exploitation",
            name="debt_amount",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_armed_group_name",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_bprice_amount_kind",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_child_marriage",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_child_soldier",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_child_soldier_age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_children_from_marriage",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_criminal_activity",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_forced_labour",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_forced_marriage",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_m_health_issues_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_maternal_health_issues",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_online_porno",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_operation_country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation_operation_country",
                to="case_interview_app.country",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_organ_removed",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_organ_sale_price",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_other_sexual",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_other_sexual_online",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_prostitution",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_remarks",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_spouse_nationality",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation_spouse_nationality",
                to="case_interview_app.country",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_victim_knew_spouse",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_victim_pregnancy",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="event_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="exploitation_length",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="intent_to_exploit",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="pay_debt",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="subject_to_exploitation",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_body_part_removed",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="exploitation",
                to="case_interview_app.bodypart",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_bprice_paid",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation",
                to="case_interview_app.brideprice",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_brice_recipient",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="exploitation",
                to="case_interview_app.bridepricerecipient",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_child_marriage_reason",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="exploitation",
                to="case_interview_app.childmarriagereason",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_criminal_activity_type",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="exploitation",
                to="case_interview_app.criminalactivitytype",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_forced_labour_industry",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="exploitation",
                to="case_interview_app.forcedlabourindustry",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_forced_military_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation",
                to="case_interview_app.militarytype",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_marriage_violence",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation",
                to="case_interview_app.affirmoption",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_marriage_violence_type",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="exploitation",
                to="case_interview_app.marriageviolencetype",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_operation_location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation",
                to="case_interview_app.operationlocation",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_organ_paid_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation",
                to="case_interview_app.organpaidto",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_recruiter_relationship",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation",
                to="case_interview_app.recruiterrelationship",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_recruitment_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation",
                to="case_interview_app.recruitmenttype",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_trafficking_means",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="exploitation",
                to="case_interview_app.traffickingmean",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="e_victim_military_activities",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="exploitation",
                to="case_interview_app.militaryactivity",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="exploitation_age",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation",
                to="case_interview_app.exploitationage",
            ),
        ),
        migrations.AddField(
            model_name="exploitation",
            name="freed_method",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exploitation",
                to="case_interview_app.freedmethod",
            ),
        ),
    ]
