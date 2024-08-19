from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path, re_path, include
from .views import (AdminViewSet, ServicesViewSet, FeaturesViewSet, OffersViewSet,
                    BlogViewSet, ClientsViewSet, CommentsViewSet, AdvisersViewSet, ReviewsViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Payment API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = routers.DefaultRouter()
router.register(r'services', ServicesViewSet, basename='services')
router.register(r'features', FeaturesViewSet, basename='features')
router.register(r'offers', OffersViewSet, basename='offers')
router.register(r'blogs', BlogViewSet, basename='blogs')
router.register(r'clients', ClientsViewSet, basename='clients')
router.register(r'comments', CommentsViewSet, basename='comments')
router.register(r'advisers', AdvisersViewSet, basename='advisers')
router.register(r'reviews', ReviewsViewSet, basename='reviews')


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    ]
urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
