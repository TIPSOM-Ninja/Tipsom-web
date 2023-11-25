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

@admin.register(Verdict)
class VerdictAdmin(admin.ModelAdmin):
    pass

@admin.register(ApprovalStatus)
class ApprovalStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(AccessPermission)
class AccessPermissionAdmin(admin.ModelAdmin):
    pass

@admin.register(ExploitationAge)
class ExploitationAgeAdmin(admin.ModelAdmin):
    pass

@admin.register(FreedMethod)
class FreedMethodAdmin(admin.ModelAdmin):
    pass

@admin.register(CriminalActivityType)
class CriminalActivityTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(ForcedLabourIndustry)
class ForcedLabourIndustryAdmin(admin.ModelAdmin):
    pass

@admin.register(BridePrice)
class BridePriceAdmin(admin.ModelAdmin):
    pass

@admin.register(BridePriceRecipient)
class BridePriceRecipientAdmin(admin.ModelAdmin):
    pass

@admin.register(ChildMarriageReason)
class ChildMarriageReasonAdmin(admin.ModelAdmin):
    pass

@admin.register(AffirmOption)
class AffirmOptionAdmin(admin.ModelAdmin):
    pass

@admin.register(MarriageViolenceType)
class MarriageViolenceTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(MilitaryType)
class MilitaryTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(MilitaryActivity)
class MilitaryActivityAdmin(admin.ModelAdmin):
    pass

@admin.register(BodyPart)
class BodyPartAdmin(admin.ModelAdmin):
    pass

@admin.register(OperationLocation)
class OperationLocationAdmin(admin.ModelAdmin):
    pass

@admin.register(OrganPaidTo)
class OrganPaidToAdmin(admin.ModelAdmin):
    pass

@admin.register(RecruitmentType)
class RecruitmentTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(RecruiterRelationship)
class RecruiterRelationshipAdmin(admin.ModelAdmin):
    pass

@admin.register(TraffickingMean)
class TraffickingMeanAdmin(admin.ModelAdmin):
    pass

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass

@admin.register(IncomeProjectType)
class IncomeProjectTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(ImEmmigrationStatus)
class ImEmmigrationStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(CommunityAssistanceType)
class CommunityAssistanceTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(DataSupplier)
class DataSupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(FamilyStructure)
class FamilyStructureAdmin(admin.ModelAdmin):
    pass

@admin.register(LivingWith)
class LivingWithAdmin(admin.ModelAdmin):
    pass

@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass




@admin.register(VictimProfile)
class VictimProfileAdmin(admin.ModelAdmin):
    list_display = ['victim_identifier','citizenship','countryOfBirth','gender','interview_location','interview_date','approval']
    list_filter = ["approval", "citizenship"]

class PendingCase(VictimProfile):
    class Meta:
        proxy = True


@admin.register(PendingCase)
class PendingCaseAdmin(VictimProfileAdmin):
    actions = ["approve", "reject","clarify"]
    def get_queryset(self, request):
        return self.model.objects.filter(approval_id=1)

    @admin.action(description="Approve victim profile")
    def approve(modeladmin, request, queryset):
        queryset.update(approval_id=2)

    @admin.action(description="Reject Victim profile")
    def reject(modeladmin, request, queryset):
        queryset.update(approval_id=3)
    
    @admin.action(description="Request clarification")
    def clarify(modeladmin, request, queryset):
        queryset.update(approval_id=4)



@admin.register(Interviewer)
class InterviewerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','position','organization','email_address','country','approval']
    list_filter = ["country", "data_entry_purpose","approval"]



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

@admin.register(Exploitation)
class ExploitationAdmin(admin.ModelAdmin):
    pass

@admin.register(VictimPermissions)
class VictimPermissionsAdmin(admin.ModelAdmin):
    pass

@admin.register(Assistance)
class AssistanceAdmin(admin.ModelAdmin):
    pass

@admin.register(AssistanceAggregateData)
class AssistanceAggregateDataAdmin(admin.ModelAdmin):
    pass

@admin.register(SocioEconomic)
class SocioEconomicAdmin(admin.ModelAdmin):
    pass

@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ['search_text','search_description','search_link','search_tag','is_technical','is_admin']
    list_filter = ["search_tag", "is_technical",'is_admin']




