# Kalpeon Group of Industry - Website

A professional, fully functional website for Kalpeon Group - a multinational conglomerate with operations across multiple industries.

## Overview

This is a complete Flask-based web application with both frontend and backend, featuring:
- **Multiple Pages**: Home, About, Industries, Services, News, Careers, Gallery, Contact
- **Working Forms**: Contact form with validation and storage
- **Responsive Design**: Mobile-friendly interface
- **Dynamic Content**: News articles, job listings, team members
- **Interactive Features**: Newsletter subscription, FAQ toggle, gallery filtering

## Features

### Pages & Functionality

1. **Home Page** - Hero section, features, industries preview, latest news
2. **About Page** - Company info, mission/vision, team, milestones, awards
3. **Industries Page** - 6 major industry sectors with detailed information
4. **Services Page** - Service offerings with process workflow
5. **News Page** - News articles with individual article pages
6. **Careers Page** - Job listings with application modal
7. **Gallery Page** - Image gallery with filtering capabilities
8. **Contact Page** - Contact form with validation, FAQ section, contact information
9. **Error Pages** - 404 and 500 error pages

### Technical Features

- **Flask Backend**: Robust Python backend with multiple routes
- **Form Handling**: Contact form validation and storage in JSON
- **Data Persistence**: JSON file storage for contacts and news
- **Responsive Design**: Mobile-optimized CSS
- **Interactive JavaScript**: Smooth interactions, form handling, animations
- **SEO Friendly**: Proper meta tags and structure

## Installation

### Requirements

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Navigate to the project directory:
```bash
cd kalpeon-website
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

The website will be running on your local machine. All pages, forms, and interactive features will work properly.

## Project Structure

```
kalpeon-website/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── templates/                      # HTML templates
│   ├── base.html                   # Base template with navigation & footer
│   ├── index.html                  # Home page
│   ├── about.html                  # About page
│   ├── industries.html             # Industries page
│   ├── services.html               # Services page
│   ├── news.html                   # News listing page
│   ├── news_detail.html            # Individual news article
│   ├── contact.html                # Contact page with form
│   ├── careers.html                # Careers page with job listings
│   ├── gallery.html                # Gallery page
│   ├── sitemap.html                # Sitemap
│   ├── 404.html                    # 404 error page
│   └── 500.html                    # 500 error page
├── static/                         # Static files
│   ├── css/
│   │   └── style.css               # Main stylesheet
│   ├── js/
│   │   └── main.js                 # JavaScript functionality
│   └── images/                     # Image assets (placeholder)
├── contacts.json                   # Stored contact form submissions
└── news.json                       # News articles database
```

## Features Explained

### Contact Form
- Located on the Contact page
- Validates all required fields
- Stores submissions in `contacts.json`
- Shows success/error messages
- Works with AJAX for smooth submission

### News System
- Dynamic news articles stored in `news.json`
- Each article has a detail page
- News listing with filtering
- Related news section on article pages

### Job Listings
- Multiple job positions listed on Careers page
- Application modal for easy submission
- Job categories and locations
- Benefits section showcasing company perks

### Gallery
- Image gallery with category filtering
- Lightbox view for full-size images
- Responsive grid layout
- Statistics section

### FAQ
- Expandable FAQ items
- Smooth toggle animations
- Contact information section
- Newsletter subscription

## Customization

### Colors
Edit CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #1e3c72;
    --secondary-color: #2a5298;
    --accent-color: #f39c12;
    ...
}
```

### Content
- Edit page content in template files (`.html` files)
- Modify news in `news.json`
- Update team members in `about.html`
- Change job listings in `careers.html`

### Database
To use a real database instead of JSON files, modify `app.py`:
1. Add SQLAlchemy or another ORM
2. Create database models
3. Update routes to use the database

## API Endpoints

- `GET /` - Home page
- `GET /about` - About page
- `GET /industries` - Industries page
- `GET /services` - Services page
- `GET /news` - News listing
- `GET /news/<id>` - Individual news article
- `GET /contact` - Contact page
- `POST /contact` - Submit contact form
- `GET /careers` - Careers page
- `GET /gallery` - Gallery page
- `POST /api/newsletter` - Newsletter subscription
- `GET /api/get-contacts` - Get all contacts (admin)

## Troubleshooting

### Port Already in Use
If port 5000 is in use, modify `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)  # Change port
```

### Flask Not Found
Make sure Flask is installed:
```bash
pip install Flask==2.3.3
```

### Template Not Found
Ensure all template files are in the `templates/` directory with correct names.

## Future Enhancements

- Database integration (PostgreSQL/MySQL)
- User authentication system
- Blog functionality with comments
- Email notifications for form submissions
- Admin dashboard
- Payment integration
- Multi-language support
- API documentation

## License

Proprietary - Kalpeon Group of Industry

## Support

For issues or questions, contact: info@kalpeon.com

---

**Version**: 1.0.0  
**Last Updated**: April 2026
