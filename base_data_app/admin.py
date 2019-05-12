from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Slider, Contacts, AboutUs, News, CompanyNumbers, Team, Reviews, Partners, FaqCategory, \
    Faq, Features, Logo, Services, Department, DepartmentSlider, FeedBack


class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = Slider


class AboutUsAdmin(admin.ModelAdmin):
    model = AboutUs

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return True
        else:
            return False


class ContactsAdmin(admin.ModelAdmin):
    model = Contacts

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return True
        else:
            return False


class FeaturesAdmin(admin.ModelAdmin):
    save_as = True


class NewsAdmin(admin.ModelAdmin):
    module = News
    list_display = ('title',)


class FaqAdmin(admin.ModelAdmin):
    module = Faq


class FaqCategoryAdmin(admin.ModelAdmin):
    module = FaqCategory


class TeamAdmin(admin.ModelAdmin):
    module = Team


class ReviewsAdmin(admin.ModelAdmin):
    module = Reviews


class CompanyNumbersAdmin(admin.ModelAdmin):
    module = CompanyNumbers


class LogoAdmin(admin.ModelAdmin):
    module = Logo


admin.site.register(Slider, SliderAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(CompanyNumbers, CompanyNumbersAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Partners)
admin.site.register(FaqCategory, FaqCategoryAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(FeedBack)
admin.site.register(Services)
admin.site.register(Department)
admin.site.register(DepartmentSlider)
