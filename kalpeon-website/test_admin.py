#!/usr/bin/env python
"""Test admin login credentials"""

from app import app, db
from models import Admin

with app.app_context():
    admin = Admin.query.filter_by(username='admin').first()
    
    if admin:
        print(f'✓ Admin found: {admin.username}')
        print(f'✓ Email: {admin.email}')
        print(f'✓ Password hash exists: {bool(admin.password_hash)}')
        
        # Test password
        test_pwd = admin.check_password('admin123')
        print(f'✓ Password "admin123" correct: {test_pwd}')
        
        if test_pwd:
            print('\n✅ Login should work!')
        else:
            print('\n❌ Password check failed!')
    else:
        print('❌ Admin user not found in database!')
        print('Available users:', Admin.query.all())
