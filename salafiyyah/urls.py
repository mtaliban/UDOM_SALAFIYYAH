from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # API Routes - Include vituo app URLs
    path('api/', include('vituo.urls')),
    
    # DRF Default Routes (optional - for API root)
    path('api-auth/', include('rest_framework.urls')),
]

# ============================================
# FULL API ENDPOINTS:
# ============================================
#
# ROOT API URLS:
# GET    /api/                   → API Root (list all endpoints)
# GET    /api/colleges/          → List colleges
# GET    /api/muswallah/         → List muswallah
# GET    /api/facilities/        → List facilities
#
# AUTH (optional):
# GET    /api-auth/login/        → DRF login
# GET    /api-auth/logout/       → DRF logout
#
# ADMIN:
# GET    /admin/                 → Django Admin Panel
#
# ============================================