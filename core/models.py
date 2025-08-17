
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=[
        ('cloud', 'Cloud & DevOps'),
        ('web', 'Web Development'),
        ('automation', 'Automation'),
        ('data', 'Data Science'),
        ('other', 'Other')
    ], default='other')
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert')
    ], default='intermediate')
    category = models.CharField(max_length=50, choices=[
        ('cloud', 'Cloud Platforms'),
        ('devops', 'DevOps Tools'),
        ('programming', 'Programming Languages'),
        ('frameworks', 'Frameworks & Libraries'),
        ('databases', 'Databases'),
        ('tools', 'Tools & Platforms')
    ], default='programming')
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")
    
    def __str__(self):
        return f"{self.name} ({self.level})"
    
    class Meta:
        ordering = ['category', 'name']

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    certificate_url = models.URLField(blank=True, null=True)
    issuer = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=50, choices=[
        ('certification', 'Certification'),
        ('competition', 'Competition'),
        ('project', 'Project Award'),
        ('academic', 'Academic'),
        ('other', 'Other')
    ], default='other')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, default="Portfolio Contact")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']

class Resume(models.Model):
    title = models.CharField(max_length=100, default="Resume")
    file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title} - {self.uploaded_at.strftime('%Y-%m-%d')}"
    
    class Meta:
        ordering = ['-uploaded_at']

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    technologies = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"
    
    class Meta:
        ordering = ['-start_date']
