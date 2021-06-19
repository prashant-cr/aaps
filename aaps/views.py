from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from aaps.serializers import FamilySerializer, FamilyMembersSerializer
from aaps.models import Family, FamilyMember


class FamilyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Family.objects.all().order_by('id')
    serializer_class = FamilySerializer
    permission_classes = [permissions.IsAuthenticated]


class FamilyMemberViewSet(viewsets.ModelViewSet):

    queryset = FamilyMember.objects.all().order_by('id')
    serializer_class = FamilyMembersSerializer

    permission_classes = [permissions.IsAuthenticated]
