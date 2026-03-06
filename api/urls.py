from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'achievements', AchievementViewSet)
router.register(r'achievements-categories', AchievementCategoryViewSet)
router.register(r'team', TeamMemberViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'courses-categories', CourseCategoryViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'contact', ContactRequestViewSet)
router.register(r'settings', SystemSettingsViewSet, basename='settings')

urlpatterns = [
    path('', include(router.urls)),
]
