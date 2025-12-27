from rest_framework import serializers
from vituo.models import Muswallah


class MuswallahNestedSerializer(serializers.ModelSerializer):
    """Muswallah nested kwenye college"""
    
    class Meta:
        model = Muswallah
        fields = ['muswallah_id', 'name', 'is_salafi']
        read_only_fields = ['muswallah_id']
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Jina lazima kuwa na herufi 3+")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Jina lazima kuwa na herufi tu")
        return value.strip().title()


class MuswallahSerializer(serializers.ModelSerializer):
    """Muswallah standalone (with college info)"""
    
    college_name = serializers.CharField(source='college.name', read_only=True)
    
    class Meta:
        model = Muswallah
        fields = ['muswallah_id', 'name', 'is_salafi', 'college', 'college_name']
        read_only_fields = ['muswallah_id', 'college_name']
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Jina lazima kuwa na herufi 3+")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Jina lazima kuwa na herufi tu")
        return value.strip().title()


class MuswallahCountSerializer(serializers.Serializer):
    """Custom serializer for muswallah count statistics"""
    
    count = serializers.IntegerField(read_only=True)
    college = serializers.IntegerField(required=False, allow_null=True)
    college_name = serializers.CharField(required=False, allow_null=True)
    is_salafi = serializers.BooleanField(required=False, allow_null=True)