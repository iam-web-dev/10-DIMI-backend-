import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import News, AchievementCategory, Achievement, TeamMember, CourseCategory, Course, Feedback, SystemSettings

def seed_data():
    print("Test ma'lumotlari kiritilmoqda...")

    # 1. System Settings
    SystemSettings.objects.get_or_create(id=1, defaults={
        "botToken": "8632538695:AAGrBNDrqUPxpu5N7pzKK8Zpemd0M8kYlS4",
        "chatId": "5046205739",
        "adminLogin": "admin",
        "adminPassword": "admin777"
    })

    # 2. News
    News.objects.create(
        title_uz="Maktabimizda bayram",
        title_ru="Праздник в нашей школе",
        title_en="Holiday at our school",
        short_uz="Bugun maktabimizda katta bayram tadbiri bo'lib o'tdi.",
        short_ru="Сегодня в нашей школе прошло большое праздничное мероприятие.",
        short_en="Today a large festive event was held at our school.",
        desc_uz="Tadbirda barcha o'quvchilar va o'qituvchilar ishtirok etishdi...",
        desc_ru="В мероприятии приняли участие все учащиеся и учителя...",
        desc_en="All students and teachers took part in the event...",
        views=120
    )

    # 3. Achievement Categories
    sport_cat, _ = AchievementCategory.objects.get_or_create(key="sport", defaults={"name_uz": "Sport", "name_ru": "Спорт", "name_en": "Sport"})
    edu_cat, _ = AchievementCategory.objects.get_or_create(key="education", defaults={"name_uz": "Ta'lim", "name_ru": "Образование", "name_en": "Education"})

    # 4. Achievements
    Achievement.objects.create(
        category=sport_cat,
        title_uz="Futbol bo'yicha 1-o'rin",
        title_ru="1-е место по футболу",
        title_en="1st place in football",
        desc_uz="Viloyat bosqichida jamoamiz g'olib bo'ldi.",
        desc_ru="Наша команда победила на областном этапе.",
        desc_en="Our team won the regional stage."
    )

    # 5. Team
    TeamMember.objects.create(
        name_uz="Alisher Toshmatov",
        name_ru="Алишер Тошматов",
        name_en="Alisher Toshmatov",
        pos_uz="Maktab direktori",
        pos_ru="Директор школы",
        pos_en="School Director"
    )

    # 6. Course Categories
    it_cat, _ = CourseCategory.objects.get_or_create(key="it", defaults={"name_uz": "IT", "name_ru": "IT", "name_en": "IT"})

    # 7. Courses
    Course.objects.create(
        category=it_cat,
        name_uz="Web Dasturlash",
        name_ru="Веб-программирование",
        name_en="Web Programming",
        desc_uz="Frontend va Backend asoslari",
        desc_ru="Основы Frontend и Backend",
        desc_en="Frontend and Backend basics",
        teacher_uz="Botir Ergashev",
        teacher_ru="Ботир Эргашев",
        teacher_en="Botir Ergashev",
        time_uz="14:00 - 16:00",
        time_ru="14:00 - 16:00",
        time_en="14:00 - 16:00",
        level_uz="Boshlang'ich",
        level_ru="Начальный",
        level_en="Beginner",
        room_uz="201-xona",
        room_ru="201-комната",
        room_en="Room 201"
    )

    # 8. Feedbacks
    Feedback.objects.create(
        name_uz="Malika Axmedova",
        name_ru="Малика Ахмедова",
        name_en="Malika Axmedova",
        role_uz="Ota-ona",
        role_ru="Родитель",
        role_en="Parent",
        content_uz="Maktabdagi sharoitlar juda yaxshi, o'qituvchilar doimo e'tiborli.",
        content_ru="Условия в школе очень хорошие, учителя всегда внимательны.",
        content_en="The school conditions are very good, teachers are always attentive."
    )


    print("Barcha test ma'lumotlari muvaffaqiyatli kiritildi!")

if __name__ == "__main__":
    seed_data()
