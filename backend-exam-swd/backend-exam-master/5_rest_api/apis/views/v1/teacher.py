from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apis.models import Teacher
from apis.serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['firstname', 'lastname', 'gender', 'classrooms__school']
