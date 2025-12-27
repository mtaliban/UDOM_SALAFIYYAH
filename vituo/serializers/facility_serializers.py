from rest_framework import serializers
from vituo.models import ExternalIslamicFacility


class ExternalIslamicFacilitySerializer(serializers.ModelSerializer):
    """External Islamic Facility"""
    
    college_name = serializers.CharField(source='college.name', read_only=True, allow_null=True)
    
    class Meta:
        model = ExternalIslamicFacility
        fields = ['facility_id', 'name', 'location', 'college', 'college_name']
        read_only_fields = ['facility_id', 'college_name']
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Jina lazima kuwa na herufi 3+")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Jina lazima kuwa na herufi tu")
        return value.strip().title()
    
    def validate_location(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Location lazima kuwa na herufi 3+")
        return value.strip()