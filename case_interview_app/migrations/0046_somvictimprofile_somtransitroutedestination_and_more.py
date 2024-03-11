# Generated by Django 4.2.7 on 2024-03-11 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "case_interview_app",
            "0045_accesspermission_name_en_accesspermission_name_fr_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="SomVictimProfile",
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
                ("victim_identifier", models.CharField(blank=True, null=True)),
                (
                    "place_of_birth",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "identification_number",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("initials", models.CharField(blank=True, max_length=50, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("address", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "email_address",
                    models.EmailField(blank=True, max_length=150, null=True),
                ),
                (
                    "interview_location",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("interview_date", models.DateField(blank=True, null=True)),
                ("additional_remarks", models.TextField(blank=True, null=True)),
                (
                    "consent_share_gov_patner",
                    models.BooleanField(blank=True, null=True),
                ),
                (
                    "consent_limited_disclosure",
                    models.BooleanField(blank=True, null=True),
                ),
                ("consent_research", models.BooleanField(blank=True, null=True)),
                ("consent_abstain_answer", models.BooleanField(blank=True, null=True)),
                ("approval_comments", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "approval",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_victimprofile",
                        to="case_interview_app.approvalstatus",
                    ),
                ),
                (
                    "citizenship",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_victims_cit",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "countryOfBirth",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_victims_country",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_victims",
                        to="case_interview_app.gender",
                    ),
                ),
                (
                    "identification_type",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_victims",
                        to="case_interview_app.idtype",
                    ),
                ),
                (
                    "interview_country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_victim_interview_country",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "languages",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_victims_lang",
                        to="case_interview_app.language",
                    ),
                ),
                (
                    "last_place_of_residence",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_victims_last_place",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "race",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_victims",
                        to="case_interview_app.race",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SomTransitRouteDestination",
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
                (
                    "city_village_of_dest",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "city_village_of_origin",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("remarks", models.TextField(blank=True, null=True)),
                ("approval_comments", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "approval",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_destinations",
                        to="case_interview_app.approvalstatus",
                    ),
                ),
                (
                    "country_of_dest",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_dest_destinations",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "country_of_origin",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_origin_destinations",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "interviewer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_destinations",
                        to="case_interview_app.interviewer",
                    ),
                ),
                (
                    "transport_means",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_transit",
                        to="case_interview_app.transportmean",
                    ),
                ),
                (
                    "victim",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_destinations",
                        to="case_interview_app.somvictimprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SomSuspectedTrafficker",
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
                ("first_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(blank=True, max_length=50, null=True)),
                ("dob", models.DateField(blank=True, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("id_number", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "last_residence",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("address", models.CharField(blank=True, max_length=50, null=True)),
                ("approval_comments", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "approval",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_traffickers",
                        to="case_interview_app.approvalstatus",
                    ),
                ),
                (
                    "citizenship",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_cit_traffickers",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "country_of_birth",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_traffickers",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_traffickers",
                        to="case_interview_app.gender",
                    ),
                ),
                (
                    "id_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_traffickers",
                        to="case_interview_app.idtype",
                    ),
                ),
                (
                    "interviewer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_traffickers",
                        to="case_interview_app.interviewer",
                    ),
                ),
                (
                    "languages",
                    models.ManyToManyField(
                        blank=True, null=True, to="case_interview_app.language"
                    ),
                ),
                (
                    "nationality",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_nat_traffickers",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "race",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_traffickers",
                        to="case_interview_app.race",
                    ),
                ),
                (
                    "victim",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_traffickers",
                        to="case_interview_app.somvictimprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SomSocioEconomic",
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
                ("violence_prior", models.BooleanField(blank=True, null=True)),
                (
                    "violence_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("approval_comments", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "approval",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_socio_economic",
                        to="case_interview_app.approvalstatus",
                    ),
                ),
                (
                    "education_level",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_socio_economic",
                        to="case_interview_app.educationlevel",
                    ),
                ),
                (
                    "family_structure",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_socio_economic",
                        to="case_interview_app.familystructure",
                    ),
                ),
                (
                    "interviewer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_socio_economic",
                        to="case_interview_app.interviewer",
                    ),
                ),
                (
                    "last_occupation",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_socio_economic",
                        to="case_interview_app.occupation",
                    ),
                ),
                (
                    "living_with",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_socio_economic",
                        to="case_interview_app.livingwith",
                    ),
                ),
                (
                    "victim",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_socio_economic",
                        to="case_interview_app.somvictimprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SomProsecution",
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
                (
                    "court_case_no",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("guilty_verdict", models.BooleanField(blank=True, null=True)),
                (
                    "review_appeal_outcome",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("years_imposed", models.IntegerField(blank=True, null=True)),
                ("approval_comments", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "approval",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.approvalstatus",
                    ),
                ),
                (
                    "aquital_reason",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.aquitalreason",
                    ),
                ),
                (
                    "guilty_verdict_reason",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.guiltyreason",
                    ),
                ),
                (
                    "interviewer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.interviewer",
                    ),
                ),
                (
                    "prosecution_outcome",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.prosecutionoutcome",
                    ),
                ),
                (
                    "sanction_penalty",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.sanctionpenalty",
                    ),
                ),
                (
                    "status_of_case",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.casestatus",
                    ),
                ),
                (
                    "trafficker",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.somsuspectedtrafficker",
                    ),
                ),
                (
                    "trial_court",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.trialcourt",
                    ),
                ),
                (
                    "trial_court_country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "verdict",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.verdict",
                    ),
                ),
                (
                    "victim",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_prosecutions",
                        to="case_interview_app.somvictimprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SomCase",
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
                ("date_of_arrest", models.DateField(blank=True, null=True)),
                (
                    "traffick_from_place",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "traffick_to_place",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("approval_comments", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "approval",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cases",
                        to="case_interview_app.approvalstatus",
                    ),
                ),
                (
                    "interviewer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cases",
                        to="case_interview_app.interviewer",
                    ),
                ),
                (
                    "role_in_trafficking",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="cases",
                        to="case_interview_app.roleintrafficking",
                    ),
                ),
                (
                    "traffick_from_country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="from_cases",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "traffick_to_country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_cases",
                        to="case_interview_app.country",
                    ),
                ),
                (
                    "victim",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cases",
                        to="case_interview_app.somvictimprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SomAssistance",
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
                ("approval_comments", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "approval",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_assistance",
                        to="case_interview_app.approvalstatus",
                    ),
                ),
                (
                    "education_assistance_level",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_education_assistance",
                        to="case_interview_app.educationlevel",
                    ),
                ),
                (
                    "education_assistance_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_education_assistance",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "financial_assistance_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_financial_assistance",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "halfway_house_providers",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_halfway_house",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "housing_allowance_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_housing_allowance",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "im_emmigration_assistance_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_im_emmigration_assistance",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "im_emmigration_assistance_status",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_im_emmigration_assistance",
                        to="case_interview_app.imemmigrationstatus",
                    ),
                ),
                (
                    "interviewer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_assistance",
                        to="case_interview_app.interviewer",
                    ),
                ),
                (
                    "legal_assistance_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_legal_assistance",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "med_rehab_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_med_rehab",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "medical_assistance_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_medical_assistance",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "micro_ent_income_project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_micro_ent_income",
                        to="case_interview_app.incomeprojecttype",
                    ),
                ),
                (
                    "micro_ent_income_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_micro_ent_income",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "other_community_assistance_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_other_community_assistance",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "other_community_assistance_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_other_community_assistance",
                        to="case_interview_app.communityassistancetype",
                    ),
                ),
                (
                    "shelter_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_shelter",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "social_assistance_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_social_assistance",
                        to="case_interview_app.provider",
                    ),
                ),
                (
                    "victim",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_assistance",
                        to="case_interview_app.somvictimprofile",
                    ),
                ),
                (
                    "vocational_training_provider",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_vocational_training",
                        to="case_interview_app.provider",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SomArrestInvestigation",
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
                ("org_crime", models.BooleanField(blank=True, null=True)),
                ("suspects_arrested", models.BooleanField(blank=True, null=True)),
                ("why_no_arrest", models.TextField(blank=True, null=True)),
                ("victim_smuggled", models.BooleanField(blank=True, null=True)),
                ("investigation_done", models.BooleanField(blank=True, null=True)),
                ("why_no_investigation", models.TextField(blank=True, null=True)),
                ("why_pending", models.TextField(blank=True, null=True)),
                ("withdrawn_closed_reason", models.TextField(blank=True, null=True)),
                ("approval_comments", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "approval",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_investigations",
                        to="case_interview_app.approvalstatus",
                    ),
                ),
                (
                    "how_traffickers_org",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="som_investigations",
                        to="case_interview_app.traffickerorg",
                    ),
                ),
                (
                    "interviewer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_investigations",
                        to="case_interview_app.interviewer",
                    ),
                ),
                (
                    "investigation_status",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_investigations",
                        to="case_interview_app.investigationstatus",
                    ),
                ),
                (
                    "victim",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="som_investigations",
                        to="case_interview_app.somvictimprofile",
                    ),
                ),
            ],
        ),
    ]
