from rest_framework import viewsets, filters
from vituo.models import ExternalIslamicFacility
from vituo.serializers import ExternalIslamicFacilitySerializer
from django_filters.rest_framework import DjangoFilterBackend


class ExternalIslamicFacilityViewSet(viewsets.ModelViewSet):
    """
    External Islamic Facility ViewSet - CRUD operations
    
    GET    /facilities/                → List all facilities
    POST   /facilities/                → Create facility
    GET    /facilities/?search=Markaz  → Search by name
    GET    /facilities/?college=1      → Filter by college
    GET    /facilities/1/              → Get single facility
    PUT    /facilities/1/              → Update facility
    PATCH  /facilities/1/              → Partial update
    DELETE /facilities/1/              → Delete facility
    """
    
    queryset = ExternalIslamicFacility.objects.all().order_by('name')
    serializer_class = ExternalIslamicFacilitySerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'location']
    filterset_fields = ['name','location'] 
    ordering_fields = ['name', 'location', 'created_at']
    
    def get_queryset(self):
        """Filter kwa college kama query parameter inapatikana"""
        queryset = ExternalIslamicFacility.objects.all().order_by('name')
        
        # Filter by college
        college = self.request.query_params.get('college')
        if college:
            queryset = queryset.filter(college_id=college)
        
        return queryset