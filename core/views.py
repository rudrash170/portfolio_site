from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from .models import Project, Skill, Achievement, ContactMessage, Resume, Experience, Education
from .forms import ContactForm

def home(request):
    """Home page view with featured content"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    recent_projects = Project.objects.all()[:6]
    skills = Skill.objects.all()
    achievements = Achievement.objects.all()[:5]
    
    context = {
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
        'skills': skills,
        'achievements': achievements,
    }
    return render(request, 'core/home.html', context)

def single_page(request):
    """Single page portfolio view with all content"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    projects = Project.objects.all()
    skills = Skill.objects.all()
    achievements = Achievement.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    resume = Resume.objects.filter(is_active=True).first()
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'featured_projects': featured_projects,
        'projects': projects,
        'skills_by_category': skills_by_category,
        'achievements': achievements,
        'experience': experience,
        'education': education,
        'resume': resume,
    }
    return render(request, 'core/single_page.html', context)

def about(request):
    """About page view with personal information"""
    experience = Experience.objects.all()
    education = Education.objects.all()
    resume = Resume.objects.filter(is_active=True).first()
    
    context = {
        'experience': experience,
        'education': education,
        'resume': resume,
    }
    return render(request, 'core/about.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Project.objects.all()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Project.objects.values_list('category', flat=True).distinct()
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'core/project_detail.html'
    context_object_name = 'project'

def skills(request):
    """Skills page view grouped by category"""
    skills_by_category = {}
    for skill in Skill.objects.all():
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'skills_by_category': skills_by_category,
    }
    return render(request, 'core/skills.html', context)

def achievements(request):
    """Achievements page view"""
    achievements = Achievement.objects.all()
    
    context = {
        'achievements': achievements,
    }
    return render(request, 'core/achievements.html', context)

def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)
