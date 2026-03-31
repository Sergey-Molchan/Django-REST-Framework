from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PaymentListAPIView, MyTokenObtainPairView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
