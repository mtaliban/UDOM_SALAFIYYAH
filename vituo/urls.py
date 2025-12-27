from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vituo.views import (
    CollegeViewSet,
    MuswallahViewSet,
    ExternalIslamicFacilityViewSet,
)

# Initialize Router
router = DefaultRouter()

# Register ViewSets
# DefaultRouter automatically creates all CRUD URLs
router.register(r'colleges', CollegeViewSet, basename='college')
router.register(r'muswallah', MuswallahViewSet, basename='muswallah')
router.register(r'facilities', ExternalIslamicFacilityViewSet, basename='facility')

# URL Patterns
urlpatterns = [
    # Include all router URLs
    path('', include(router.urls)),
]

# ============================================
# AUTO-GENERATED URLS BY ROUTER:
# ============================================
#
# COLLEGE URLS:
# GET    /colleges/              → List colleges
# POST   /colleges/              → Create college
# GET    /colleges/1/            → Get single college
# PUT    /colleges/1/            → Update college
# PATCH  /colleges/1/            → Partial update
# DELETE /colleges/1/            → Delete college
#
# WITH FILTERS:
# GET    /colleges/?search=UDOM
# GET    /colleges/?is_salafi=true
# GET    /colleges/?ordering=name
#
# ============================================
#
# MUSWALLAH URLS:
# GET    /muswallah/             → List muswallah
# POST   /muswallah/             → Create muswallah
# GET    /muswallah/1/           → Get single muswallah
# PUT    /muswallah/1/           → Update muswallah
# PATCH  /muswallah/1/           → Partial update
# DELETE /muswallah/1/           → Delete muswallah
#
# WITH FILTERS:
# GET    /muswallah/?search=Noor
# GET    /muswallah/?college=1
# GET    /muswallah/?is_salafi=true
# GET    /muswallah/?ordering=name
#
# EXTRA ACTIONS (AUTO-GENERATED FROM @action):
# GET    /muswallah/by-college/1/          → Get by college
# GET    /muswallah/by-college/1/?is_salafi=true
# GET    /muswallah/salafi/                → Only salafi
# GET    /muswallah/salafi/?college=1
# GET    /muswallah/non-salafi/            → Only non-salafi
# GET    /muswallah/count/                 → Count total
# GET    /muswallah/count/?college=1
# GET    /muswallah/count/?is_salafi=true
#
# ============================================
#
# FACILITY URLS:
# GET    /facilities/            → List facilities
# POST   /facilities/            → Create facility
# GET    /facilities/1/          → Get single facility
# PUT    /facilities/1/          → Update facility
# PATCH  /facilities/1/          → Partial update
# DELETE /facilities/1/          → Delete facility
#
# WITH FILTERS:
# GET    /facilities/?search=Markaz
# GET    /facilities/?college=1
# GET    /facilities/?ordering=name
#
# ============================================