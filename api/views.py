import json
import urllib.request
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-date')
    serializer_class = NewsSerializer

class AchievementCategoryViewSet(viewsets.ModelViewSet):
    queryset = AchievementCategory.objects.all()
    serializer_class = AchievementCategorySerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class CourseCategoryViewSet(viewsets.ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ContactRequestViewSet(viewsets.ModelViewSet):
    queryset = ContactRequest.objects.all().order_by('-created_at')
    serializer_class = ContactRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        
        # Telegramga xabar yuborish
        settings = SystemSettings.objects.first()
        if settings and settings.botToken and settings.chatId:
            token = settings.botToken
            chat_ids = [cid.strip() for cid in settings.chatId.split(',') if cid.strip()]
            text = (
                f"âœ¨â€¢ Yangi ariza!\n\n"
                f"ðŸ‘¤ Ism: {instance.name}\n"
                f"ðŸ“– Tel: {instance.phone}\n"
                f"ðŸ’¬ Xabar: {instance.message or 'Xabar yoq'}"
            )
            
            for cid in chat_ids:
                try:
                    url = f"https://api.telegram.org/bot{token}/sendMessage"
                    data = json.dumps({"chat_id": cid, "text": text}).encode('utf-8')
                    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
                    with urllib.request.urlopen(req) as response:
                        pass
                except Exception as e:
                    print(f"Telegram error: {e}")

class SystemSettingsViewSet(viewsets.ModelViewSet):
    queryset = SystemSettings.objects.all()
    serializer_class = SystemSettingsSerializer

    def get_queryset(self):
        # Always return only the first settings object
        if not SystemSettings.objects.exists():
            SystemSettings.objects.create()
        return SystemSettings.objects.all()[:1]
