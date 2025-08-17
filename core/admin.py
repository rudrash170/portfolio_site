from django.contrib import admin
from .models import Project, Skill, Achievement, ContactMessage, Resume, Experience, Education

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'created_at']
    list_filter = ['category', 'featured', 'created_at']
    search_fields = ['title', 'description', 'tech_stack']
    list_editable = ['featured']
    prepopulated_fields = {'title': ('title',)}

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'category']
    list_filter = ['level', 'category']
    search_fields = ['name']
    list_editable = ['level', 'category']

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'issuer', 'date']
    list_filter = ['category', 'date']
    search_fields = ['title', 'description', 'issuer']
    date_hierarchy = 'date'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['read']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'uploaded_at']
    list_filter = ['is_active', 'uploaded_at']
    search_fields = ['title']
    list_editable = ['is_active']
    readonly_fields = ['uploaded_at']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'start_date']
    search_fields = ['title', 'company', 'description']
    list_editable = ['current']
    date_hierarchy = 'start_date'

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'current', 'gpa']
    list_filter = ['current', 'start_date']
    search_fields = ['degree', 'institution', 'description']
    list_editable = ['current']
    date_hierarchy = 'start_date'
