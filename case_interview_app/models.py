from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)

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


class VictimProfile(models.Model):
    citizenship = models.ForeignKey(
        Country, related_name = "victims_cit",  on_delete=models.CASCADE, null=True, blank=True
    )
    countryOfBirth = models.ForeignKey(
        Country, related_name = "victims_country",  on_delete=models.CASCADE, null=True, blank=True
    )
    languages = models.ManyToManyField(Country, related_name = "victims_lang", null=True, blank=True)
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
    interview_location = models.CharField(max_length=50, null=True, blank=True)
    interview_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    additional_remarks = models.TextField(null=True, blank=True)


class Interviewer(models.Model):
    victim = models.ForeignKey(VictimProfile, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(
        Country, related_name = "interviewers", on_delete=models.CASCADE, null=True, blank=True
    )
    data_entry_purpose = models.ForeignKey(
        DataEntryPurpose, related_name = "interviewers", on_delete=models.CASCADE, null=True, blank=True
    )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    organization = models.CharField(max_length=50, null=True, blank=True)
    email_address = models.EmailField(max_length=254, null=True, blank=True)


class TransitRouteDestination(models.Model):
    victim = models.ForeignKey(VictimProfile, related_name = "destinations", on_delete=models.CASCADE, null=True, blank=True)
    country_of_origin = models.ForeignKey(
        Country, related_name = "origin_destinations", on_delete=models.CASCADE, null=True, blank=True
    )
    city_village_of_origin = models.CharField(max_length=50, null=True, blank=True)
    country_of_dest = models.ForeignKey(
        Country, related_name = "dest_destinations", on_delete=models.CASCADE, null=True, blank=True
    )
    means_of_transport = models.ForeignKey(
        TransportMean, related_name = "destinations", on_delete=models.CASCADE, null=True, blank=True
    )
    remarks = models.TextField(null=True, blank=True)


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
    id_number = models.IntegerField(null=True, blank=True)
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


class ArrestInvestigation(models.Model):
    victim = models.ForeignKey(VictimProfile, related_name = "investigations", on_delete=models.CASCADE, null=True, blank=True)
    trafficker = models.ForeignKey(
        SuspectedTrafficker, related_name = "investigations",  on_delete=models.CASCADE, null=True, blank=True
    )
    suspects_arrested = models.BooleanField(null=True, blank=True)
    why_no_arrest = models.TextField(null=True, blank=True)
    victim_smuggled = models.BooleanField(null=True, blank=True)
    how_traffickers_org = models.ForeignKey(
        TraffickerOrg,  related_name = "investigations", on_delete=models.CASCADE, null=True, blank=True
    )
    investigation_done = models.BooleanField(null=True, blank=True)
    why_no_investigation = models.TextField(null=True, blank=True)
    investigation_status = models.ForeignKey(
        InvestigationStatus, related_name = "investigations", on_delete=models.CASCADE, null=True, blank=True
    )
    why_pending = models.TextField(null=True, blank=True)
    withdrawn_closed_reason = models.TextField(null=True, blank=True)


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
