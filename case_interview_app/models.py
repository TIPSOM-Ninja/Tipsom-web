from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    flag = models.CharField(max_length=150, null=True, blank=True)
    two_code = models.CharField(max_length=2, null=True, blank=True)
    three_code = models.CharField(max_length=3, null=True, blank=True)
    is_sadc = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Gender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Race(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name}"


class IdType(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name}"


class DataEntryPurpose(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name}"


class InvestigationStatus(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name}"


class TraffickerOrg(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name}"


class RoleInTrafficking(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class CaseStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class TrialCourt(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class GuiltyReason(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class ProsecutionOutcome(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class AquitalReason(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class SanctionPenalty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class TransportMean(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Verdict(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class ApprovalStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class AccessPermission(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class ExploitationAge(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class FreedMethod(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class CriminalActivityType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class ForcedLabourIndustry(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class BridePrice(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class BridePriceRecipient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class ChildMarriageReason(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class AffirmOption(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class MarriageViolenceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class MilitaryType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class MilitaryActivity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class BodyPart(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class OperationLocation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class OrganPaidTo(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class RecruitmentType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class RecruiterRelationship(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class TraffickingMean(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Provider(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class IncomeProjectType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class EducationLevel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class ImEmmigrationStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class CommunityAssistanceType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class DataSupplier(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class FamilyStructure(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class LivingWith(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class Occupation(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
     
class VictimProfile(models.Model):
    victim_identifier = models.CharField(null=True,blank=True)
    citizenship = models.ForeignKey(
        Country, related_name = "victims_cit",  on_delete=models.CASCADE, null=True, blank=True
    )
    countryOfBirth = models.ForeignKey(
        Country, related_name = "victims_country",  on_delete=models.CASCADE, null=True, blank=True
    )
    languages = models.ManyToManyField(Language, related_name = "victims_lang", null=True, blank=True)
    gender = models.ForeignKey(Gender, related_name = "victims", on_delete=models.CASCADE, null=True, blank=True)
    race = models.ForeignKey(Race, related_name = "victims", on_delete=models.CASCADE, null=True, blank=True)
    identification_type = models.ManyToManyField(
        IdType, related_name = "victims", null=True, blank=True
    )
    place_of_birth = models.CharField(max_length=50, null=True, blank=True)
    last_place_of_residence = models.ForeignKey(
        Country, related_name = "victims_last_place", on_delete=models.CASCADE, null=True, blank=True
    )
    identification_number = models.CharField(max_length=50, null=True, blank=True)
    initials = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    email_address = models.EmailField(max_length=150, null=True, blank=True)
    interview_country = models.ForeignKey(
        Country, related_name = "victim_interview_country", on_delete=models.CASCADE, null=True, blank=True
    )
    interview_location = models.CharField(max_length=50, null=True, blank=True)
    interview_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    additional_remarks = models.TextField(null=True, blank=True)
    
    consent_share_gov_patner = models.BooleanField(null=True, blank=True)
    consent_limited_disclosure = models.BooleanField(null=True, blank=True)
    consent_research = models.BooleanField(null=True, blank=True)
    consent_abstain_answer = models.BooleanField(null=True, blank=True)

    approval = models.ForeignKey(
        ApprovalStatus, related_name = "victimprofile", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class Interviewer(models.Model):
    country = models.ForeignKey(
        Country, related_name = "interviewers", on_delete=models.CASCADE, null=True, blank=True
    )
    data_entry_purpose = models.ForeignKey(
        DataEntryPurpose, related_name = "interviewers", on_delete=models.CASCADE, null=True, blank=True
    )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=250, null=True, blank=True)
    organization = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    email_address = models.EmailField(max_length=254, null=True, blank=True)
    approval = models.ForeignKey(
        ApprovalStatus, related_name = "interviewers", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    victims = models.ManyToManyField(VictimProfile, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class TransitRouteDestination(models.Model):
    victim = models.ForeignKey(VictimProfile, related_name = "destinations", on_delete=models.CASCADE, null=True, blank=True)
    country_of_origin = models.ForeignKey(
        Country, related_name = "origin_destinations", on_delete=models.CASCADE, null=True, blank=True
    )
    city_village_of_dest = models.CharField(max_length=50, null=True, blank=True)
    city_village_of_origin = models.CharField(max_length=50, null=True, blank=True)
    country_of_dest = models.ForeignKey(
        Country, related_name = "dest_destinations", on_delete=models.CASCADE, null=True, blank=True
    )
    
    remarks = models.TextField(null=True, blank=True)
    transport_means = models.ManyToManyField(
        TransportMean, related_name = "transit", null=True, blank=True
    )
    interviewer = models.ForeignKey(Interviewer, related_name = "destinations", on_delete=models.CASCADE, null=True, blank=True)
    approval = models.ForeignKey(
        ApprovalStatus, related_name = "destinations", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class SuspectedTrafficker(models.Model):
    victim = models.ForeignKey(VictimProfile,  related_name = "traffickers",  on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    gender = models.ForeignKey(Gender, related_name = "traffickers",  on_delete=models.CASCADE, null=True, blank=True)
    race = models.ForeignKey(Race,  related_name = "traffickers", on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    country_of_birth = models.ForeignKey(
        Country,  related_name = "traffickers", on_delete=models.CASCADE, null=True, blank=True
    )
    citizenship = models.ForeignKey(
        Country,  related_name = "cit_traffickers", on_delete=models.CASCADE, null=True, blank=True
    )
    nationality = models.ForeignKey(
        Country,  related_name = "nat_traffickers", on_delete=models.CASCADE, null=True, blank=True
    )
    id_number = models.CharField(max_length=50,null=True, blank=True)
    id_type = models.ForeignKey(IdType,  related_name = "traffickers",  on_delete=models.CASCADE, null=True, blank=True)
    languages = models.ManyToManyField(Language, null=True, blank=True)
    last_residence = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    date_of_arrest = models.DateField(
        auto_now=False,   auto_now_add=False, null=True, blank=True
    )
    role_in_trafficking = models.ManyToManyField(
        RoleInTrafficking,  related_name = "traffickers",  null=True, blank=True
    )
    traffick_from_country = models.ForeignKey(
        Country,  related_name = "from_traffickers",  on_delete=models.CASCADE, null=True, blank=True
    )
    traffick_from_place = models.CharField(max_length=50, null=True, blank=True)
    traffick_to_country = models.ForeignKey(
        Country, related_name = "to_traffickers", on_delete=models.CASCADE, null=True, blank=True
    )
    traffick_to_place = models.CharField(null=True, blank=True, max_length=50)
    interviewer = models.ForeignKey(Interviewer, related_name = "traffickers", on_delete=models.CASCADE, null=True, blank=True)
    approval = models.ForeignKey(
        ApprovalStatus, related_name = "traffickers", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class ArrestInvestigation(models.Model):
    victim = models.ForeignKey(VictimProfile, related_name = "investigations", on_delete=models.CASCADE, null=True, blank=True)
    # clarify on trafficker
    # trafficker = models.ForeignKey(
    #     SuspectedTrafficker, related_name = "investigations",  on_delete=models.CASCADE, null=True, blank=True
    # )
    org_crime = models.BooleanField(null=True, blank=True)
    suspects_arrested = models.BooleanField(null=True, blank=True)
    why_no_arrest = models.TextField(null=True, blank=True)
    victim_smuggled = models.BooleanField(null=True, blank=True)
    how_traffickers_org = models.ManyToManyField(
        TraffickerOrg,  related_name = "investigations", null=True, blank=True
    )
    investigation_done = models.BooleanField(null=True, blank=True)
    why_no_investigation = models.TextField(null=True, blank=True)
    investigation_status = models.ForeignKey(
        InvestigationStatus, related_name = "investigations", on_delete=models.CASCADE, null=True, blank=True
    )
    why_pending = models.TextField(null=True, blank=True)
    withdrawn_closed_reason = models.TextField(null=True, blank=True)
    interviewer = models.ForeignKey(Interviewer, related_name = "investigations", on_delete=models.CASCADE, null=True, blank=True)
    approval = models.ForeignKey(
        ApprovalStatus, related_name = "investigations", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)


class Prosecution(models.Model):
    victim = models.ForeignKey(VictimProfile, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True)
    trafficker = models.ForeignKey(
        SuspectedTrafficker, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    interviewer = models.ForeignKey(
        Interviewer, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    status_of_case = models.ForeignKey(
        CaseStatus, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    trial_court = models.ForeignKey(
        TrialCourt, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    trial_court_country = models.ForeignKey(
        Country, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    court_case_no = models.CharField(max_length=50, null=True, blank=True)
    guilty_verdict = models.BooleanField(null=True, blank=True)
    verdict = models.ForeignKey(
        Verdict, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    guilty_verdict_reason = models.ForeignKey(
        GuiltyReason, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    prosecution_outcome = models.ForeignKey(
        ProsecutionOutcome, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    aquital_reason = models.ForeignKey(
        AquitalReason, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    review_appeal_outcome = models.CharField(max_length=50, null=True, blank=True)
    sanction_penalty = models.ForeignKey(
        SanctionPenalty, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    years_imposed = models.IntegerField(null=True, blank=True)
    approval = models.ForeignKey(
        ApprovalStatus, related_name = "prosecutions", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class VictimPermissions(models.Model):
    interviewer = models.ForeignKey(
        Interviewer,  on_delete=models.CASCADE, null=True, blank=True
    )
    victim = models.ForeignKey(
        VictimProfile, related_name = "victim_permission", on_delete=models.CASCADE, null=True, blank=True
    )
    permissions_requested = models.ManyToManyField(
        AccessPermission,  related_name = "permissions_request", null=True, blank=True
    )

    permissions_granted = models.ManyToManyField(
        AccessPermission,  related_name = "permissions_granted", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class Exploitation(models.Model):
    victim = models.ForeignKey(
        VictimProfile, related_name = "exploitation", on_delete=models.CASCADE, null=True, blank=True
    )
    subject_to_exploitation  = models.BooleanField(null=True,blank=True)
    intent_to_exploit = models.BooleanField(null=True,blank=True)
    exploitation_length = models.CharField(max_length=50,null=True,blank=True)
    exploitation_age = models.ForeignKey(
        ExploitationAge, related_name="exploitation", on_delete=models.CASCADE, null=True, blank=True
    )
    pay_debt = models.BooleanField(null=True,blank=True)
    debt_amount = models.CharField(max_length=50,null=True,blank=True)
    freed_method = models.ForeignKey(FreedMethod, related_name="exploitation", on_delete=models.CASCADE,null=True,blank=True)
    event_description = models.TextField(null=True,blank=True)
    e_prostitution = models.BooleanField(null=True,blank=True)
    e_other_sexual = models.BooleanField(null=True,blank=True)
    e_other_sexual_online = models.BooleanField(null=True,blank=True)
    e_online_porno = models.BooleanField(null=True,blank=True)
    e_criminal_activity = models.BooleanField(null=True,blank=True)
    e_criminal_activity_type = models.ManyToManyField(
        CriminalActivityType,  related_name = "exploitation", null=True, blank=True
    )
    e_forced_labour = models.BooleanField(null=True,blank=True)
    e_forced_labour_industry = models.ManyToManyField(
        ForcedLabourIndustry,  related_name = "exploitation", null=True, blank=True
    )
    e_forced_marriage = models.BooleanField(null=True,blank=True)
    e_victim_knew_spouse = models.BooleanField(null=True,blank=True)
    e_spouse_nationality = models.ForeignKey(Country, related_name="exploitation_spouse_nationality", on_delete=models.CASCADE,null=True,blank=True)
    e_bprice_paid = models.ForeignKey(BridePrice, related_name="exploitation", on_delete=models.CASCADE,null=True,blank=True)
    e_bprice_amount_kind = models.CharField(max_length=250,null=True,blank=True)
    e_brice_recipient = models.ManyToManyField(
        BridePriceRecipient,  related_name = "exploitation", null=True, blank=True
    )
    e_child_marriage = models.BooleanField(null=True,blank=True)
    e_child_marriage_reason = models.ManyToManyField(
        ChildMarriageReason,  related_name = "exploitation", null=True, blank=True
    )
    e_victim_pregnancy = models.BooleanField(null=True,blank=True)
    e_children_from_marriage = models.IntegerField(null=True, blank=True)
    e_maternal_health_issues = models.BooleanField(null=True,blank=True)
    e_m_health_issues_description = models.TextField(null=True,blank=True)
    e_marriage_violence = models.ForeignKey(AffirmOption, related_name="exploitation", on_delete=models.CASCADE,null=True,blank=True)
    e_marriage_violence_type = models.ManyToManyField(
        MarriageViolenceType,  related_name = "exploitation", null=True, blank=True
    )
    e_forced_military_type = models.ForeignKey(MilitaryType, related_name="exploitation", on_delete=models.CASCADE,null=True,blank=True)
    e_armed_group_name = models.CharField(max_length=250,null=True,blank=True)
    e_victim_military_activities = models.ManyToManyField(
        MilitaryActivity,  related_name = "exploitation", null=True, blank=True
    )
    e_child_soldier = models.BooleanField(null=True,blank=True)
    e_child_soldier_age = models.IntegerField(null=True, blank=True)
    e_organ_removed = models.BooleanField(null=True,blank=True)
    e_body_part_removed = models.ManyToManyField(
        BodyPart,  related_name = "exploitation", null=True, blank=True
    )
    e_operation_location = models.ForeignKey(OperationLocation, related_name="exploitation", on_delete=models.CASCADE,null=True,blank=True)
    e_operation_country = models.ForeignKey(Country, related_name="exploitation_operation_country", on_delete=models.CASCADE,null=True,blank=True)
    e_organ_sale_price = models.CharField(max_length=50,null=True,blank=True)
    e_organ_paid_to = models.ForeignKey(OrganPaidTo, related_name="exploitation", on_delete=models.CASCADE,null=True,blank=True)
    e_remarks = models.TextField(null=True,blank=True)
    e_recruitment_type = models.ForeignKey(RecruitmentType, related_name="exploitation", on_delete=models.CASCADE,null=True,blank=True)
    e_recruiter_relationship = models.ForeignKey(RecruiterRelationship, related_name="exploitation", on_delete=models.CASCADE,null=True,blank=True)
    e_trafficking_means = models.ManyToManyField(
        TraffickingMean,  related_name = "exploitation", null=True, blank=True
    )
    interviewer = models.ForeignKey(Interviewer, related_name = "exploitation", on_delete=models.CASCADE, null=True, blank=True)
    approval = models.ForeignKey(
        ApprovalStatus, related_name = "exploitation", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class Assistance(models.Model):
    victim = models.ForeignKey(VictimProfile, related_name = "assistance", on_delete=models.CASCADE, null=True, blank=True)
    social_assistance_days = models.IntegerField(null=True, blank=True)
    social_assistance_months = models.IntegerField(null=True, blank=True)
    social_assistance_provider = models.ManyToManyField(
        Provider,  related_name = "social_assistance", null=True, blank=True
    )
    med_rehab_days = models.IntegerField(null=True, blank=True)
    med_rehab_months = models.IntegerField(null=True, blank=True)
    med_rehab_provider = models.ManyToManyField(
        Provider,  related_name = "med_rehab", null=True, blank=True
    )
    housing_allowance_days = models.IntegerField(null=True, blank=True)
    housing_allowance_months = models.IntegerField(null=True, blank=True)
    housing_allowance_provider = models.ManyToManyField(
        Provider,  related_name = "housing_allowance", null=True, blank=True
    )
    halfway_house_days = models.IntegerField(null=True, blank=True)
    halfway_house_months = models.IntegerField(null=True, blank=True)
    halfway_house_providers = models.ManyToManyField(
        Provider,  related_name = "halfway_house", null=True, blank=True
    )
    shelter_days = models.IntegerField(null=True, blank=True)
    shelter_months = models.IntegerField(null=True, blank=True)
    shelter_provider = models.ManyToManyField(
        Provider,  related_name = "shelter", null=True, blank=True
    )
    vocational_training_days = models.IntegerField(null=True, blank=True)
    vocational_training_months = models.IntegerField(null=True, blank=True)
    vocational_training_provider = models.ManyToManyField(
        Provider,  related_name = "vocational_training", null=True, blank=True
    )
    micro_ent_income_days = models.IntegerField(null=True, blank=True)
    micro_ent_income_months = models.IntegerField(null=True, blank=True)
    micro_ent_income_provider = models.ManyToManyField(
        Provider,  related_name = "micro_ent_income", null=True, blank=True
    )
    micro_ent_income_project= models.ForeignKey(IncomeProjectType,  related_name = "micro_ent_income", on_delete=models.CASCADE, null=True, blank=True) 
    legal_assistance_days = models.IntegerField(null=True, blank=True)
    legal_assistance_months = models.IntegerField(null=True, blank=True)
    legal_assistance_provider = models.ManyToManyField(
        Provider,  related_name = "legal_assistance", null=True, blank=True
    )
    medical_assistance_days = models.IntegerField(null=True, blank=True)
    medical_assistance_months = models.IntegerField(null=True, blank=True)
    medical_assistance_provider = models.ManyToManyField(
        Provider,  related_name = "medical_assistance", null=True, blank=True
    )
    financial_assistance_days = models.IntegerField(null=True, blank=True)
    financial_assistance_months = models.IntegerField(null=True, blank=True)
    financial_assistance_provider = models.ManyToManyField(
        Provider,  related_name = "financial_assistance", null=True, blank=True
    )
    education_assistance_days = models.IntegerField(null=True, blank=True)
    education_assistance_months = models.IntegerField(null=True, blank=True)
    education_assistance_provider = models.ManyToManyField(
        Provider,  related_name = "education_assistance", null=True, blank=True
    )
    education_assistance_level= models.ForeignKey(EducationLevel,  related_name = "education_assistance", on_delete=models.CASCADE, null=True, blank=True)
    im_emmigration_assistance_days = models.IntegerField(null=True, blank=True)
    im_emmigration_assistance_months = models.IntegerField(null=True, blank=True)
    im_emmigration_assistance_provider = models.ManyToManyField(
        Provider,  related_name = "im_emmigration_assistance", null=True, blank=True
    )
    im_emmigration_assistance_status= models.ForeignKey(ImEmmigrationStatus,  related_name = "im_emmigration_assistance", on_delete=models.CASCADE, null=True, blank=True)
    other_community_assistance_days = models.IntegerField(null=True, blank=True)
    other_community_assistance_months = models.IntegerField(null=True, blank=True)
    other_community_assistance_provider = models.ManyToManyField(
        Provider,  related_name = "other_community_assistance", null=True, blank=True
    )
    other_community_assistance_type= models.ForeignKey(CommunityAssistanceType,  related_name = "other_community_assistance", on_delete=models.CASCADE, null=True, blank=True)
    interviewer = models.ForeignKey(Interviewer, related_name = "assistance", on_delete=models.CASCADE, null=True, blank=True)
    approval = models.ForeignKey(
        ApprovalStatus, related_name = "assistance", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class AssistanceAggregateData(models.Model):
    data_supplier = models.ForeignKey(DataSupplier,  related_name = "aggregate_data_supplier", on_delete=models.CASCADE, null=True, blank=True)
    total_tip_annually = models.IntegerField(null=True,blank=True)
    total_service = models.IntegerField(null=True,blank=True)
    eligible_family_service = models.IntegerField(null=True,blank=True)
    total_anon_contacts = models.IntegerField(null=True,blank=True)
    interviewer = models.ForeignKey(Interviewer, related_name = "assistance_aggregate", on_delete=models.CASCADE, null=True, blank=True)
    approval = models.ForeignKey(
        ApprovalStatus, related_name = "assistance_aggregate", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class SocioEconomic(models.Model):
    victim = models.ForeignKey(VictimProfile, related_name = "socio_economic", on_delete=models.CASCADE, null=True, blank=True)
    family_structure = models.ForeignKey(FamilyStructure,  related_name = "socio_economic", on_delete=models.CASCADE, null=True, blank=True)
    living_with = models.ForeignKey(LivingWith,  related_name = "socio_economic", on_delete=models.CASCADE, null=True, blank=True)
    violence_prior = models.BooleanField(null=True,blank=True)
    violence_type = models.CharField(max_length=50, null=True, blank=True)
    education_level = models.ForeignKey(EducationLevel,  related_name = "socio_economic", on_delete=models.CASCADE, null=True, blank=True)
    last_occupation = models.ManyToManyField(
        Occupation,  related_name = "socio_economic", null=True, blank=True
    )
    interviewer = models.ForeignKey(Interviewer, related_name = "socio_economic", on_delete=models.CASCADE, null=True, blank=True)
    approval = models.ForeignKey(
        ApprovalStatus, related_name = "socio_economic", on_delete=models.CASCADE, null=True, blank=True
    )
    approval_comments = models.TextField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

class Search(models.Model):
    search_text = models.CharField(null = True, blank = True)
    search_description = models.CharField(null = True, blank = True)
    search_text_fr = models.CharField(null = True, blank = True)
    search_description_fr = models.CharField(null = True, blank = True)
    search_text_pt = models.CharField(null = True, blank = True)
    search_description_pt = models.CharField(null = True, blank = True)
    search_link = models.CharField(null = True, blank = True)
    search_tag = models.ForeignKey(
        Tag, related_name = "search", on_delete=models.CASCADE, null=True, blank=True
    )
    is_technical = models.BooleanField(blank=True,null=True)
    is_admin = models.BooleanField(blank=True,null=True)
    data_entry_purpose = models.ForeignKey(
        DataEntryPurpose, related_name = "search", on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True,null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)


class Faq(models.Model):
    question = models.CharField(null = True, blank = True)
    answer = models.TextField(null = True, blank = True)
    is_active = models.BooleanField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True,null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)

