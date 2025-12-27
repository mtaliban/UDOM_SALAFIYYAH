from rest_framework import viewsets, filters
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from vituo.models import Muswallah, College
from vituo.serializers import (
    MuswallahSerializer,
    MuswallahCountSerializer,
)


class MuswallahViewSet(viewsets.ModelViewSet):
    """
    Muswallah ViewSet - CRUD + extra actions
    
    STANDARD CRUD:
    GET    /muswallah/              → List all muswallah
    POST   /muswallah/              → Create muswallah
    GET    /muswallah/?search=Noor  → Search by name
    GET    /muswallah/?is_salafi=true → Filter by salafi
    GET    /muswallah/?college=1    → Filter by college
    GET    /muswallah/1/            → Get single muswallah
    PUT    /muswallah/1/            → Update muswallah
    PATCH  /muswallah/1/            → Partial update
    DELETE /muswallah/1/            → Delete muswallah
    
    EXTRA ACTIONS:
    GET    /muswallah/by-college/1/          → Get muswallah by college
    GET    /muswallah/salafi/                → Get only salafi
    GET    /muswallah/non-salafi/            → Get only non-salafi
    GET    /muswallah/count/                 → Count statistics
    """
    
    queryset = Muswallah.objects.all().order_by('name')
    serializer_class = MuswallahSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_salafi', 'name'] 
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']
    
    def get_queryset(self):
        """Filter kwa college na salafi status"""
        queryset = Muswallah.objects.all().order_by('name')
        return queryset
    
    @action(detail=False, methods=['get'], url_path='by-college/(?P<college_id>[0-9]+)')
    def by_college(self, request, college_id=None):
        """
        GET /muswallah/by-college/1/ → Get muswallah ya college fulani
        GET /muswallah/by-college/1/?is_salafi=true → + Filter by salafi
        """
        queryset = Muswallah.objects.filter(college_id=college_id).order_by('name')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
  
    
  
    
 
