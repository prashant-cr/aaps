from django.urls import include, path
from rest_framework import routers
from aaps.views import *

router = routers.DefaultRouter()
router.register(r'family', FamilyViewSet)
router.register(r'family-members', FamilyMemberViewSet)
