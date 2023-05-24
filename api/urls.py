from django.urls import path
from api import views as v

urlpatterns = [
    # ... other URL patterns ...
    path("/",v.home),
    
    # Catch-all pattern for non-existing URLs
    path('<path:not_found>/', v.error_view),
]