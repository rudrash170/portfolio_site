// Single Page Portfolio JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // Scroll Progress Bar
    const scrollProgress = document.querySelector('.scroll-progress');
    
    function updateScrollProgress() {
        const scrollTop = window.pageYOffset;
        const docHeight = document.body.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;
        if (scrollProgress) {
            scrollProgress.style.width = scrollPercent + '%';
        }
    }
    
    window.addEventListener('scroll', updateScrollProgress);
    
    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            navbar.style.background = 'rgba(10, 10, 10, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.3)';
        } else {
            navbar.style.background = 'rgba(10, 10, 10, 0.95)';
            navbar.style.boxShadow = 'none';
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80; // Account for fixed navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add active class to current nav item based on scroll position
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const sections = document.querySelectorAll('section[id]');
    
    window.addEventListener('scroll', function() {
        let current = '';
        const scrollPosition = window.scrollY + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
    
    // Animate elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('.skill-card, .project-card, .achievement-card, .card').forEach(el => {
        observer.observe(el);
    });
    
    // Project filter functionality
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card-wrapper');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const category = this.getAttribute('data-filter');
            
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            // Filter projects
            projectCards.forEach(card => {
                if (category === 'all' || card.getAttribute('data-category') === category) {
                    card.style.display = 'block';
                    card.classList.add('fade-in-up');
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
    
    // Enhanced contact card interactions
    const contactCard = document.querySelector('.contact-info-card');
    if (contactCard) {
        const contactItems = contactCard.querySelectorAll('.contact-item');
        const socialLinks = contactCard.querySelectorAll('.social-links .btn');
        
        // Add ripple effect to contact items
        contactItems.forEach(item => {
            item.addEventListener('click', function(e) {
                if (this.querySelector('a')) return; // Skip if it's a clickable item
                
                const ripple = document.createElement('div');
                ripple.className = 'contact-ripple';
                ripple.style.cssText = `
                    position: absolute;
                    border-radius: 50%;
                    background: rgba(0, 212, 255, 0.3);
                    transform: scale(0);
                    animation: ripple 0.6s linear;
                    pointer-events: none;
                `;
                
                const rect = this.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                ripple.style.width = ripple.style.height = size + 'px';
                ripple.style.left = (e.clientX - rect.left - size / 2) + 'px';
                ripple.style.top = (e.clientY - rect.top - size / 2) + 'px';
                
                this.style.position = 'relative';
                this.appendChild(ripple);
                
                setTimeout(() => ripple.remove(), 600);
            });
        });
        
        // Enhanced hover effects for social links
        socialLinks.forEach(link => {
            link.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-5px) scale(1.15) rotate(5deg)';
            });
            
            link.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1) rotate(0deg)';
            });
            
            // Add click feedback
            link.addEventListener('click', function(e) {
                this.style.transform = 'translateY(-2px) scale(0.95)';
                setTimeout(() => {
                    this.style.transform = 'translateY(-5px) scale(1.15) rotate(5deg)';
                }, 150);
            });
        });
    }
    
    // Add CSS for ripple animation
    const rippleStyle = document.createElement('style');
    rippleStyle.textContent = `
        @keyframes ripple {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(rippleStyle);
    
    // Skill level indicators
    const skillItems = document.querySelectorAll('.skill-card');
    skillItems.forEach(item => {
        // Avoid adding duplicate bars if a progress or a custom bar exists
        if (item.querySelector('.progress, .skill-level-bar')) return;
        const levelBadge = item.querySelector('.badge');
        if (!levelBadge) return;
        const level = (levelBadge.textContent || '').trim();
        const levelBar = document.createElement('div');
        levelBar.className = 'skill-level-bar mt-2';
        levelBar.style.height = '4px';
        levelBar.style.background = '#333';
        levelBar.style.borderRadius = '2px';
        levelBar.style.overflow = 'hidden';
        
        const levelFill = document.createElement('div');
        levelFill.style.height = '100%';
        levelFill.style.transition = 'width 1s ease';
        
        // Set width based on skill level
        switch(level.toLowerCase()) {
            case 'beginner':
                levelFill.style.width = '25%';
                levelFill.style.background = '#ff4757';
                break;
            case 'intermediate':
                levelFill.style.width = '50%';
                levelFill.style.background = '#fbbf24';
                break;
            case 'advanced':
                levelFill.style.width = '75%';
                levelFill.style.background = '#1976d2';
                break;
            case 'expert':
                levelFill.style.width = '100%';
                levelFill.style.background = '#10b981';
                break;
        }
        // Animate skill level bar
        // Animate width on next frame
        requestAnimationFrame(() => {
            levelFill.style.width = levelFill.style.width;
        });
    });
    
    // Add glow effect to cards on hover
    const cards = document.querySelectorAll('.card, .skill-card, .project-card, .achievement-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 20px 40px rgba(0, 212, 255, 0.3)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.5)';
        });
    });
    // Console welcome message
    console.log('%c🌙 Welcome to Rudra\'s Dark Portfolio!', 'color: #00d4ff; font-size: 20px; font-weight: bold;');
    console.log('%c🚀 Built with Django, Bootstrap, and lots of ❤️', 'color: #0099cc; font-size: 14px;');
    // Add particle effect to hero section
    createParticles();
});

// Particle effect function
function createParticles() {
    const heroSection = document.querySelector('.hero-section');
    if (!heroSection) return;
    
    const particleCount = 50;
    const particles = [];
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.cssText = `
            position: absolute;
            width: 2px;
            height: 2px;
            background: rgba(0, 212, 255, 0.5);
            border-radius: 50%;
            pointer-events: none;
            animation: float 6s ease-in-out infinite;
            animation-delay: ${Math.random() * 6}s;
        `;
        
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        
        heroSection.appendChild(particle);
        particles.push(particle);
    }
    
    // Add CSS animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.5; }
            50% { transform: translateY(-20px) rotate(180deg); opacity: 1; }
        }
    `;
    document.head.appendChild(style);
}