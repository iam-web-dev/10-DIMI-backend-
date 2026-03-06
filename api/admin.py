from django.contrib import admin
from django.utils.html import format_html
from .models import *

def get_image_preview(obj, size=100):
    if hasattr(obj, 'image') and obj.image:
        return format_html('<img src="{}" style="max-height: {}px; border-radius: 5px;" />', obj.image.url, size)
    return "Rasm yo'q"

class NewsMediaInline(admin.TabularInline):
    model = NewsMedia
    extra = 1
    fields = ('media_type', 'image', 'image_preview', 'video_url')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return get_image_preview(obj, size=50)
    image_preview.short_description = "Ko'rinishi"

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview_list', 'title_uz', 'date', 'views')
    search_fields = ('title_uz', 'title_ru', 'title_en')
    inlines = [NewsMediaInline]
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return get_image_preview(obj, 200)
    
    def image_preview_list(self, obj):
        return get_image_preview(obj, 40)
    image_preview_list.short_description = "Rasm"

@admin.register(AchievementCategory)
class AchievementCategoryAdmin(admin.ModelAdmin):
    list_display = ('key', 'name_uz')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview_list', 'title_uz', 'category')
    list_filter = ('category',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return get_image_preview(obj, 200)
    
    def image_preview_list(self, obj):
        return get_image_preview(obj, 40)
    image_preview_list.short_description = "Rasm"

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview_list', 'name_uz', 'pos_uz')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return get_image_preview(obj, 200)
    
    def image_preview_list(self, obj):
        return get_image_preview(obj, 40)
    image_preview_list.short_description = "Rasm"

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('key', 'name_uz')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview_list', 'name_uz', 'category', 'teacher_uz')
    list_filter = ('category',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return get_image_preview(obj, 200)
    
    def image_preview_list(self, obj):
        return get_image_preview(obj, 40)
    image_preview_list.short_description = "Rasm"

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview_list', 'name_uz', 'role_uz')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return get_image_preview(obj, 200)
    
    def image_preview_list(self, obj):
        return get_image_preview(obj, 40)
    image_preview_list.short_description = "Rasm"

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'phone', 'message')

@admin.register(SystemSettings)
class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = ('botToken', 'chatId', 'phoneNumber', 'telegramLink')
