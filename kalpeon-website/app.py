"""
Kalpeon Group of Industry - Flask Application with Database
Complete website with admin dashboard for content management
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Admin, News, Industry, Service, Job, TeamMember, Contact, WebsiteSettings, JobApplication
from datetime import datetime
import os

app = Flask(__name__)

# ==================== CONFIGURATION ====================

# Ensure instance folder exists and set correct database path
instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
os.makedirs(instance_path, exist_ok=True)

db_path = os.path.join(instance_path, 'kalpeon.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'kalpeon-secret-key-2026'
app.config['SESSION_COOKIE_SECURE'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'
login_manager.login_message = 'Please log in to access the admin dashboard'

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

# ==================== DATABASE INITIALIZATION ====================

def init_database():
    """Initialize database with default data"""
    with app.app_context():
        db.create_all()
        
        # Create default admin if doesn't exist
        if not Admin.query.first():
            admin = Admin(
                username='admin',
                email='admin@kalpeon.com'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✓ Default admin created (username: admin, password: admin123)")
        
        # Create default website settings if doesn't exist
        if not WebsiteSettings.query.first():
            settings = WebsiteSettings()
            db.session.add(settings)
            db.session.commit()
            print("✓ Website settings created")
        
        # Create sample industries if empty
        if Industry.query.count() == 0:
            sample_industries = [
                Industry(name='Manufacturing', description='Advanced manufacturing facilities with ISO certifications', icon='industry'),
                Industry(name='Technology', description='IT Solutions and digital transformation services', icon='laptop'),
                Industry(name='Energy', description='Renewable and sustainable energy solutions', icon='bolt'),
                Industry(name='Pharmaceuticals', description='Healthcare and pharmaceutical research & development', icon='flask'),
                Industry(name='Real Estate', description='Commercial and residential development projects', icon='building'),
                Industry(name='Logistics', description='Global supply chain and logistics management', icon='truck'),
            ]
            for ind in sample_industries:
                db.session.add(ind)
            db.session.commit()
            print("✓ Sample industries created")
        
        # Create sample services if empty
        if Service.query.count() == 0:
            sample_services = [
                Service(title='Consulting Services', description='Expert business consulting for strategic growth'),
                Service(title='Infrastructure Development', description='State-of-the-art infrastructure solutions'),
                Service(title='Technology Integration', description='Digital transformation and IT modernization'),
                Service(title='Supply Chain Solutions', description='Efficient and scalable supply chain management'),
            ]
            for svc in sample_services:
                db.session.add(svc)
            db.session.commit()
            print("✓ Sample services created")
        
        # Create sample news if empty
        if News.query.count() == 0:
            sample_news = [
                News(
                    title='Kalpeon Expands to Asia-Pacific Region',
                    content='We are thrilled to announce our expansion into the Asia-Pacific region with new offices in Singapore, Tokyo, and Mumbai.',
                    date=datetime.utcnow()
                ),
                News(
                    title='Sustainability Initiative Launched',
                    content='Kalpeon Group commits to achieving carbon neutrality by 2030 with major investments in renewable energy.',
                    date=datetime.utcnow()
                ),
            ]
            for news in sample_news:
                db.session.add(news)
            db.session.commit()
            print("✓ Sample news created")

# ==================== PUBLIC ROUTES ====================

@app.route('/')
def index():
    """Home page"""
    featured_news = News.query.filter_by(is_published=True).order_by(News.date.desc()).limit(2).all()
    return render_template('index.html', featured_news=featured_news)

@app.route('/about')
def about():
    """About Us page"""
    team = TeamMember.query.filter_by(is_active=True).all()
    return render_template('about.html', team=team)

@app.route('/industries')
def industries():
    """Industries page"""
    industries_list = Industry.query.filter_by(is_active=True).all()
    return render_template('industries.html', industries=industries_list)

@app.route('/services')
def services():
    """Services page"""
    services_list = Service.query.filter_by(is_active=True).all()
    return render_template('services.html', services=services_list)

@app.route('/news')
def news():
    """News page"""
    all_news = News.query.filter_by(is_published=True).order_by(News.date.desc()).all()
    return render_template('news.html', news=all_news)

@app.route('/news/<int:news_id>')
def news_detail(news_id):
    """Individual news page"""
    news_item = News.query.get_or_404(news_id)
    if not news_item.is_published:
        return "News not found", 404
    news_item.views += 1
    db.session.commit()
    return render_template('news_detail.html', news=news_item)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact Us page"""
    if request.method == 'POST':
        return handle_contact_form()
    return render_template('contact.html')

def handle_contact_form():
    """Process contact form submission"""
    try:
        data = {
            'name': request.form.get('name', '').strip(),
            'email': request.form.get('email', '').strip(),
            'phone': request.form.get('phone', '').strip(),
            'subject': request.form.get('subject', '').strip(),
            'message': request.form.get('message', '').strip(),
        }
        
        if not all([data['name'], data['email'], data['message']]):
            return jsonify({'success': False, 'error': 'Please fill all required fields'}), 400
        
        contact = Contact(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            subject=data['subject'],
            message=data['message']
        )
        db.session.add(contact)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Thank you! Your message has been received. We will contact you soon.'
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/careers')
def careers():
    """Careers page"""
    jobs = Job.query.filter_by(is_active=True).all()
    return render_template('careers.html', jobs=jobs)

@app.route('/gallery')
def gallery():
    """Gallery page"""
    gallery_items = [
        {"title": "Manufacturing Plant", "category": "facilities", "image": "gallery1.jpg"},
        {"title": "Corporate Office", "category": "facilities", "image": "gallery2.jpg"},
        {"title": "Team Event", "category": "events", "image": "gallery3.jpg"},
        {"title": "Product Launch", "category": "events", "image": "gallery4.jpg"}
    ]
    return render_template('gallery.html', items=gallery_items)

@app.route('/sitemap')
def sitemap():
    """Sitemap page"""
    return render_template('sitemap.html')

@app.route('/api/newsletter', methods=['POST'])
def api_newsletter():
    """Newsletter subscription endpoint"""
    try:
        email = request.form.get('email', '').strip()
        if not email:
            return jsonify({'success': False, 'error': 'Email required'}), 400
        return jsonify({'success': True, 'message': 'Subscribed successfully!'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ==================== ADMIN AUTHENTICATION ====================

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        admin = Admin.query.filter_by(username=username).first()
        
        if admin and admin.check_password(password):
            login_user(admin, remember=request.form.get('remember') == 'on')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    """Admin logout"""
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('admin_login'))

# ==================== ADMIN DASHBOARD ====================

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """Admin dashboard main page"""
    stats = {
        'total_news': News.query.count(),
        'total_contacts': Contact.query.count(),
        'new_contacts': Contact.query.filter_by(is_read=False).count(),
        'total_jobs': Job.query.count(),
        'total_industries': Industry.query.count(),
        'total_services': Service.query.count(),
        'total_team': TeamMember.query.count(),
    }
    
    recent_contacts = Contact.query.order_by(Contact.created_at.desc()).limit(5).all()
    recent_news = News.query.order_by(News.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html', stats=stats, recent_contacts=recent_contacts, recent_news=recent_news)

# ==================== ADMIN - NEWS MANAGEMENT ====================

@app.route('/admin/news')
@login_required
def admin_news_list():
    """List all news articles"""
    page = request.args.get('page', 1, type=int)
    news_list = News.query.order_by(News.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('admin/news_list.html', news=news_list)

@app.route('/admin/news/new', methods=['GET', 'POST'])
@login_required
def admin_news_create():
    """Create new news article"""
    if request.method == 'POST':
        try:
            news = News(
                title=request.form.get('title'),
                content=request.form.get('content'),
                is_published=request.form.get('is_published') == 'on'
            )
            db.session.add(news)
            db.session.commit()
            flash(f'News "{news.title}" created successfully!', 'success')
            return redirect(url_for('admin_news_list'))
        except Exception as e:
            flash(f'Error creating news: {str(e)}', 'error')
    
    return render_template('admin/news_form.html', news=None)

@app.route('/admin/news/<int:news_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_news_edit(news_id):
    """Edit news article"""
    news = News.query.get_or_404(news_id)
    
    if request.method == 'POST':
        try:
            news.title = request.form.get('title')
            news.content = request.form.get('content')
            news.is_published = request.form.get('is_published') == 'on'
            news.updated_at = datetime.utcnow()
            db.session.commit()
            flash(f'News "{news.title}" updated successfully!', 'success')
            return redirect(url_for('admin_news_list'))
        except Exception as e:
            flash(f'Error updating news: {str(e)}', 'error')
    
    return render_template('admin/news_form.html', news=news)

@app.route('/admin/news/<int:news_id>/delete', methods=['POST'])
@login_required
def admin_news_delete(news_id):
    """Delete news article"""
    news = News.query.get_or_404(news_id)
    try:
        db.session.delete(news)
        db.session.commit()
        flash(f'News "{news.title}" deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting news: {str(e)}', 'error')
    
    return redirect(url_for('admin_news_list'))

# ==================== ADMIN - INDUSTRIES MANAGEMENT ====================

@app.route('/admin/industries')
@login_required
def admin_industries_list():
    """List all industries"""
    industries_list = Industry.query.all()
    return render_template('admin/industries_list.html', industries=industries_list)

@app.route('/admin/industries/new', methods=['GET', 'POST'])
@login_required
def admin_industry_create():
    """Create new industry"""
    if request.method == 'POST':
        try:
            industry = Industry(
                name=request.form.get('name'),
                description=request.form.get('description'),
                icon=request.form.get('icon', 'briefcase'),
                is_active=request.form.get('is_active') == 'on'
            )
            db.session.add(industry)
            db.session.commit()
            flash(f'Industry "{industry.name}" created successfully!', 'success')
            return redirect(url_for('admin_industries_list'))
        except Exception as e:
            flash(f'Error creating industry: {str(e)}', 'error')
    
    return render_template('admin/industry_form.html', industry=None)

@app.route('/admin/industries/<int:industry_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_industry_edit(industry_id):
    """Edit industry"""
    industry = Industry.query.get_or_404(industry_id)
    
    if request.method == 'POST':
        try:
            industry.name = request.form.get('name')
            industry.description = request.form.get('description')
            industry.icon = request.form.get('icon', 'briefcase')
            industry.is_active = request.form.get('is_active') == 'on'
            industry.updated_at = datetime.utcnow()
            db.session.commit()
            flash(f'Industry "{industry.name}" updated successfully!', 'success')
            return redirect(url_for('admin_industries_list'))
        except Exception as e:
            flash(f'Error updating industry: {str(e)}', 'error')
    
    return render_template('admin/industry_form.html', industry=industry)

@app.route('/admin/industries/<int:industry_id>/delete', methods=['POST'])
@login_required
def admin_industry_delete(industry_id):
    """Delete industry"""
    industry = Industry.query.get_or_404(industry_id)
    try:
        db.session.delete(industry)
        db.session.commit()
        flash(f'Industry "{industry.name}" deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting industry: {str(e)}', 'error')
    
    return redirect(url_for('admin_industries_list'))

# ==================== ADMIN - SERVICES MANAGEMENT ====================

@app.route('/admin/services')
@login_required
def admin_services_list():
    """List all services"""
    services_list = Service.query.all()
    return render_template('admin/services_list.html', services=services_list)

@app.route('/admin/services/new', methods=['GET', 'POST'])
@login_required
def admin_service_create():
    """Create new service"""
    if request.method == 'POST':
        try:
            service = Service(
                title=request.form.get('title'),
                description=request.form.get('description'),
                icon=request.form.get('icon', 'star'),
                is_active=request.form.get('is_active') == 'on'
            )
            db.session.add(service)
            db.session.commit()
            flash(f'Service "{service.title}" created successfully!', 'success')
            return redirect(url_for('admin_services_list'))
        except Exception as e:
            flash(f'Error creating service: {str(e)}', 'error')
    
    return render_template('admin/service_form.html', service=None)

@app.route('/admin/services/<int:service_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_service_edit(service_id):
    """Edit service"""
    service = Service.query.get_or_404(service_id)
    
    if request.method == 'POST':
        try:
            service.title = request.form.get('title')
            service.description = request.form.get('description')
            service.icon = request.form.get('icon', 'star')
            service.is_active = request.form.get('is_active') == 'on'
            service.updated_at = datetime.utcnow()
            db.session.commit()
            flash(f'Service "{service.title}" updated successfully!', 'success')
            return redirect(url_for('admin_services_list'))
        except Exception as e:
            flash(f'Error updating service: {str(e)}', 'error')
    
    return render_template('admin/service_form.html', service=service)

@app.route('/admin/services/<int:service_id>/delete', methods=['POST'])
@login_required
def admin_service_delete(service_id):
    """Delete service"""
    service = Service.query.get_or_404(service_id)
    try:
        db.session.delete(service)
        db.session.commit()
        flash(f'Service "{service.title}" deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting service: {str(e)}', 'error')
    
    return redirect(url_for('admin_services_list'))

# ==================== ADMIN - JOBS MANAGEMENT ====================

@app.route('/admin/jobs')
@login_required
def admin_jobs_list():
    """List all jobs"""
    jobs_list = Job.query.all()
    return render_template('admin/jobs_list.html', jobs=jobs_list)

@app.route('/admin/jobs/new', methods=['GET', 'POST'])
@login_required
def admin_job_create():
    """Create new job"""
    if request.method == 'POST':
        try:
            job = Job(
                title=request.form.get('title'),
                department=request.form.get('department'),
                location=request.form.get('location'),
                job_type=request.form.get('job_type', 'Full-time'),
                description=request.form.get('description'),
                requirements=request.form.get('requirements'),
                salary_range=request.form.get('salary_range'),
                is_active=request.form.get('is_active') == 'on'
            )
            db.session.add(job)
            db.session.commit()
            flash(f'Job "{job.title}" created successfully!', 'success')
            return redirect(url_for('admin_jobs_list'))
        except Exception as e:
            flash(f'Error creating job: {str(e)}', 'error')
    
    return render_template('admin/job_form.html', job=None)

@app.route('/admin/jobs/<int:job_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_job_edit(job_id):
    """Edit job"""
    job = Job.query.get_or_404(job_id)
    
    if request.method == 'POST':
        try:
            job.title = request.form.get('title')
            job.department = request.form.get('department')
            job.location = request.form.get('location')
            job.job_type = request.form.get('job_type', 'Full-time')
            job.description = request.form.get('description')
            job.requirements = request.form.get('requirements')
            job.salary_range = request.form.get('salary_range')
            job.is_active = request.form.get('is_active') == 'on'
            job.updated_at = datetime.utcnow()
            db.session.commit()
            flash(f'Job "{job.title}" updated successfully!', 'success')
            return redirect(url_for('admin_jobs_list'))
        except Exception as e:
            flash(f'Error updating job: {str(e)}', 'error')
    
    return render_template('admin/job_form.html', job=job)

@app.route('/admin/jobs/<int:job_id>/delete', methods=['POST'])
@login_required
def admin_job_delete(job_id):
    """Delete job"""
    job = Job.query.get_or_404(job_id)
    try:
        db.session.delete(job)
        db.session.commit()
        flash(f'Job "{job.title}" deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting job: {str(e)}', 'error')
    
    return redirect(url_for('admin_jobs_list'))

# ==================== ADMIN - TEAM MANAGEMENT ====================

@app.route('/admin/team')
@login_required
def admin_team_list():
    """List all team members"""
    team_list = TeamMember.query.all()
    return render_template('admin/team_list.html', team=team_list)

@app.route('/admin/team/new', methods=['GET', 'POST'])
@login_required
def admin_team_create():
    """Create new team member"""
    if request.method == 'POST':
        try:
            member = TeamMember(
                name=request.form.get('name'),
                position=request.form.get('position'),
                bio=request.form.get('bio'),
                email=request.form.get('email'),
                phone=request.form.get('phone'),
                twitter=request.form.get('twitter'),
                linkedin=request.form.get('linkedin'),
                is_active=request.form.get('is_active') == 'on'
            )
            db.session.add(member)
            db.session.commit()
            flash(f'Team member "{member.name}" created successfully!', 'success')
            return redirect(url_for('admin_team_list'))
        except Exception as e:
            flash(f'Error creating team member: {str(e)}', 'error')
    
    return render_template('admin/team_form.html', member=None)

@app.route('/admin/team/<int:member_id>/edit', methods=['GET', 'POST'])
@login_required
def admin_team_edit(member_id):
    """Edit team member"""
    member = TeamMember.query.get_or_404(member_id)
    
    if request.method == 'POST':
        try:
            member.name = request.form.get('name')
            member.position = request.form.get('position')
            member.bio = request.form.get('bio')
            member.email = request.form.get('email')
            member.phone = request.form.get('phone')
            member.twitter = request.form.get('twitter')
            member.linkedin = request.form.get('linkedin')
            member.is_active = request.form.get('is_active') == 'on'
            member.updated_at = datetime.utcnow()
            db.session.commit()
            flash(f'Team member "{member.name}" updated successfully!', 'success')
            return redirect(url_for('admin_team_list'))
        except Exception as e:
            flash(f'Error updating team member: {str(e)}', 'error')
    
    return render_template('admin/team_form.html', member=member)

@app.route('/admin/team/<int:member_id>/delete', methods=['POST'])
@login_required
def admin_team_delete(member_id):
    """Delete team member"""
    member = TeamMember.query.get_or_404(member_id)
    try:
        db.session.delete(member)
        db.session.commit()
        flash(f'Team member "{member.name}" deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting team member: {str(e)}', 'error')
    
    return redirect(url_for('admin_team_list'))

# ==================== ADMIN - CONTACTS MANAGEMENT ====================

@app.route('/admin/contacts')
@login_required
def admin_contacts_list():
    """List all contact submissions"""
    page = request.args.get('page', 1, type=int)
    contacts = Contact.query.order_by(Contact.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('admin/contacts_list.html', contacts=contacts)

@app.route('/admin/contacts/<int:contact_id>')
@login_required
def admin_contact_detail(contact_id):
    """View contact details"""
    contact = Contact.query.get_or_404(contact_id)
    contact.is_read = True
    db.session.commit()
    return render_template('admin/contact_detail.html', contact=contact)

@app.route('/admin/contacts/<int:contact_id>/delete', methods=['POST'])
@login_required
def admin_contact_delete(contact_id):
    """Delete contact"""
    contact = Contact.query.get_or_404(contact_id)
    try:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting contact: {str(e)}', 'error')
    
    return redirect(url_for('admin_contacts_list'))

# ==================== ADMIN - SETTINGS ====================

@app.route('/admin/settings', methods=['GET', 'POST'])
@login_required
def admin_settings():
    """Website settings management"""
    settings = WebsiteSettings.query.first()
    
    if request.method == 'POST':
        try:
            settings.site_title = request.form.get('site_title')
            settings.site_description = request.form.get('site_description')
            settings.company_phone = request.form.get('company_phone')
            settings.company_email = request.form.get('company_email')
            settings.company_address = request.form.get('company_address')
            settings.company_years = int(request.form.get('company_years', 30))
            settings.company_employees = int(request.form.get('company_employees', 500000))
            settings.company_countries = int(request.form.get('company_countries', 50))
            settings.facebook_url = request.form.get('facebook_url')
            settings.twitter_url = request.form.get('twitter_url')
            settings.linkedin_url = request.form.get('linkedin_url')
            settings.instagram_url = request.form.get('instagram_url')
            settings.updated_at = datetime.utcnow()
            
            db.session.commit()
            flash('Settings updated successfully!', 'success')
        except Exception as e:
            flash(f'Error updating settings: {str(e)}', 'error')
    
    return render_template('admin/settings.html', settings=settings)

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """500 error handler"""
    return render_template('500.html'), 500

# ==================== MAIN ====================

if __name__ == '__main__':
    init_database()
    app.run(debug=True, host='localhost', port=5000)
