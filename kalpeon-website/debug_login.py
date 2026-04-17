#!/usr/bin/env python
"""Debug login issues"""

from app import app, db
from models import Admin

with app.app_context():
    print("=== Database Debug ===\n")
    
    # Check database file
    import os
    db_path = 'instance/kalpeon.db'
    print(f"Database path: {db_path}")
    print(f"Database exists: {os.path.exists(db_path)}")
    print(f"Database size: {os.path.getsize(db_path) if os.path.exists(db_path) else 'N/A'} bytes\n")
    
    # Check admin user
    print("=== Admin Users in Database ===\n")
    admins = Admin.query.all()
    print(f"Total admins: {len(admins)}")
    
    for admin in admins:
        print(f"\nUsername: {admin.username}")
        print(f"Email: {admin.email}")
        print(f"ID: {admin.id}")
        print(f"Is Active: {admin.is_active}")
        print(f"Has password hash: {bool(admin.password_hash)}")
        
        # Test password
        test_pwd = admin.check_password('admin123')
        print(f"Password 'admin123' matches: {test_pwd}")
    
    # Test query
    print("\n=== Query Test ===\n")
    admin = Admin.query.filter_by(username='admin').first()
    print(f"Found admin by username: {admin is not None}")
    if admin:
        print(f"Admin object: {admin}")
        print(f"Can create session: {bool(admin.get_id())}")

print("\n✅ Debug complete!")
