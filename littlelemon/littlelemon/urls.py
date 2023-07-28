from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("admin/", admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/bookings/', include(router.urls))
]
