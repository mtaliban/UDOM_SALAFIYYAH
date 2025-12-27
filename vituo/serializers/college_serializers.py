from rest_framework import serializers
from vituo.models import College
from .muswallah_serializers import MuswallahNestedSerializer


class CollegeBasicSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = College
        fields = ['college_id', 'name', 'is_salafi']
        read_only_fields = ['college_id']
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Jina lazima kuwa na herufi 3+")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Jina lazima kuwa na herufi tu")
        return value.strip().title()


class CollegeDetailSerializer(serializers.ModelSerializer):
    """College + miswallah nested"""
    
    miswallah = MuswallahNestedSerializer(many=True, read_only=True)
    total_miswallah = serializers.SerializerMethodField()
    salafi_miswallah = serializers.SerializerMethodField()
    non_salafi_miswallah = serializers.SerializerMethodField()
    
    class Meta:
        model = College
        fields = ['college_id', 'name', 'is_salafi', 'miswallah','total_miswallah', 'salafi_miswallah', 'non_salafi_miswallah']
        read_only_fields = ['college_id', 'miswallah']


    def get_total_miswallah(self, obj):
        return obj.miswallah.count()
    
    def get_salafi_miswallah(self, obj):
        return obj.miswallah.filter(is_salafi=True).count()
    
    def get_non_salafi_miswallah(self, obj):
        return obj.miswallah.filter(is_salafi=False).count()
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Jina lazima kuwa na herufi 3+")
        if not value.replace(" ", "").isalpha():
            raise serializers.ValidationError("Jina lazima kuwa na herufi tu")
        return value.strip().title()