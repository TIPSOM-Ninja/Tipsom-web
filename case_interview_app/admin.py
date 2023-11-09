from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    pass


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    pass


@admin.register(IdType)
class IdTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(DataEntryPurpose)
class DataEntryPurposeAdmin(admin.ModelAdmin):
    pass


@admin.register(InvestigationStatus)
class InvestigationStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(TraffickerOrg)
class TraffickerOrgAdmin(admin.ModelAdmin):
    pass


@admin.register(RoleInTrafficking)
class RoleInTraffickingAdmin(admin.ModelAdmin):
    pass


@admin.register(CaseStatus)
class CaseStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(TrialCourt)
class TrialCourtAdmin(admin.ModelAdmin):
    pass


@admin.register(GuiltyReason)
class GuiltyReasonAdmin(admin.ModelAdmin):
    pass


@admin.register(ProsecutionOutcome)
class ProsecutionOutcomeAdmin(admin.ModelAdmin):
    pass


@admin.register(AquitalReason)
class AquitalReasonAdmin(admin.ModelAdmin):
    pass


@admin.register(SanctionPenalty)
class SanctionPenaltyAdmin(admin.ModelAdmin):
    pass


@admin.register(TransportMean)
class TransportMeanAdmin(admin.ModelAdmin):
    pass


@admin.register(VictimProfile)
class VictimProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Interviewer)
class InterviewerAdmin(admin.ModelAdmin):
    pass


@admin.register(TransitRouteDestination)
class TransitRouteDestinationAdmin(admin.ModelAdmin):
    pass


@admin.register(SuspectedTrafficker)
class SuspectedTraffickerAdmin(admin.ModelAdmin):
    pass


@admin.register(ArrestInvestigation)
class ArrestInvestigationAdmin(admin.ModelAdmin):
    pass


@admin.register(Prosecution)
class ProsecutionAdmin(admin.ModelAdmin):
    pass

@admin.register(ApprovalStatus)
class ApprovalStatusAdmin(admin.ModelAdmin):
    pass
