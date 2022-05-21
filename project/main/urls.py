from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'image_list', ListImageView)
router.register(r'tiers', TiersView)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('api/add_tiers/', AddTiersView.as_view()),
    path('api/user_list/', ListUserView.as_view(), name='user_list'),
    path('api/user_list/<pk>/<str:username>/', DetailUserView.as_view(), name='user_detail'),
]