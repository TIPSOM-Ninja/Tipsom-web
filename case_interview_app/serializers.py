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

class VictimProfileSerializer(serializers.ModelSerializer):
    citizenship = CountrySerializer(read_only=True)
    countryOfBirth = CountrySerializer(read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    gender = GenderSerializer(read_only=True)
    race = RaceSerializer(read_only=True)
    identification_type = IdTypeSerializer(many=True, read_only=True)
    last_place_of_residence = CountrySerializer(read_only=True)
    interview_country = CountrySerializer(read_only=True)
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
    social_assistance_provider = ProviderSerializer(many=True, read_only=True)
    med_rehab_provider = ProviderSerializer(many=True, read_only=True)
    housing_allowance_provider = ProviderSerializer(many=True, read_only=True)
    halfway_house_providers = ProviderSerializer(many=True, read_only=True)
    shelter_provider = ProviderSerializer(many=True, read_only=True)
    vocational_training_provider = ProviderSerializer(many=True, read_only=True)
    micro_ent_income_provider = ProviderSerializer(many=True, read_only=True)
    micro_ent_income_project = IncomeProjectTypeSerializer(read_only=True)
    legal_assistance_provider = ProviderSerializer(many=True, read_only=True)
    medical_assistance_provider = ProviderSerializer(many=True, read_only=True)
    financial_assistance_provider = ProviderSerializer(many=True, read_only=True)
    education_assistance_provider = ProviderSerializer(many=True, read_only=True)
    education_assistance_level = EducationLevelSerializer(read_only=True)
    im_emmigration_assistance_provider = ProviderSerializer(many=True, read_only=True)
    im_emmigration_assistance_status = ImEmmigrationStatusSerializer(read_only=True)
    other_community_assistance_provider = ProviderSerializer(many=True, read_only=True)
    other_community_assistance_type = CommunityAssistanceTypeSerializer(read_only=True)
    interviewer = InterviewerSerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = Assistance
        fields = '__all__'

class SocioEconomicSerializer(serializers.ModelSerializer):
    victim = VictimProfileSerializer(read_only=True)
    family_structure = FamilyStructureSerializer(read_only=True)
    living_with = LivingWithSerializer(read_only=True)
    education_level = EducationLevelSerializer(read_only=True)
    last_occupation = OccupationSerializer(many=True, read_only=True)
    interviewer = InterviewerSerializer(read_only=True)
    approval = ApprovalStatusSerializer(read_only=True)

    class Meta:
        model = SocioEconomic
        fields = '__all__'


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