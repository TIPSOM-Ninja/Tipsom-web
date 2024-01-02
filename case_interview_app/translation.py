from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields=['name']

@register(Gender)
class GenderTranslationOptions(TranslationOptions):
    fields=['name']

@register(Race)
class RaceTranslationOptions(TranslationOptions):
    fields=['name']

@register(IdType)
class IdTypeTranslationOptions(TranslationOptions):
    fields=['name']

@register(DataEntryPurpose)
class DataEntryPurposeTranslationOptions(TranslationOptions):
    fields=['name']

@register(InvestigationStatus)
class InvestigationStatusTranslationOptions(TranslationOptions):
    fields=['name']

@register(TraffickerOrg)
class TraffickerOrgTranslationOptions(TranslationOptions):
    fields=['name']

@register(RoleInTrafficking)
class RoleInTraffickingTranslationOptions(TranslationOptions):
    fields=['name']

@register(CaseStatus)
class CaseStatusTranslationOptions(TranslationOptions):
    fields=['name']

@register(TrialCourt)
class TrialCourtTranslationOptions(TranslationOptions):
    fields=['name']

@register(GuiltyReason)
class GuiltyReasonTranslationOptions(TranslationOptions):
    fields=['name']

@register(ProsecutionOutcome)
class ProsecutionOutcomeTranslationOptions(TranslationOptions):
    fields=['name']

@register(AquitalReason)
class AquitalReasonTranslationOptions(TranslationOptions):
    fields=['name']

@register(SanctionPenalty)
class SanctionPenaltyTranslationOptions(TranslationOptions):
    fields=['name']

@register(TransportMean)
class TransportMeanTranslationOptions(TranslationOptions):
    fields=['name']

@register(Verdict)
class VerdictTranslationOptions(TranslationOptions):
    fields=['name']

@register(ApprovalStatus)
class ApprovalStatusTranslationOptions(TranslationOptions):
    fields=['name']

@register(AccessPermission)
class AccessPermissionTranslationOptions(TranslationOptions):
    fields=['name']

@register(ExploitationAge)
class ExploitationAgeTranslationOptions(TranslationOptions):
    fields=['name']

@register(FreedMethod)
class FreedMethodTranslationOptions(TranslationOptions):
    fields=['name']

@register(CriminalActivityType)
class CriminalActivityTypeTranslationOptions(TranslationOptions):
    fields=['name']

@register(ForcedLabourIndustry)
class ForcedLabourIndustryTranslationOptions(TranslationOptions):
    fields=['name']

@register(BridePrice)
class BridePriceTranslationOptions(TranslationOptions):
    fields=['name']

@register(BridePriceRecipient)
class BridePriceRecipientTranslationOptions(TranslationOptions):
    fields=['name']

@register(ChildMarriageReason)
class ChildMarriageReasonTranslationOptions(TranslationOptions):
    fields=['name']

@register(AffirmOption)
class AffirmOptionTranslationOptions(TranslationOptions):
    fields=['name']

@register(MarriageViolenceType)
class MarriageViolenceTypeTranslationOptions(TranslationOptions):
    fields=['name']

@register(MilitaryType)
class MilitaryTypeTranslationOptions(TranslationOptions):
    fields=['name']

@register(MilitaryActivity)
class MilitaryActivityTranslationOptions(TranslationOptions):
    fields=['name']

@register(BodyPart)
class BodyPartTranslationOptions(TranslationOptions):
    fields=['name']

@register(OperationLocation)
class OperationLocationTranslationOptions(TranslationOptions):
    fields=['name']

@register(OrganPaidTo)
class OrganPaidToTranslationOptions(TranslationOptions):
    fields=['name']

@register(RecruitmentType)
class RecruitmentTypeTranslationOptions(TranslationOptions):
    fields=['name']

@register(RecruiterRelationship)
class RecruiterRelationshipTranslationOptions(TranslationOptions):
    fields=['name']

@register(TraffickingMean)
class TraffickingMeanTranslationOptions(TranslationOptions):
    fields=['name']

@register(Provider)
class ProviderTranslationOptions(TranslationOptions):
    fields=['name']

@register(IncomeProjectType)
class IncomeProjectTypeTranslationOptions(TranslationOptions):
    fields=['name']

@register(EducationLevel)
class EducationLevelTranslationOptions(TranslationOptions):
    fields=['name']

@register(ImEmmigrationStatus)
class ImEmmigrationStatusTranslationOptions(TranslationOptions):
    fields=['name']

@register(CommunityAssistanceType)
class CommunityAssistanceTypeTranslationOptions(TranslationOptions):
    fields=['name']

@register(DataSupplier)
class DataSupplierTranslationOptions(TranslationOptions):
    fields=['name']

@register(FamilyStructure)
class FamilyStructureTranslationOptions(TranslationOptions):
    fields=['name']

@register(LivingWith)
class LivingWithTranslationOptions(TranslationOptions):
    fields=['name']

@register(Occupation)
class OccupationTranslationOptions(TranslationOptions):
    fields=['name']

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields=['name']



