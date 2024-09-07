from django.urls import path
from django.views.generic import RedirectView

from .views import (
    CourseListCreate,
    CourseDetail,
    CourseInstanceCreate,
    CourseInstanceList,
    CourseInstanceDetail
)

urlpatterns = [
    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('instances/', CourseInstanceCreate.as_view(), name='course-instance-create'),
    path('instances/<int:year>/<int:semester>/', CourseInstanceList.as_view(), name='course-instance-list'),
    path('instances/<int:year>/<int:semester>/<int:instance_id>/', CourseInstanceDetail.as_view(), name='course-instance-detail'),
]
