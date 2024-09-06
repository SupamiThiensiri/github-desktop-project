from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apis.views.v1.school import SchoolViewSet
from apis.views.v1.classroom import ClassroomViewSet
from apis.views.v1.teacher import TeacherViewSet
from apis.views.v1.student import StudentViewSet

# กำหนด Router สำหรับ API
router = DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('v1/', include(router.urls)), 
]


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# api_v1_urls = (router.urls, 'v1')

# urlpatterns = [
#     path('v1/', include(api_v1_urls))
# ]
