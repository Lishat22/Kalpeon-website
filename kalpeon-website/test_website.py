#!/usr/bin/env python
"""
Test website to ensure pages load and database works
"""
import os
import sys
from app import app, db, Admin

def test_pages():
    """Test that all pages can be accessed"""
    print("=== Testing Website Pages ===\n")
    
    with app.test_client() as client:
        # Test public pages
        public_pages = [
            ('/', 'Home'),
            ('/about', 'About'),
            ('/industries', 'Industries'),
            ('/services', 'Services'),
            ('/news', 'News'),
            ('/careers', 'Careers'),
            ('/gallery', 'Gallery'),
            ('/contact', 'Contact'),
        ]
        
        print("Testing public pages:")
        for route, name in public_pages:
            response = client.get(route)
            status = "✓" if response.status_code == 200 else "✗"
            print(f"  {status} {name:15} ({route:20}) - Status: {response.status_code}")
        
        print("\nTesting admin login page:")
        response = client.get('/admin/login')
        status = "✓" if response.status_code == 200 else "✗"
        print(f"  {status} Admin Login - Status: {response.status_code}")
        
        print("\nTesting protected dashboard (should redirect to login):")
        response = client.get('/admin/dashboard', follow_redirects=False)
        status = "✓" if response.status_code == 302 else "✗"
        print(f"  {status} Admin Dashboard - Status: {response.status_code} (302 = correct)")

def test_database():
    """Test database connectivity"""
    print("\n=== Testing Database ===\n")
    
    try:
        # Count records
        with app.app_context():
            from models import News, Industry, Service
            
            news_count = News.query.count()
            industry_count = Industry.query.count()
            service_count = Service.query.count()
            admin_count = Admin.query.count()
            
            print(f"✓ Database connection works!")
            print(f"  - News articles: {news_count}")
            print(f"  - Industries: {industry_count}")
            print(f"  - Services: {service_count}")
            print(f"  - Admin users: {admin_count}")
            
            return True
    except Exception as e:
        print(f"✗ Database error: {e}")
        return False

def test_static_files():
    """Test that static files exist"""
    print("\n=== Testing Static Files ===\n")
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    static_files = [
        'static/css/style.css',
        'static/css/admin-style.css',
        'static/js/main.js',
    ]
    
    for file_path in static_files:
        full_path = os.path.join(base_path, file_path)
        exists = os.path.exists(full_path)
        size = os.path.getsize(full_path) if exists else 0
        status = "✓" if exists else "✗"
        print(f"  {status} {file_path:30} - {size:,} bytes")

if __name__ == '__main__':
    print("\n" + "="*60)
    print("KALPEON WEBSITE TEST SUITE")
    print("="*60 + "\n")
    
    test_pages()
    test_database()
    test_static_files()
    
    print("\n" + "="*60)
    print("✅ Test complete!")
    print("="*60 + "\n")
