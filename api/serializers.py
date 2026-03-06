from rest_framework import serializers
from .models import *

class NewsMediaSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    type = serializers.CharField(source='media_type')
    
    class Meta:
        model = NewsMedia
        fields = ['type', 'url']
        
    def get_url(self, obj):
        if obj.media_type == 'image' and obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url) if 'request' in self.context else obj.image.url
        return obj.video_url

class NewsSerializer(serializers.ModelSerializer):
    uz = serializers.SerializerMethodField()
    ru = serializers.SerializerMethodField()
    en = serializers.SerializerMethodField()
    media = NewsMediaSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'image', 'date', 'views', 'uz', 'ru', 'en', 'media', 'title_uz', 'title_ru', 'title_en', 'short_uz', 'short_ru', 'short_en', 'desc_uz', 'desc_ru', 'desc_en']
        extra_kwargs = {
            'title_uz': {'write_only': True}, 'title_ru': {'write_only': True}, 'title_en': {'write_only': True},
            'short_uz': {'write_only': True}, 'short_ru': {'write_only': True}, 'short_en': {'write_only': True},
            'desc_uz': {'write_only': True}, 'desc_ru': {'write_only': True}, 'desc_en': {'write_only': True},
        }

    def get_image(self, obj):
        if not obj.image: return None
        request = self.context.get('request')
        if request: return request.build_absolute_uri(obj.image.url)
        return obj.image.url

    def get_uz(self, obj): return {"title": obj.title_uz, "shortDescription": obj.short_uz, "description": obj.desc_uz}
    def get_ru(self, obj): return {"title": obj.title_ru, "shortDescription": obj.short_ru, "description": obj.desc_ru}
    def get_en(self, obj): return {"title": obj.title_en, "shortDescription": obj.short_en, "description": obj.desc_en}



class AchievementCategorySerializer(serializers.ModelSerializer):
    uz = serializers.SerializerMethodField()
    ru = serializers.SerializerMethodField()
    en = serializers.SerializerMethodField()
    class Meta:
        model = AchievementCategory
        fields = ['id', 'key', 'uz', 'ru', 'en', 'name_uz', 'name_ru', 'name_en']
        extra_kwargs = {'name_uz': {'write_only': True}, 'name_ru': {'write_only': True}, 'name_en': {'write_only': True}}
    def get_uz(self, obj): return obj.name_uz
    def get_ru(self, obj): return obj.name_ru
    def get_en(self, obj): return obj.name_en

class AchievementSerializer(serializers.ModelSerializer):
    uz = serializers.SerializerMethodField()
    ru = serializers.SerializerMethodField()
    en = serializers.SerializerMethodField()
    categoryKey = serializers.ReadOnlyField(source='category.key')

    class Meta:
        model = Achievement
        fields = ['id', 'category', 'categoryKey', 'image', 'typeMap', 'uz', 'ru', 'en', 'title_uz', 'title_ru', 'title_en', 'desc_uz', 'desc_ru', 'desc_en']
        extra_kwargs = {
            'title_uz': {'write_only': True}, 'title_ru': {'write_only': True}, 'title_en': {'write_only': True},
            'desc_uz': {'write_only': True}, 'desc_ru': {'write_only': True}, 'desc_en': {'write_only': True},
        }
    def get_uz(self, obj): return {"title": obj.title_uz, "description": obj.desc_uz}
    def get_ru(self, obj): return {"title": obj.title_ru, "description": obj.desc_ru}
    def get_en(self, obj): return {"title": obj.title_en, "description": obj.desc_en}


class TeamMemberSerializer(serializers.ModelSerializer):
    uz = serializers.SerializerMethodField()
    ru = serializers.SerializerMethodField()
    en = serializers.SerializerMethodField()
    class Meta:
        model = TeamMember
        fields = ['id', 'image', 'uz', 'ru', 'en', 'name_uz', 'name_ru', 'name_en', 'pos_uz', 'pos_ru', 'pos_en']
        extra_kwargs = {
            'name_uz': {'write_only': True}, 'name_ru': {'write_only': True}, 'name_en': {'write_only': True},
            'pos_uz': {'write_only': True}, 'pos_ru': {'write_only': True}, 'pos_en': {'write_only': True},
        }
    def get_uz(self, obj): return {"name": obj.name_uz, "position": obj.pos_uz}
    def get_ru(self, obj): return {"name": obj.name_ru, "position": obj.pos_ru}
    def get_en(self, obj): return {"name": obj.name_en, "position": obj.pos_en}

class CourseCategorySerializer(serializers.ModelSerializer):
    uz = serializers.SerializerMethodField()
    ru = serializers.SerializerMethodField()
    en = serializers.SerializerMethodField()
    class Meta:
        model = CourseCategory
        fields = ['id', 'key', 'uz', 'ru', 'en', 'name_uz', 'name_ru', 'name_en']
        extra_kwargs = {'name_uz': {'write_only': True}, 'name_ru': {'write_only': True}, 'name_en': {'write_only': True}}
    def get_uz(self, obj): return obj.name_uz
    def get_ru(self, obj): return obj.name_ru
    def get_en(self, obj): return obj.name_en

class CourseSerializer(serializers.ModelSerializer):
    uz = serializers.SerializerMethodField()
    ru = serializers.SerializerMethodField()
    en = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id', 'category', 'image', 'uz', 'ru', 'en', 
                  'name_uz', 'name_ru', 'name_en', 'desc_uz', 'desc_ru', 'desc_en',
                  'teacher_uz', 'teacher_ru', 'teacher_en', 'time_uz', 'time_ru', 'time_en',
                  'level_uz', 'level_ru', 'level_en', 'room_uz', 'room_ru', 'room_en']
        extra_kwargs = {f"{field}_{lang}": {'write_only': True} for field in ['name', 'desc', 'teacher', 'time', 'level', 'room'] for lang in ['uz', 'ru', 'en']}

    def get_uz(self, obj): return {"name": obj.name_uz, "description": obj.desc_uz, "teacher": obj.teacher_uz, "time": obj.time_uz, "level": obj.level_uz, "room": obj.room_uz}
    def get_ru(self, obj): return {"name": obj.name_ru, "description": obj.desc_ru, "teacher": obj.teacher_ru, "time": obj.time_ru, "level": obj.level_ru, "room": obj.room_ru}
    def get_en(self, obj): return {"name": obj.name_en, "description": obj.desc_en, "teacher": obj.teacher_en, "time": obj.time_en, "level": obj.level_en, "room": obj.room_en}

class FeedbackSerializer(serializers.ModelSerializer):
    uz = serializers.SerializerMethodField()
    ru = serializers.SerializerMethodField()
    en = serializers.SerializerMethodField()
    class Meta:
        model = Feedback
        fields = ['id', 'image', 'uz', 'ru', 'en', 'name_uz', 'name_ru', 'name_en', 'role_uz', 'role_ru', 'role_en', 'content_uz', 'content_ru', 'content_en']
        extra_kwargs = {f"{f}_{l}": {'write_only': True} for f in ['name', 'role', 'content'] for l in ['uz', 'ru', 'en']}
    def get_uz(self, obj): return {"name": obj.name_uz, "role": obj.role_uz, "content": obj.content_uz}
    def get_ru(self, obj): return {"name": obj.name_ru, "role": obj.role_ru, "content": obj.content_ru}
    def get_en(self, obj): return {"name": obj.name_en, "role": obj.role_en, "content": obj.content_en}


class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ['id', 'name', 'phone', 'message', 'created_at']

class SystemSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSettings
        fields = '__all__'
