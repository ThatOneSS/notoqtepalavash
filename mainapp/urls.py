from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet,BranchViewSet

router=DefaultRouter()
router.register("category",CategoryViewSet,basename="category")
router.register("product",ProductViewSet,basename="product")
router.register("branch",BranchViewSet,basename="branch")
urlpatterns = [
    path("",include(router.urls)),
]