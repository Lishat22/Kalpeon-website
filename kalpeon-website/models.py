"""
Database Models for Kalpeon Website
Using SQLAlchemy ORM
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

# ==================== ADMIN USER MODEL ====================

class Admin(UserMixin, db.Model):
    """Admin user model for authentication"""
    __tablename__ = 'admin'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if password matches hash"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<Admin {self.username}>'

# ==================== NEWS MODEL ====================

class News(db.Model):
    """News articles model"""
    __tablename__ = 'news'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.String(200), default='news_default.jpg')
    is_published = db.Column(db.Boolean, default=True)
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'date': self.date.strftime('%Y-%m-%d') if self.date else '',
            'image': self.image,
            'is_published': self.is_published
        }
    
    def __repr__(self):
        return f'<News {self.title}>'

# ==================== INDUSTRY MODEL ====================

class Industry(db.Model):
    """Industries model"""
    __tablename__ = 'industry'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(50), default='briefcase')
    image = db.Column(db.String(200), default='industry_default.jpg')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'icon': self.icon
        }
    
    def __repr__(self):
        return f'<Industry {self.name}>'

# ==================== SERVICE MODEL ====================

class Service(db.Model):
    """Services model"""
    __tablename__ = 'service'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(50), default='star')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'icon': self.icon
        }
    
    def __repr__(self):
        return f'<Service {self.title}>'

# ==================== JOB MODEL ====================

class Job(db.Model):
    """Job postings model"""
    __tablename__ = 'job'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(50), default='Full-time')  # Full-time, Part-time, Contract
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=True)
    salary_range = db.Column(db.String(100), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship to job applications
    applications = db.relationship('JobApplication', back_populates='job', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'department': self.department,
            'location': self.location,
            'type': self.job_type
        }
    
    def __repr__(self):
        return f'<Job {self.title}>'

# ==================== TEAM MEMBER MODEL ====================

class TeamMember(db.Model):
    """Team members model"""
    __tablename__ = 'team_member'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(200), default='member_default.jpg')
    email = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    twitter = db.Column(db.String(100), nullable=True)
    linkedin = db.Column(db.String(100), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<TeamMember {self.name}>'

# ==================== CONTACT FORM SUBMISSION MODEL ====================

class Contact(db.Model):
    """Contact form submissions model"""
    __tablename__ = 'contact'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    subject = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    is_responded = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Contact {self.name}>'

# ==================== WEBSITE SETTINGS MODEL ====================

class WebsiteSettings(db.Model):
    """Website configuration and settings"""
    __tablename__ = 'website_settings'
    
    id = db.Column(db.Integer, primary_key=True)
    site_title = db.Column(db.String(200), default='Kalpeon Group of Industry')
    site_description = db.Column(db.Text, default='Leading Multinational Conglomerate')
    site_logo = db.Column(db.String(200), default='logo.png')
    company_phone = db.Column(db.String(20), default='+91 (0) 22-XXXX-XXXX')
    company_email = db.Column(db.String(120), default='info@kalpeon.com')
    company_address = db.Column(db.Text, default='Mumbai, India')
    company_years = db.Column(db.Integer, default=30)
    company_employees = db.Column(db.Integer, default=500000)
    company_countries = db.Column(db.Integer, default=50)
    facebook_url = db.Column(db.String(200), default='#')
    twitter_url = db.Column(db.String(200), default='#')
    linkedin_url = db.Column(db.String(200), default='#')
    instagram_url = db.Column(db.String(200), default='#')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return '<WebsiteSettings>'

# ==================== APPLICATION SUBMISSION MODEL ====================

class JobApplication(db.Model):
    """Job application submissions"""
    __tablename__ = 'job_application'
    
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    job_title = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    message = db.Column(db.Text, nullable=True)
    resume = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), default='pending')  # pending, reviewed, accepted, rejected
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    job = db.relationship('Job', back_populates='applications')
    
    def __repr__(self):
        return f'<JobApplication {self.name} for {self.job_title}>'
