from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import School
from apis.serializers import SchoolSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
