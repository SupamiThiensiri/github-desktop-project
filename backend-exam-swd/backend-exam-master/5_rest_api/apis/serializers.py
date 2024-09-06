from rest_framework import serializers
from .models import *

class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(source='classrooms.count', read_only=True)
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'abbreviation', 'address', 'classroom_count', 'teacher_count', 'student_count']

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()

class ClassroomSerializer(serializers.ModelSerializer):
    teachers = serializers.StringRelatedField(many=True)
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = Classroom
        fields = ['id', 'grade', 'section', 'school', 'teachers', 'students']  # แก้ไขจาก 'year' เป็น 'grade'

class TeacherSerializer(serializers.ModelSerializer):
    classrooms = serializers.StringRelatedField(many=True)

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender', 'classrooms']  # แก้ไข 'firstname' เป็น 'first_name'

class StudentSerializer(serializers.ModelSerializer):
    classroom = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom']  # แก้ไข 'firstname' เป็น 'first_name'
