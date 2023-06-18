from django.contrib import admin

from cv.models import Experience, Skil, Education, Contacts, Cv


class ExperienceInline(admin.TabularInline):
    model = Experience


class SkilInline(admin.TabularInline):
    model = Skil


class EducationInline(admin.TabularInline):
    model = Education


class ContactsInline(admin.TabularInline):
    model = Contacts


@admin.register(Cv)
class CvAdmin(admin.ModelAdmin):
    inlines = [ExperienceInline, SkilInline, EducationInline, ContactsInline]
