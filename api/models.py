from django.db import models

class News(models.Model):
    image = models.ImageField(upload_to='news/', null=True, blank=True, verbose_name="Asosiy rasm (Preview)")
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    
    title_uz = models.CharField(max_length=255, verbose_name="Sarlavha (UZ)", default="")
    title_ru = models.CharField(max_length=255, verbose_name="Sarlavha (RU)", null=True, blank=True, default="")
    title_en = models.CharField(max_length=255, verbose_name="Sarlavha (EN)", null=True, blank=True, default="")
    
    short_uz = models.TextField(verbose_name="Qisqa tavsif (UZ)", default="")
    short_ru = models.TextField(verbose_name="Qisqa tavsif (RU)", null=True, blank=True, default="")
    short_en = models.TextField(verbose_name="Qisqa tavsif (EN)", null=True, blank=True, default="")
    
    desc_uz = models.TextField(verbose_name="To'liq tavsif (UZ)", default="")
    desc_ru = models.TextField(verbose_name="To'liq tavsif (RU)", null=True, blank=True, default="")
    desc_en = models.TextField(verbose_name="To'liq tavsif (EN)", null=True, blank=True, default="")

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

class NewsMedia(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='media')
    MEDIA_TYPES = [('image', 'Rasm'), ('video', 'Video (YouTube)')]
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='image')
    image = models.ImageField(upload_to='news/media/', null=True, blank=True, verbose_name="Rasm yuklash")
    video_url = models.URLField(null=True, blank=True, verbose_name="YouTube havola (URL)")

    def __str__(self):
        return f"{self.news.title_uz[:20]} - {self.media_type}"


class AchievementCategory(models.Model):
    key = models.CharField(max_length=100, unique=True)
    name_uz = models.CharField(max_length=255, verbose_name="Nomi (UZ)", default="")
    name_ru = models.CharField(max_length=255, verbose_name="Nomi (RU)", null=True, blank=True, default="")
    name_en = models.CharField(max_length=255, verbose_name="Nomi (EN)", null=True, blank=True, default="")

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Yutuq kategoriyasi"
        verbose_name_plural = "Yutuq kategoriyalari"


class Achievement(models.Model):
    category = models.ForeignKey(AchievementCategory, on_delete=models.CASCADE, related_name='achievements')
    image = models.ImageField(upload_to='achievements/', null=True, blank=True)
    typeMap = models.CharField(max_length=20, default="portrait", choices=[("portrait", "Tik"), ("landscape", "Yotiq")])
    
    title_uz = models.CharField(max_length=255, verbose_name="Sarlavha (UZ)", default="")
    title_ru = models.CharField(max_length=255, verbose_name="Sarlavha (RU)", null=True, blank=True, default="")
    title_en = models.CharField(max_length=255, verbose_name="Sarlavha (EN)", null=True, blank=True, default="")
    
    desc_uz = models.TextField(verbose_name="Tavsif (UZ)", null=True, blank=True, default="")
    desc_ru = models.TextField(verbose_name="Tavsif (RU)", null=True, blank=True, default="")
    desc_en = models.TextField(verbose_name="Tavsif (EN)", null=True, blank=True, default="")

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Yutuq"
        verbose_name_plural = "Yutuqlar"

class TeamMember(models.Model):
    image = models.ImageField(upload_to='team/', null=True, blank=True)
    name_uz = models.CharField(max_length=255, verbose_name="Ism (UZ)", default="")
    name_ru = models.CharField(max_length=255, verbose_name="Ism (RU)", null=True, blank=True, default="")
    name_en = models.CharField(max_length=255, verbose_name="Ism (EN)", null=True, blank=True, default="")
    
    pos_uz = models.CharField(max_length=255, verbose_name="Lavozim (UZ)", default="")
    pos_ru = models.CharField(max_length=255, verbose_name="Lavozim (RU)", null=True, blank=True, default="")
    pos_en = models.CharField(max_length=255, verbose_name="Lavozim (EN)", null=True, blank=True, default="")

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Jamoa a'zolari"

class CourseCategory(models.Model):
    key = models.CharField(max_length=100, unique=True)
    name_uz = models.CharField(max_length=255, verbose_name="Nomi (UZ)", default="")
    name_ru = models.CharField(max_length=255, verbose_name="Nomi (RU)", null=True, blank=True, default="")
    name_en = models.CharField(max_length=255, verbose_name="Nomi (EN)", null=True, blank=True, default="")

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Kurs kategoriyasi"
        verbose_name_plural = "Kurs kategoriyalari"


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    
    name_uz = models.CharField(max_length=255, verbose_name="Nomi (UZ)", default="")
    name_ru = models.CharField(max_length=255, verbose_name="Nomi (RU)", null=True, blank=True, default="")
    name_en = models.CharField(max_length=255, verbose_name="Nomi (EN)", null=True, blank=True, default="")
    
    desc_uz = models.TextField(verbose_name="Tavsif (UZ)", default="")
    desc_ru = models.TextField(verbose_name="Tavsif (RU)", null=True, blank=True, default="")
    desc_en = models.TextField(verbose_name="Tavsif (EN)", null=True, blank=True, default="")
    
    teacher_uz = models.CharField(max_length=255, verbose_name="O'qituvchi (UZ)", default="")
    teacher_ru = models.CharField(max_length=255, verbose_name="O'qituvchi (RU)", null=True, blank=True, default="")
    teacher_en = models.CharField(max_length=255, verbose_name="O'qituvchi (EN)", null=True, blank=True, default="")
    
    time_uz = models.CharField(max_length=255, verbose_name="Vaqti (UZ)", default="")
    time_ru = models.CharField(max_length=255, verbose_name="Vaqti (RU)", null=True, blank=True, default="")
    time_en = models.CharField(max_length=255, verbose_name="Vaqti (EN)", null=True, blank=True, default="")
    
    level_uz = models.CharField(max_length=255, verbose_name="Darajasi (UZ)", default="")
    level_ru = models.CharField(max_length=255, verbose_name="Darajasi (RU)", null=True, blank=True, default="")
    level_en = models.CharField(max_length=255, verbose_name="Darajasi (EN)", null=True, blank=True, default="")
    
    room_uz = models.CharField(max_length=255, verbose_name="Xona (UZ)", default="")
    room_ru = models.CharField(max_length=255, verbose_name="Xona (RU)", null=True, blank=True, default="")
    room_en = models.CharField(max_length=255, verbose_name="Xona (EN)", null=True, blank=True, default="")

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"

class Feedback(models.Model):
    image = models.ImageField(upload_to='feedbacks/', null=True, blank=True)
    
    name_uz = models.CharField(max_length=255, verbose_name="Ism (UZ)", default="")
    name_ru = models.CharField(max_length=255, verbose_name="Ism (RU)", null=True, blank=True, default="")
    name_en = models.CharField(max_length=255, verbose_name="Ism (EN)", null=True, blank=True, default="")
    
    role_uz = models.CharField(max_length=255, verbose_name="Roli (UZ)", default="")
    role_ru = models.CharField(max_length=255, verbose_name="Roli (RU)", null=True, blank=True, default="")
    role_en = models.CharField(max_length=255, verbose_name="Roli (EN)", null=True, blank=True, default="")
    
    content_uz = models.TextField(verbose_name="Fikr (UZ)", default="")
    content_ru = models.TextField(verbose_name="Fikr (RU)", null=True, blank=True, default="")
    content_en = models.TextField(verbose_name="Fikr (EN)", null=True, blank=True, default="")

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Fikr-mulohaza"
        verbose_name_plural = "Fikr-mulohazalar"


class ContactRequest(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ism")
    phone = models.CharField(max_length=50, verbose_name="Telefon")
    message = models.TextField(verbose_name="Xabar", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqti")
    is_processed = models.BooleanField(default=False, verbose_name="Ko'rib chiqildi")

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = "Bog'lanish arizasi"
        verbose_name_plural = "Bog'lanish arizalari"




class SystemSettings(models.Model):
    botToken = models.CharField(max_length=255, verbose_name="Telegram Bot Token", default="8632538695:AAGrBNDrqUPxpu5N7pzKK8Zpemd0M8kYlS4")
    chatId = models.CharField(max_length=255, verbose_name="Telegram Chat ID (vergul bilan bir nechta)", default="5046205739")
    
    phoneNumber = models.CharField(max_length=50, verbose_name="Bog'lanish uchun telefon", default="+998 (90) 123 45 67")
    telegramLink = models.URLField(verbose_name="Telegram kanal", default="https://t.me/10dimi")
    instagramLink = models.URLField(verbose_name="Instagram sahifa", default="https://instagram.com/10dimi")
    youtubeLink = models.URLField(verbose_name="YouTube kanal", default="https://youtube.com/10dimi")

    def __str__(self):
        return "Tizim sozlamalari"

    class Meta:
        verbose_name = "Tizim sozlamasi"
        verbose_name_plural = "Tizim sozlamalari"
