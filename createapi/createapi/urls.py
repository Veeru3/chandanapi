from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.Productviewset import ProductViewset
router = routers.DefaultRouter()
router.register(r'products', ProductViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
