from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from core.models import Project, Skill, Achievement, Experience, Education, Resume

class Command(BaseCommand):
    help = 'Populate the portfolio with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample portfolio data...')
        
        # Create Skills
        skills_data = [
            # Cloud Platforms
            {'name': 'AWS', 'level': 'intermediate', 'category': 'cloud', 'icon': 'fab fa-aws'},
            {'name': 'Azure', 'level': 'intermediate', 'category': 'cloud', 'icon': 'fab fa-microsoft'},
            {'name': 'Google Cloud', 'level': 'beginner', 'category': 'cloud', 'icon': 'fab fa-google'},
            {'name': 'Kubernetes', 'level': 'beginner', 'category': 'cloud', 'icon': 'fab fa-docker'},
            
            # DevOps Tools
            {'name': 'Docker', 'level': 'intermediate', 'category': 'devops', 'icon': 'fab fa-docker'},
            {'name': 'Terraform', 'level': 'intermediate', 'category': 'devops', 'icon': 'fas fa-code'},
            {'name': 'Jenkins', 'level': 'intermediate', 'category': 'devops', 'icon': 'fab fa-jenkins'},
            {'name': 'GitLab CI/CD', 'level': 'intermediate', 'category': 'devops', 'icon': 'fab fa-gitlab'},
            {'name': 'Ansible', 'level': 'beginner', 'category': 'devops', 'icon': 'fas fa-cogs'},
            
            # Programming Languages
            {'name': 'Python', 'level': 'advanced', 'category': 'programming', 'icon': 'fab fa-python'},
            {'name': 'JavaScript', 'level': 'intermediate', 'category': 'programming', 'icon': 'fab fa-js-square'},
            {'name': 'Bash', 'level': 'intermediate', 'category': 'programming', 'icon': 'fas fa-terminal'},
            {'name': 'YAML', 'level': 'intermediate', 'category': 'programming', 'icon': 'fas fa-file-code'},
            
            # Frameworks & Libraries
            {'name': 'Django', 'level': 'intermediate', 'category': 'frameworks', 'icon': 'fab fa-python'},
            {'name': 'Flask', 'level': 'intermediate', 'category': 'frameworks', 'icon': 'fab fa-python'},
            {'name': 'React', 'level': 'beginner', 'category': 'frameworks', 'icon': 'fab fa-react'},
            {'name': 'Bootstrap', 'level': 'intermediate', 'category': 'frameworks', 'icon': 'fab fa-bootstrap'},
            
            # Databases
            {'name': 'PostgreSQL', 'level': 'intermediate', 'category': 'databases', 'icon': 'fas fa-database'},
            {'name': 'MongoDB', 'level': 'beginner', 'category': 'databases', 'icon': 'fas fa-database'},
            {'name': 'Redis', 'level': 'beginner', 'category': 'databases', 'icon': 'fas fa-database'},
            
            # Tools & Platforms
            {'name': 'Git', 'level': 'advanced', 'category': 'tools', 'icon': 'fab fa-git-alt'},
            {'name': 'Linux', 'level': 'intermediate', 'category': 'tools', 'icon': 'fab fa-linux'},
            {'name': 'VSCode', 'level': 'intermediate', 'category': 'tools', 'icon': 'fas fa-code'},
            {'name': 'Postman', 'level': 'intermediate', 'category': 'tools', 'icon': 'fas fa-paper-plane'},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')
        
        # Create Projects
        projects_data = [
            {
                'title': 'Cloud Infrastructure Automation',
                'description': 'Automated AWS infrastructure deployment using Terraform and Ansible. Implemented CI/CD pipelines with Jenkins and created monitoring dashboards with CloudWatch.',
                'tech_stack': 'AWS Terraform Ansible Jenkins Python CloudWatch',
                'category': 'cloud',
                'featured': True,
                'github_link': 'https://github.com/rudra/cloud-automation',
                'live_link': 'https://demo.cloud-automation.com'
            },
            {
                'title': 'DevOps Pipeline Automation',
                'description': 'Built comprehensive CI/CD pipelines for microservices architecture. Integrated automated testing, security scanning, and deployment strategies.',
                'tech_stack': 'Docker Kubernetes Jenkins GitLab Python',
                'category': 'automation',
                'featured': True,
                'github_link': 'https://github.com/rudra/devops-pipeline'
            },
            {
                'title': 'Python Web Application',
                'description': 'Full-stack web application built with Django and React. Features user authentication, real-time updates, and responsive design.',
                'tech_stack': 'Python Django React PostgreSQL Redis',
                'category': 'web',
                'featured': False,
                'github_link': 'https://github.com/rudra/python-web-app',
                'live_link': 'https://python-web-app.herokuapp.com'
            },
            {
                'title': 'Infrastructure Monitoring Dashboard',
                'description': 'Real-time monitoring dashboard for cloud infrastructure using Python, Flask, and various AWS services.',
                'tech_stack': 'Python Flask AWS CloudWatch Grafana',
                'category': 'cloud',
                'featured': False,
                'github_link': 'https://github.com/rudra/monitoring-dashboard'
            },
            {
                'title': 'Automated Backup System',
                'description': 'Automated backup solution for databases and file systems with scheduling, encryption, and cloud storage integration.',
                'tech_stack': 'Python AWS S3 Bash Cron Encryption',
                'category': 'automation',
                'featured': False,
                'github_link': 'https://github.com/rudra/backup-system'
            },
            {
                'title': 'Container Orchestration Platform',
                'description': 'Kubernetes-based platform for managing containerized applications with automated scaling and load balancing.',
                'tech_stack': 'Kubernetes Docker Helm Python Prometheus',
                'category': 'cloud',
                'featured': False,
                'github_link': 'https://github.com/rudra/container-platform'
            }
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created project: {project.title}')
        
        # Create Achievements
        achievements_data = [
            {
                'title': 'AWS Cloud Practitioner',
                'description': 'Certified in AWS Cloud fundamentals and best practices',
                'issuer': 'Amazon Web Services',
                'category': 'certification',
                'date': date(2024, 6, 15)
            },
            {
                'title': 'Python Programming Excellence',
                'description': 'Awarded for outstanding performance in Python programming course',
                'issuer': 'University Computer Science Department',
                'category': 'academic',
                'date': date(2024, 3, 20)
            },
            {
                'title': 'Hackathon Winner',
                'description': 'First place in university hackathon for innovative cloud solution',
                'issuer': 'University Tech Club',
                'category': 'competition',
                'date': date(2024, 2, 10)
            },
            {
                'title': 'DevOps Best Practices',
                'description': 'Completed advanced DevOps course with hands-on projects',
                'issuer': 'Online Learning Platform',
                'category': 'certification',
                'date': date(2024, 1, 15)
            }
        ]
        
        for achievement_data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                title=achievement_data['title'],
                defaults=achievement_data
            )
            if created:
                self.stdout.write(f'Created achievement: {achievement.title}')
        
        # Create Experience
        experience_data = [
            {
                'title': 'Cloud Engineering Intern',
                'company': 'Tech Solutions Inc.',
                'location': 'Remote',
                'start_date': date(2024, 5, 1),
                'current': True,
                'description': 'Working on cloud infrastructure automation and DevOps practices. Implementing CI/CD pipelines and monitoring solutions.',
                'technologies': 'AWS Terraform Jenkins Python Docker'
            },
            {
                'title': 'Student Developer',
                'company': 'University Projects',
                'location': 'University Campus',
                'start_date': date(2023, 9, 1),
                'current': True,
                'description': 'Developing various projects including web applications, automation scripts, and cloud solutions.',
                'technologies': 'Python Django React AWS Docker'
            }
        ]
        
        for exp_data in experience_data:
            experience, created = Experience.objects.get_or_create(
                title=exp_data['title'],
                company=exp_data['company'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Created experience: {experience.title}')
        
        # Create Education
        education_data = [
            {
                'degree': 'Bachelor of Science in Computer Science',
                'institution': 'University of Technology',
                'location': 'India',
                'start_date': date(2022, 8, 1),
                'current': True,
                'gpa': 3.8,
                'description': 'Focusing on cloud computing, DevOps, and software engineering. Active in tech clubs and hackathons.'
            }
        ]
        
        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                degree=edu_data['degree'],
                institution=edu_data['institution'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'Created education: {education.degree}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated portfolio with sample data!')
        ) 