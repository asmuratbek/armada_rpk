from geoposition.fields import GeopositionField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

class Logo(models.Model):
    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'

    image = models.ImageField(upload_to='images/logos', verbose_name='Логотипы')

class Contacts(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон', null=True, blank=True)
    phone_2 = models.CharField(max_length=255, verbose_name='Телефон-2', null=True, blank=True)
    phone_3 = models.CharField(max_length=255, verbose_name='Телефон-3', null=True, blank=True)
    email = models.CharField(max_length=255, verbose_name='Email', null=True, blank=True)
    facebook = models.CharField(max_length=255, verbose_name='Facebook', null=True, blank=True)
    instagram = models.CharField(max_length=255, verbose_name='Instagram', null=True, blank=True)
    youtube = models.CharField(max_length=255, verbose_name='Youtube', null=True, blank=True)
    whatsapp = models.CharField(max_length=255, verbose_name='Whatsapp', null=True, blank=True)
    work_time = models.CharField(max_length=255, verbose_name='Режим работы', null=True, blank=True)
    location = GeopositionField(verbose_name='Маркер на карте', null=True, blank=True)

    def __unicode__(self):
        return 'Контакты'


class ContactsPhone(models.Model):
    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    phone = models.CharField(max_length=255, verbose_name='Телефон')
    contact = models.ForeignKey(Contacts, verbose_name='Контакт', on_delete=models.CASCADE)


class Slider(models.Model):
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'
        ordering = ('order',)

    title = models.CharField(max_length=255, verbose_name='Название слайдера')
    image = models.ImageField(upload_to='images/slider', verbose_name='Изображение', null=True, blank=True)
    video = models.FileField(upload_to='images/videos', verbose_name='Загрузите Видео', null=True, blank=True)
    text = models.TextField(verbose_name='Текст на слайде', null=True, blank=True)
    order = models.PositiveIntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.title


class News(models.Model):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=255, verbose_name='Название новости')
    image = models.ImageField(upload_to='images/news', blank=True, null=True, verbose_name='Изображение новости')
    anons = RichTextUploadingField(max_length=255, verbose_name='Короткое описание', null=True, blank=True)
    text = RichTextUploadingField(verbose_name='Текст новости')
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.title


class Blog(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    title = models.CharField(max_length=255, verbose_name='Название новости')
    image = models.ImageField(upload_to='images/news', blank=True, null=True, verbose_name='Изображение новости')
    anons = RichTextUploadingField(max_length=255, verbose_name='Короткое описание', null=True, blank=True)
    text = RichTextUploadingField(verbose_name='Текст новости')
    date = models.DateTimeField(auto_now_add=True, null=True)


class AboutUs(models.Model):
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    title = models.CharField(max_length=255, verbose_name='О нас')
    text = RichTextUploadingField(verbose_name='Текст о нас')

    def __unicode__(self):
        return self.title


class CompanyNumbers(models.Model):
    class Meta:
        verbose_name = 'Цифра'
        verbose_name_plural = 'Цифры'

    title = models.CharField(max_length=255, verbose_name='Название')
    number = models.CharField(max_length=255, verbose_name='Цифры')

    def __unicode__(self):
        return self.title


class Team(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = "Команда"

    title = models.CharField(max_length=255, verbose_name='Имя сотрудника')
    position = models.CharField(max_length=255, verbose_name='Позиция')
    image = models.ImageField(upload_to='images/avatar', verbose_name='Фото сотрудника', null=True, blank=True)
    info = models.TextField(max_length=150, verbose_name='Доп инфо 150 символов', null=True, blank=True)

    def __unicode__(self):
        return self.title


class Reviews(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    name = models.CharField(max_length=255, verbose_name='ФИО')
    image = models.ImageField(upload_to='images/reviews', verbose_name='Аватарка', null=True, blank=True)
    video = models.CharField(max_length=255, verbose_name='Видео отзыв', null=True, blank=True)
    text = RichTextUploadingField(verbose_name='Текст')
    location_of_review = models.CharField(max_length=255, verbose_name='Страна получения отзыва', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.name


class Partners(models.Model):
    class Meta:
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'

    title = models.CharField(max_length=255, verbose_name='Название компании')
    image = models.ImageField(upload_to='images/partners', verbose_name='Логотип партнеров')

    def __unicode__(self):
        return self.title


class FaqCategory(models.Model):
    class Meta:
        verbose_name = 'Категория Вопроса'
        verbose_name_plural = "Категория Вопросов"

    title = models.CharField(max_length=255, verbose_name='Название категории')
    icon = models.ImageField(max_length=255, verbose_name='Иконка изображения', null=True)

    def __unicode__(self):
        return self.title


class Faq(models.Model):
    class Meta:
        verbose_name = 'Вопрос-Ответ'
        verbose_name_plural = 'Вопросы-Ответы'
        ordering = ('order',)

    category = models.ForeignKey(FaqCategory, verbose_name='Выберите категорию', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, verbose_name='Вопрос')
    text = RichTextUploadingField(verbose_name='Ответ')
    order = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=255, verbose_name='Название категории')
    is_menu = models.BooleanField(default=False)



class FeedBack(models.Model):
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    email = models.CharField(max_length=255, verbose_name='Email')
    message = models.TextField(verbose_name='Комментарий')

    def __unicode__(self):
        return self.name + '-' + self.last_name



class Features(models.Model):
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(upload_to='images/features_icon', verbose_name='Иконка', null=True, blank=True)
    text = models.TextField(max_length=200, verbose_name='Текс')

    def __unicode__(self):
        return self.title