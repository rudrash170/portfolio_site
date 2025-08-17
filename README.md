# 🚀 Rudra's Portfolio - Cloud & DevOps Engineer

A modern, responsive portfolio website built with Django showcasing expertise in cloud computing, DevOps automation, and Python development.

## ✨ Features

- **Modern Design**: Beautiful, responsive UI with Bootstrap 5 and custom CSS
- **Dynamic Content**: Database-driven content management through Django admin
- **Interactive Elements**: Smooth animations, filtering, and interactive components
- **Mobile-First**: Fully responsive design that works on all devices
- **SEO Optimized**: Clean URLs and meta tags for better search engine visibility

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Icons**: Font Awesome 6
- **Fonts**: Inter & JetBrains Mono (Google Fonts)

## 📱 Pages

1. **Home** - Hero section, featured projects, skills preview
2. **About** - Personal information, experience, education
3. **Projects** - Portfolio showcase with filtering by category
4. **Skills** - Technical skills organized by category
5. **Achievements** - Certifications, awards, and milestones
6. **Contact** - Contact form and information

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Populate with sample data**
   ```bash
   python manage.py populate_portfolio
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Open in browser**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📊 Sample Data

The portfolio comes pre-populated with sample data including:

- **6 Projects** across different categories (Cloud, DevOps, Web Development)
- **25+ Skills** organized by category with proficiency levels
- **4 Achievements** including certifications and awards
- **2 Experience entries** showing career progression
- **1 Education entry** with academic details

## 🎨 Customization

### Content Management
- Use Django admin panel to manage all content
- Add/edit projects, skills, achievements, experience, and education
- Upload project images and resume files

### Styling
- Custom CSS variables in `static/css/style.css`
- Easy color scheme modification
- Responsive breakpoints for different screen sizes

### Adding New Skills
```python
# In Django admin or via management command
Skill.objects.create(
    name="New Technology",
    level="intermediate",
    category="cloud",
    icon="fas fa-icon-name"
)
```

## 🔧 Management Commands

### Populate Portfolio
```bash
python manage.py populate_portfolio
```
Creates sample data for all models.

### Custom Commands
Located in `core/management/commands/` for easy data management.

## 📁 Project Structure

```
portfolio/
├── core/                    # Main app
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── admin.py            # Admin interface
│   ├── forms.py            # Forms
│   └── management/         # Management commands
├── templates/               # HTML templates
│   └── core/               # App-specific templates
├── static/                  # Static files
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript
│   └── images/             # Images
├── media/                   # User-uploaded files
└── portfolio/              # Project settings
    ├── settings.py         # Django settings
    ├── urls.py             # Main URL configuration
    └── wsgi.py             # WSGI configuration
```

## 🌟 Key Features

### Responsive Design
- Mobile-first approach
- Bootstrap 5 grid system
- Custom CSS animations and transitions

### Interactive Elements
- Smooth scrolling navigation
- Project filtering by category
- Skill level indicators
- Contact form with validation

### Performance
- Optimized static files
- Efficient database queries
- Lazy loading for images

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False`
2. Configure production database
3. Set up static file serving
4. Configure media file storage
5. Set `ALLOWED_HOSTS`

### Recommended Hosting
- **Heroku**: Easy Django deployment
- **AWS**: EC2 with RDS and S3
- **DigitalOcean**: Droplet with managed database
- **Vercel**: Frontend hosting with Django API

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- **Portfolio**: [Your Portfolio URL]
- **Email**: [Your Email]
- **LinkedIn**: [Your LinkedIn]
- **GitHub**: [Your GitHub]

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive CSS framework
- Font Awesome for the beautiful icons
- All contributors and supporters

---

**Built with ❤️ by Rudra** - Cloud & DevOps Engineer graduating in 2026 # portfolio_site
