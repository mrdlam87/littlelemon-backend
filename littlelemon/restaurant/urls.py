from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'restaurant'

urlpatterns = [
    path('', views.index, name='home'),
    path('api/menu-items/', views.MenuItemsView.as_view()),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
