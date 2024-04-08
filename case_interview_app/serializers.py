# serializers.py
from rest_framework import serializers
from .models import *
from django.db.models import Count

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'

class IdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdType
        fields = '__all__'

class DataEntryPurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEntryPurpose
        fields = '__all__'

class InvestigationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigationStatus
        fields = '__all__'

class TraffickerOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraffickerOrg
        fields = '__all__'

class RoleInTraffickingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleInTrafficking
        fields = '__all__'

class CaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStatus
        fields = '__all__'

class TrialCourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialCourt
        fields = '__all__'

class GuiltyReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiltyReason
        fields = '__all__'

class ProsecutionOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProsecutionOutcome
        fields = '__all__'

class AquitalReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AquitalReason
        fields = '__all__'

class SanctionPenaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = SanctionPenalty
        fields = '__all__'

class TransportMeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportMean
        fields = '__all__'

class VerdictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verdict
        fields = '__all__'

class ApprovalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalStatus
        fields = '__all__'

class AccessPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPermission
        fields = '__all__'

class ExploitationAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExploitationAge
        fields = '__all__'

class FreedMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreedMethod
        fields = '__all__'

class CriminalActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriminalActivityType
        fields = '__all__'

class ForcedLabourIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForcedLabourIndustry
        fields = '__all__'

class BridePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BridePrice
        fields = '__all__'

class BridePriceRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BridePriceRecipient
        fields = '__all__'

class ChildMarriageReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildMarriageReason
        fields = '__all__'

class AffirmOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffirmOption
        fields = '__all__'

class MarriageViolenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarriageViolenceType
        fields = '__all__'

class MilitaryActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryActivity
        fields = '__all__'

class MilitaryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryType
        fields = '__all__'

class BodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyPart
        fields = '__all__'

class OperationLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationLocation
        fields = '__all__'

class OrganPaidToSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganPaidTo
        fields = '__all__'

class RecruitmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentType
        fields = '__all__'

class RecruiterRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterRelationship
        fields = '__all__'

class TraffickingMeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraffickingMean
        fields = '__all__'

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class IncomeProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeProjectType
        fields = '__all__'

class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = '__all__'

class ImEmmigrationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImEmmigrationStatus
        fields = '__all__'

class CommunityAssistanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityAssistanceType
        fields = '__all__'

class DataSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSupplier
        fields = '__all__'

class FamilyStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyStructure
        fields = '__all__'

class LivingWithSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivingWith
        fields = '__all__'

class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

#
class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class LanguageNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class GenderNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class RaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'

class IdTypeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdType
        fields = '__all__'

class DataEntryPurposeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEntryPurpose
        fields = '__all__'

class InvestigationStatusNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigationStatus
        fields = '__all__'

class TraffickerOrgNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraffickerOrg
        fields = '__all__'

class RoleInTraffickingNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleInTrafficking
        fields = '__all__'

class CaseStatusNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStatus
        fields = '__all__'

class TrialCourtNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrialCourt
        fields = '__all__'

class GuiltyReasonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiltyReason
        fields = '__all__'

class ProsecutionOutcomeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProsecutionOutcome
        fields = '__all__'

class AquitalReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AquitalReason
        fields = '__all__'

class SanctionPenaltyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanctionPenalty
        fields = '__all__'

class TransportMeanNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportMean
        fields = '__all__'

class VerdictNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verdict
        fields = '__all__'

class ApprovalStatusNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalStatus
        fields = '__all__'

class AccessPermissionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPermission
        fields = '__all__'

class ExploitationAgeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExploitationAge
        fields = '__all__'

class FreedMethodNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreedMethod
        fields = '__all__'

class CriminalActivityTypeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriminalActivityType
        fields = '__all__'

class ForcedLabourIndustryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForcedLabourIndustry
        fields = '__all__'

class BridePriceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BridePrice
        fields = '__all__'

class BridePriceRecipientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BridePriceRecipient
        fields = '__all__'

class ChildMarriageReasonNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildMarriageReason
        fields = '__all__'

class AffirmOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffirmOption
        fields = '__all__'

class MarriageViolenceTypeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarriageViolenceType
        fields = '__all__'

class MilitaryActivityNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryActivity
        fields = '__all__'

class MilitaryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilitaryType
        fields = '__all__'

class BodyPartNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyPart
        fields = '__all__'

class OperationLocationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationLocation
        fields = '__all__'

class OrganPaidToNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganPaidTo
        fields = '__all__'

class RecruitmentTypeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentType
        fields = '__all__'

class RecruiterRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterRelationship
        fields = '__all__'

class TraffickingMeanNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraffickingMean
        fields = '__all__'

class ProviderNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class IncomeProjectTypeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeProjectType
        fields = '__all__'

class EducationLevelNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = '__all__'

class ImEmmigrationStatusNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImEmmigrationStatus
        fields = '__all__'

class CommunityAssistanceTypeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityAssistanceType
        fields = '__all__'

class DataSupplierNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSupplier
        fields = '__all__'

class FamilyStructureNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyStructure
        fields = '__all__'

class LivingWithNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivingWith
        fields = '__all__'

class OccupationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'

class TagNameNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class VictimProfileSerializer(serializers.ModelSerializer):
    citizenship = CountrySerializer(read_only=True)
    countryOfBirth = CountrySerializer(read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    gender = GenderSerializer(read_only=True)
    race = RaceSerializer(read_only=True)
    identification_type = IdTypeSerializer(many=True, read_only=True)
    lastPlaceOfResidence = CountrySerializer(read_only=True)
    interviewCountry = CountrySerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = VictimProfile
        fields = '__all__'

class InterviewerSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    data_entry_purpose = DataEntryPurposeSerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)
    victims = VictimProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Interviewer
        fields = '__all__'

class TransitRouteDestinationSerializer(serializers.ModelSerializer):
    victim = VictimProfileSerializer(read_only=True)
    country_of_origin = CountrySerializer(read_only=True)
    country_of_dest = CountrySerializer(read_only=True)
    transport_means = TransportMeanSerializer(many=True, read_only=True)
    interviewer = InterviewerSerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = TransitRouteDestination
        fields = '__all__'

class SuspectedTraffickerSerializer(serializers.ModelSerializer):
    victim = VictimProfileSerializer(read_only=True)
    gender = GenderSerializer(read_only=True)
    race = RaceSerializer(read_only=True)
    country_of_birth = CountrySerializer(read_only=True)
    citizenship = CountrySerializer(read_only=True)
    nationality = CountrySerializer(read_only=True)
    id_type = IdTypeSerializer(read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    role_in_trafficking = RoleInTraffickingSerializer(many=True, read_only=True)
    traffick_from_country = CountrySerializer(read_only=True)
    traffick_to_country = CountrySerializer(read_only=True)
    interviewer = InterviewerSerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = SuspectedTrafficker
        fields = '__all__'

class ExploitationSerializer(serializers.ModelSerializer):
    victim = VictimProfileSerializer(read_only=True)
    exploitation_age = ExploitationAgeSerializer(read_only=True)
    freed_method = FreedMethodSerializer(read_only=True)
    e_criminal_activity_type = CriminalActivityTypeSerializer(many=True, read_only=True)
    e_forced_labour_industry = ForcedLabourIndustrySerializer(many=True, read_only=True)
    e_spouse_nationality = CountrySerializer(read_only=True)
    e_bprice_paid = BridePriceSerializer(read_only=True)
    e_brice_recipient = BridePriceRecipientSerializer(many=True, read_only=True)
    e_child_marriage_reason = ChildMarriageReasonSerializer(many=True, read_only=True)
    e_marriage_violence = AffirmOptionSerializer(read_only=True)
    e_marriage_violence_type = MarriageViolenceTypeSerializer(many=True, read_only=True)
    e_forced_military_type = MilitaryTypeSerializer(read_only=True)
    e_victim_military_activities = MilitaryActivitySerializer(many=True, read_only=True)
    e_body_part_removed = BodyPartSerializer(many=True, read_only=True)
    e_operation_location = OperationLocationSerializer(read_only=True)
    e_operation_country = CountrySerializer(read_only=True)
    e_organ_paid_to = OrganPaidToSerializer(read_only=True)
    e_recruitment_type = RecruitmentTypeSerializer(read_only=True)
    e_recruiter_relationship = RecruiterRelationshipSerializer(read_only=True)
    e_trafficking_means = TraffickingMeanSerializer(many=True, read_only=True)
    interviewer = InterviewerSerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = Exploitation
        fields = '__all__'

class AssistanceSerializer(serializers.ModelSerializer):
    
    victim = VictimProfileSerializer(read_only=True)
    socialAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "social_assistance_provider")
    medicalRehabilitationAssistanceProvider = ProviderSerializer(many=True, read_only=True, source ="med_rehab_provider")
    housingAllowanceProvider = ProviderSerializer(many=True, read_only=True, source = "housing_allowance_provider")
    halfwayHouseProvider = ProviderSerializer(many=True, read_only=True, source = "halfway_house_providers")
    shelterProvider = ProviderSerializer(many=True, read_only=True, source = "shelter_provider")
    vocationalTrainingProvider = ProviderSerializer(many=True, read_only=True, source = "vocational_training_provider")
    incomeGeneratingProjectProvider = ProviderSerializer(many=True, read_only=True, source = "micro_ent_income_provider")
    micro_ent_income_project = IncomeProjectTypeSerializer(read_only=True)
    legalAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "legal_assistance_provider")
    medicalAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "medical_assistance_provider")
    financialAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "financial_assistance_provider")
    educationAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "education_assistance_provider")
    education_assistance_level = EducationLevelSerializer(read_only=True)
    immEmmigrationAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "im_emmigration_assistance_provider")
    im_emmigration_assistance_status = ImEmmigrationStatusSerializer(read_only=True)
    communityBasedAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "other_community_assistance_provider")
    other_community_assistance_type = CommunityAssistanceTypeSerializer(read_only=True)
    socialAssistanceDuration = serializers.SerializerMethodField()
    socialAssistanceDurationType = serializers.SerializerMethodField()

    medicalRehabilitationAssistanceDuration = serializers.SerializerMethodField()
    medicalRehabilitationAssistanceDurationType = serializers.SerializerMethodField()

    housingAllowanceDuration = serializers.SerializerMethodField()
    housingAllowanceDurationType = serializers.SerializerMethodField()

    halfwayHouseDuration = serializers.SerializerMethodField()
    halfwayHouseDurationType = serializers.SerializerMethodField()

    shelterDuration = serializers.SerializerMethodField()
    shelterDurationType = serializers.SerializerMethodField()

    vocationalTrainingDuration = serializers.SerializerMethodField()
    vocationalTrainingDurationType = serializers.SerializerMethodField()

    incomeGeneratingProjectDuration = serializers.SerializerMethodField()
    incomeGeneratingProjectDurationType = serializers.SerializerMethodField()

    legalAssistanceDuration = serializers.SerializerMethodField()
    legalAssistanceDurationType = serializers.SerializerMethodField()

    medicalAssistanceDuration = serializers.SerializerMethodField()
    medicalAssistanceDurationType = serializers.SerializerMethodField()

    financialAssistanceDuration = serializers.SerializerMethodField()
    financialAssistanceDurationType = serializers.SerializerMethodField()

    educationAssistanceDuration = serializers.SerializerMethodField()
    educationAssistanceDurationType = serializers.SerializerMethodField()

    immEmmigrationAssistanceDuration = serializers.SerializerMethodField()
    immEmmigrationAssistanceDurationType = serializers.SerializerMethodField()

    communityBasedAssistanceDuration = serializers.SerializerMethodField()
    communityBasedAssistanceDurationType = serializers.SerializerMethodField()

    interviewer = InterviewerSerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = Assistance
        fields = '__all__'
    
    def get_socialAssistanceDuration(self, obj):
    # Implementation based on your logic
        if obj.social_assistance_days is not None:
            return obj.social_assistance_days
        elif obj.social_assistance_months is not None:
            return obj.social_assistance_months
        else:
            return None

    def get_socialAssistanceDurationType(self, obj):
        # Implementation based on your logic
        if obj.social_assistance_days is not None:
            return "0"
        elif obj.social_assistance_months is not None:
            return "1"
        else:
            return None

    def get_medicalRehabilitationAssistanceDuration(self, obj):
        # Implementation based on your logic
        if obj.med_rehab_days is not None:
            return obj.med_rehab_days
        elif obj.med_rehab_months is not None:
            return obj.med_rehab_months
        else:
            return None

    def get_medicalRehabilitationAssistanceDurationType(self, obj):
        # Implementation based on your logic
        if obj.med_rehab_days is not None:
            return "0"
        elif obj.med_rehab_months is not None:
            return "1"
        else:
            return None

    def get_housingAllowanceDuration(self, obj):
        # Implementation based on your logic
        if obj.housing_allowance_days is not None:
            return obj.housing_allowance_days
        elif obj.housing_allowance_months is not None:
            return obj.housing_allowance_months
        else:
            return None

    def get_housingAllowanceDurationType(self, obj):
        # Implementation based on your logic
        if obj.housing_allowance_days is not None:
            return "0"
        elif obj.housing_allowance_months is not None:
            return "1"
        else:
            return None

    def get_halfwayHouseDuration(self, obj):
        # Implementation based on your logic
        if obj.halfway_house_days is not None:
            return obj.halfway_house_days
        elif obj.halfway_house_months is not None:
            return obj.halfway_house_months
        else:
            return None

    def get_halfwayHouseDurationType(self, obj):
        # Implementation based on your logic
        if obj.halfway_house_days is not None:
            return "0"
        elif obj.halfway_house_months is not None:
            return "1"
        else:
            return None

    def get_shelterDuration(self, obj):
        # Implementation based on your logic
        if obj.shelter_days is not None:
            return obj.shelter_days
        elif obj.shelter_months is not None:
            return obj.shelter_months
        else:
            return None

    def get_shelterDurationType(self, obj):
        # Implementation based on your logic
        if obj.shelter_days is not None:
            return "0"
        elif obj.shelter_months is not None:
            return "1"
        else:
            return None

    def get_vocationalTrainingDuration(self, obj):
        # Implementation based on your logic
        if obj.vocational_training_days is not None:
            return obj.vocational_training_days
        elif obj.vocational_training_months is not None:
            return obj.vocational_training_months
        else:
            return None

    def get_vocationalTrainingDurationType(self, obj):
        # Implementation based on your logic
        if obj.vocational_training_days is not None:
            return "0"
        elif obj.vocational_training_months is not None:
            return "1"
        else:
            return None

    def get_incomeGeneratingProjectDuration(self, obj):
        # Implementation based on your logic
        if obj.micro_ent_income_days is not None:
            return obj.micro_ent_income_days
        elif obj.micro_ent_income_months is not None:
            return obj.micro_ent_income_months
        else:
            return None

    def get_incomeGeneratingProjectDurationType(self, obj):
        # Implementation based on your logic
        if obj.micro_ent_income_days is not None:
            return "0"
        elif obj.micro_ent_income_months is not None:
            return "1"
        else:
            return None

    def get_legalAssistanceDuration(self, obj):
        # Implementation based on your logic
        if obj.legal_assistance_days is not None:
            return obj.legal_assistance_days
        elif obj.legal_assistance_months is not None:
            return obj.legal_assistance_months
        else:
            return None

    def get_legalAssistanceDurationType(self, obj):
        # Implementation based on your logic
        if obj.legal_assistance_days is not None:
            return "0"
        elif obj.legal_assistance_months is not None:
            return "1"
        else:
            return None

    def get_medicalAssistanceDuration(self, obj):
        # Implementation based on your logic
        if obj.medical_assistance_days is not None:
            return obj.medical_assistance_days
        elif obj.medical_assistance_months is not None:
            return obj.medical_assistance_months
        else:
            return None

    def get_medicalAssistanceDurationType(self, obj):
        # Implementation based on your logic
        if obj.medical_assistance_days is not None:
            return "0"
        elif obj.medical_assistance_months is not None:
            return "1"
        else:
            return None

    def get_financialAssistanceDuration(self, obj):
        # Implementation based on your logic
        if obj.financial_assistance_days is not None:
            return obj.financial_assistance_days
        elif obj.financial_assistance_months is not None:
            return obj.financial_assistance_months
        else:
            return None

    def get_financialAssistanceDurationType(self, obj):
        # Implementation based on your logic
        if obj.financial_assistance_days is not None:
            return "0"
        elif obj.financial_assistance_months is not None:
            return "1"
        else:
            return None

    def get_educationAssistanceDuration(self, obj):
        # Implementation based on your logic
        if obj.education_assistance_days is not None:
            return obj.education_assistance_days
        elif obj.education_assistance_months is not None:
            return obj.education_assistance_months
        else:
            return None

    def get_educationAssistanceDurationType(self, obj):
        # Implementation based on your logic
        if obj.education_assistance_days is not None:
            return "0"
        elif obj.education_assistance_months is not None:
            return "1"
        else:
            return None

    def get_immEmmigrationAssistanceDuration(self, obj):
        # Implementation based on your logic
        if obj.im_emmigration_assistance_days is not None:
            return obj.im_emmigration_assistance_days
        elif obj.im_emmigration_assistance_months is not None:
            return obj.im_emmigration_assistance_months
        else:
            return None

    def get_immEmmigrationAssistanceDurationType(self, obj):
        # Implementation based on your logic
        if obj.im_emmigration_assistance_days is not None:
            return "0"
        elif obj.im_emmigration_assistance_months is not None:
            return "1"
        else:
            return None

    def get_communityBasedAssistanceDuration(self, obj):
        # Implementation based on your logic
        if obj.other_community_assistance_days is not None:
            return obj.other_community_assistance_days
        elif obj.other_community_assistance_months is not None:
            return obj.other_community_assistance_months
        else:
            return None

    def get_communityBasedAssistanceDurationType(self, obj):
        # Implementation based on your logic
        if obj.other_community_assistance_days is not None:
            return "0"
        elif obj.other_community_assistance_months is not None:
            return "1"
        else:
            return None
    

class SocioEconomicSerializer(serializers.ModelSerializer):
    # victim = VictimProfileSerializer(read_only=True)
    familyStructure = FamilyStructureSerializer(read_only=True,source ="family_structure")
    livingWith = LivingWithSerializer(read_only=True, source = "living_with")
    educationLevel = EducationLevelSerializer(read_only=True, source = "education_level")
    lastOccupation = OccupationSerializer(many=True, read_only=True, source = "last_occupation")
    # interviewer = InterviewerSerializer(read_only=True)
    # approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = SocioEconomic
        fields = ["id","familyStructure","livingWith","educationLevel","lastOccupation","violencePrior","violenceType"]

        extra_kwargs = {
            'violencePrior': {'source': 'violence_prior'},
            'violenceType': {'source': 'violence_type'}
        }


class VictimProfileWithCountsSerializer(serializers.ModelSerializer):
    assistance_count = serializers.SerializerMethodField()
    exploitation_count = serializers.SerializerMethodField()
    investigations_count = serializers.SerializerMethodField()
    prosecutions_count = serializers.SerializerMethodField()
    socio_economic_count = serializers.SerializerMethodField()
    traffickers_count = serializers.SerializerMethodField()
    destinations_count = serializers.SerializerMethodField()

    class Meta:
        model = VictimProfile
        fields = '__all__'

    def get_assistance_count(self, obj):
        return obj.assistance.aggregate(Count('id', distinct=True))['id__count']

    def get_exploitation_count(self, obj):
        return obj.exploitation.aggregate(Count('id', distinct=True))['id__count']

    def get_investigations_count(self, obj):
        return obj.investigations.aggregate(Count('id', distinct=True))['id__count']

    def get_prosecutions_count(self, obj):
        return obj.prosecutions.aggregate(Count('id', distinct=True))['id__count']

    def get_socio_economic_count(self, obj):
        return obj.socio_economic.aggregate(Count('id', distinct=True))['id__count']

    def get_traffickers_count(self, obj):
        return obj.traffickers.aggregate(Count('id', distinct=True))['id__count']

    def get_destinations_count(self, obj):
        return obj.destinations.aggregate(Count('id', distinct=True))['id__count']
    

class VictimProfileWithRelatedSerializer(serializers.ModelSerializer):
    citizenship = CountryNameSerializer(read_only=True)
    countryOfBirth = CountryNameSerializer(read_only=True)
    languages = LanguageNameSerializer(many=True, read_only=True)
    gender = GenderNameSerializer(read_only=True)
    race = RaceNameSerializer(read_only=True)
    identificationType = IdTypeNameSerializer(many=True, read_only=True, source = "identification_type")
    lastPlaceOfResidence = CountryNameSerializer(read_only=True, source = "last_place_of_residence")
    interviewCountry = CountryNameSerializer(read_only=True, source = "interview_country")
    approval = ApprovalStatusNameSerializer(read_only=True)
    # assistance_count = serializers.SerializerMethodField()
    # exploitation_count = serializers.SerializerMethodField()
    # investigations_count = serializers.SerializerMethodField()
    # prosecutions_count = serializers.SerializerMethodField()
    # socio_economic_count = serializers.SerializerMethodField()
    # traffickers_count = serializers.SerializerMethodField()
    # destinations_count = serializers.SerializerMethodField()

    class Meta:
        model = VictimProfile
        fields = ["victim_identifier","initials","age","address", 
                  "citizenship","countryOfBirth","languages","gender",
                  "race","identificationType","lastPlaceOfResidence","interviewCountry",
                  "approval","email","interviewDate","additionalRemarks","idNumber",
                  "placeOfBirth","interviewerLocation"
                  ]

        extra_kwargs = {
            'email': {'source': 'email_address'},
            'interviewDate': {'source': 'interview_date'},
            'additionalRemarks': {'source': 'additional_remarks'},
            'idNumber': {'source': 'identification_number'},
            'placeOfBirth': {'source': 'place_of_birth'},
            'interviewerLocation': {'source': 'interview_location'},
        }
    
    # def get_assistance_count(self, obj):
    #     return obj.assistance.aggregate(Count('id', distinct=True))['id__count']

    # def get_exploitation_count(self, obj):
    #     return obj.exploitation.aggregate(Count('id', distinct=True))['id__count']

    # def get_investigations_count(self, obj):
    #     return obj.investigations.aggregate(Count('id', distinct=True))['id__count']

    # def get_prosecutions_count(self, obj):
    #     return obj.prosecutions.aggregate(Count('id', distinct=True))['id__count']

    # def get_socio_economic_count(self, obj):
    #     return obj.socio_economic.aggregate(Count('id', distinct=True))['id__count']

    # def get_traffickers_count(self, obj):
    #     return obj.traffickers.aggregate(Count('id', distinct=True))['id__count']

    # def get_destinations_count(self, obj):
    #     return obj.destinations.aggregate(Count('id', distinct=True))['id__count']
    
class ProsecutionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prosecution
        fields = ['id','suspectedTrafficker', 'courtCaseNumber', 'prosecutionOutcome', 'trialCourt','foreignCourtCountry', 'caseStatus', 'verdict','reviewAppealOutcome',  'penalty', 'guiltyVerdict','yearsImposed', 'acquitalReason','v_id']
        # Specify the field names in camelCase
        extra_kwargs = {
            'suspectedTrafficker': {'source': 'trafficker_id'},
            'courtCaseNumber': {'source': 'court_case_no'},
            'prosecutionOutcome': {'source': 'prosecution_outcome_id'},
            'trialCourt': {'source': 'trial_court_id'},
            'foreignCourtCountry': {'source': 'trial_court_country_id'},
            'caseStatus': {'source': 'status_of_case_id'},
            'verdict': {'source': 'verdict_id'},
            'reviewAppealOutcome': {'source': 'review_appeal_outcome_id'},
            'penalty': {'source': 'sanction_penalty_id'},
            'guiltyVerdict': {'source': 'guilty_verdict'},
            'yearsImposed': {'source': 'years_imposed'},
            'acquitalReason': {'source': 'aquital_reason_id'},
            'v_id': {'source':'victim_id'}
        }

class ArrestInvestigationSerializer(serializers.ModelSerializer):
    howTraffickersOrg = TraffickerOrgNameSerializer(many=True,read_only = True)
    class Meta:
        model = ArrestInvestigation
        fields = ['id', 'suspectArrested', 'organizedCrime', 'whyNoArrest', 'victimSmuggled','investigationDone', 'whyNoInvestigation', 'investigationStatus','whyPending',  'withdrawnClosedReason', 'v_id','howTraffickersOrg']
        # Specify the field names in camelCase
        extra_kwargs = {
            'suspectArrested': {'source': 'suspects_arrested'},
            'organizedCrime': {'source': 'org_crime'},
            'whyNoArrest': {'source': 'why_no_arrest'},
            'victimSmuggled': {'source': 'victim_smuggled'},
            'investigationDone': {'source': 'investigation_done'},
            'whyNoInvestigation': {'source': 'why_no_investigation'},
            'investigationStatus': {'source': 'investigation_status_id'},
            'whyPending': {'source': 'why_pending'},
            'withdrawnClosedReason': {'source': 'withdrawn_closed_reason'},
            'v_id': {'source':'victim_id'}
        }

class AssistanceAggregateDataSerializer(serializers.ModelSerializer):
    dataSupplier = DataSupplierNameSerializer(read_only = True, source = "data_supplier")
    totalTip = serializers.IntegerField(source='total_tip_annually')
    totalVictim = serializers.IntegerField(source='total_service')
    totalFamily = serializers.IntegerField(source='eligible_family_service')
    totalAnon = serializers.IntegerField(source='total_anon_contacts')

    class Meta:
        model = AssistanceAggregateData
        fields = ('id', 'dataSupplier', 'totalTip', 'totalVictim', 'totalFamily', 'totalAnon', 'approval_comments', 'created_at', 'updated_at')

class SomTransitRouteDestinationSerializer(serializers.ModelSerializer):
    victim = VictimProfileSerializer(read_only=True)
    country_of_origin = CountrySerializer(read_only=True)
    country_of_dest = CountrySerializer(read_only=True)
    country_of_interception = CountrySerializer(read_only=True)
    countries_of_transit = CountrySerializer(many=True, read_only=True)
    transport_means = TransportMeanSerializer(many=True, read_only=True)
    interviewer = InterviewerSerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = TransitRouteDestination
        fields = '__all__'

class SomAssistanceSerializer(serializers.ModelSerializer):
    
    victim = VictimProfileSerializer(read_only=True)
    socialAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "social_assistance_provider")
    medicalRehabilitationAssistanceProvider = ProviderSerializer(many=True, read_only=True, source ="med_rehab_provider")
    housingAllowanceProvider = ProviderSerializer(many=True, read_only=True, source = "housing_allowance_provider")
    halfwayHouseProvider = ProviderSerializer(many=True, read_only=True, source = "halfway_house_providers")
    shelterProvider = ProviderSerializer(many=True, read_only=True, source = "shelter_provider")
    vocationalTrainingProvider = ProviderSerializer(many=True, read_only=True, source = "vocational_training_provider")
    incomeGeneratingProjectProvider = ProviderSerializer(many=True, read_only=True, source = "micro_ent_income_provider")
    micro_ent_income_project = IncomeProjectTypeSerializer(read_only=True)
    legalAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "legal_assistance_provider")
    medicalAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "medical_assistance_provider")
    financialAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "financial_assistance_provider")
    educationAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "education_assistance_provider")
    education_assistance_level = EducationLevelSerializer(read_only=True)
    immEmmigrationAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "im_emmigration_assistance_provider")
    im_emmigration_assistance_status = ImEmmigrationStatusSerializer(read_only=True)
    communityBasedAssistanceProvider = ProviderSerializer(many=True, read_only=True, source = "other_community_assistance_provider")
    otherCommunityAssistanceType = CommunityAssistanceTypeSerializer(read_only=True)
    interviewer = InterviewerSerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = Assistance
        fields = '__all__'

class SomVictimProfileSerializer(serializers.ModelSerializer):
    citizenship = CountrySerializer(read_only=True)
    countryOfBirth = CountrySerializer(read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    gender = GenderSerializer(read_only=True)
    race = RaceSerializer(read_only=True)
    identification_type = IdTypeSerializer(many=True, read_only=True)
    lastPlaceOfResidence = CountrySerializer(read_only=True)
    interviewCountry = CountrySerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = SomVictimProfile
        fields = '__all__' 
 
class SomVictimProfileWithRelatedSerializer(serializers.ModelSerializer):
    citizenship = CountryNameSerializer(read_only=True)
    countryOfBirth = CountryNameSerializer(read_only=True)
    languages = LanguageNameSerializer(many=True, read_only=True)
    gender = GenderNameSerializer(read_only=True)
    race = RaceNameSerializer(read_only=True)
    identificationType = IdTypeNameSerializer(many=True, read_only=True, source = "identification_type")
    lastPlaceOfResidence = CountryNameSerializer(read_only=True, source = "last_place_of_residence")
    interviewCountry = CountryNameSerializer(read_only=True, source = "interview_country")
    approval = ApprovalStatusNameSerializer(read_only=True)
    # assistance_count = serializers.SerializerMethodField()
    # exploitation_count = serializers.SerializerMethodField()
    # investigations_count = serializers.SerializerMethodField()
    # prosecutions_count = serializers.SerializerMethodField()
    # socio_economic_count = serializers.SerializerMethodField()
    # traffickers_count = serializers.SerializerMethodField()
    # destinations_count = serializers.SerializerMethodField()

    class Meta:
        model = SomVictimProfile
        fields = ["victim_identifier","initials","age","address", 
                  "citizenship","countryOfBirth","languages","gender",
                  "race","identificationType","lastPlaceOfResidence","interviewCountry",
                  "approval","email","interviewDate","additionalRemarks","identificationNumber",
                  "placeOfBirth","interviewLocation"
                  ]

        extra_kwargs = {
            'email': {'source': 'email_address'},
            'interviewDate': {'source': 'interview_date'},
            'additionalRemarks': {'source': 'additional_remarks'},
            'identificationNumber': {'source': 'identification_number'},
            'placeOfBirth': {'source': 'place_of_birth'},
            'interviewLocation': {'source': 'interview_location'},
        }
    
    # def get_assistance_count(self, obj):
    #     return obj.assistance.aggregate(Count('id', distinct=True))['id__count']

    # def get_exploitation_count(self, obj):
    #     return obj.exploitation.aggregate(Count('id', distinct=True))['id__count']

    # def get_investigations_count(self, obj):
    #     return obj.investigations.aggregate(Count('id', distinct=True))['id__count']

    # def get_prosecutions_count(self, obj):
    #     return obj.prosecutions.aggregate(Count('id', distinct=True))['id__count']

    # def get_socio_economic_count(self, obj):
    #     return obj.socio_economic.aggregate(Count('id', distinct=True))['id__count']

    # def get_traffickers_count(self, obj):
    #     return obj.traffickers.aggregate(Count('id', distinct=True))['id__count']

    # def get_destinations_count(self, obj):
    #     return obj.destinations.aggregate(Count('id', distinct=True))['id__count']

class SomCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomCase
        fields = '__all__' 