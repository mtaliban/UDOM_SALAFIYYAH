from rest_framework import viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from vituo.models import College
from vituo.serializers import CollegeBasicSerializer, CollegeDetailSerializer


class CollegeViewSet(viewsets.ModelViewSet):
    """
    College ViewSet - CRUD operations
    
    GET    /colleges/              → List all colleges
    POST   /colleges/              → Create college
    GET    /colleges/?search=UDOM  → Search by name
    GET    /colleges/1/            → Get single college + nested miswallah
    PUT    /colleges/1/            → Update college
    PATCH  /colleges/1/            → Partial update
    DELETE /colleges/1/            → Delete college
    """
    
    queryset = College.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_salafi', 'name'] 
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    
    def get_serializer_class(self):
        """
        Tumiia CollegeDetailSerializer kwa GET single (kwa miswallah nested)
        Tumia CollegeBasicSerializer kwa list, create, update
        """
        # if self.action == 'retrieve':
        #     return CollegeDetailSerializer
        return CollegeDetailSerializer
        # return CollegeBasicSerializer
    
    def get_queryset(self):
        """Filter kwa salafi status kama query parameter inapatikana"""
        queryset = College.objects.all().order_by('name')
        
        # Filter by salafi status
        is_salafi = self.request.query_params.get('is_salafi')
        if is_salafi:
            queryset = queryset.filter(is_salafi=is_salafi.lower() == 'true')
        
        return queryset