# 🚀 Kalpeon Admin Dashboard - Quick Start Guide

## Start Using Your Admin Dashboard in 3 Steps

### Step 1: Start the Server
```bash
cd kalpeon-website
python app.py
```

You should see:
```
✓ Default admin created (username: admin, password: admin123)
✓ Website settings created
✓ Sample industries created
✓ Sample services created
✓ Sample news created
 * Running on http://localhost:5000
```

### Step 2: Open Your Browser
- **Website:** http://localhost:5000
- **Admin Login:** http://localhost:5000/admin/login

### Step 3: Login with Default Credentials
- **Username:** `admin`
- **Password:** `admin123`

---

## 📊 Admin Dashboard Menu

Once logged in, you'll see the admin dashboard with access to:

| Menu Item | Function | URL |
|-----------|----------|-----|
| 📊 Dashboard | View statistics & recent activity | `/admin/dashboard` |
| 📰 News | Manage blog posts & news articles | `/admin/news` |
| 🏭 Industries | Manage industry sectors | `/admin/industries` |
| ⚙️ Services | Manage service offerings | `/admin/services` |
| 💼 Jobs | Post & manage job openings | `/admin/jobs` |
| 👥 Team | Manage team member profiles | `/admin/team` |
| 📧 Contacts | View contact form submissions | `/admin/contacts` |
| ⚙️ Settings | Configure website settings | `/admin/settings` |

---

## 🎯 Common Tasks

### Adding News
1. Go to **News** in admin menu
2. Click **+ Create Article**
3. Fill in title, content, author, image URL
4. Check "Publish" to make it live
5. Click **Create Article**

### Adding a Job
1. Go to **Jobs** in admin menu
2. Click **+ Post Job**
3. Enter job title, department, location, job type
4. Add description and requirements
5. Check "Active" to accept applications
6. Click **Post Job**

### Adding Team Member
1. Go to **Team** in admin menu
2. Click **+ Add Team Member**
3. Enter name, position, department, email
4. Add bio, photo URL, social media links
5. Click **Add Member**

### Configuring Website Settings
1. Go to **Settings** in admin menu
2. Update site title, description, logo
3. Add contact information
4. Add social media links
5. Update company statistics
6. Click **Save Settings**

### Viewing Contact Messages
1. Go to **Contacts** in admin menu
2. See all messages from your contact form
3. Click **View** to read full message
4. Click **Mark as Read** to track responses

---

## 💡 Tips

✅ All forms auto-save to the database  
✅ Changes appear immediately on the website  
✅ You can edit or delete any content  
✅ All timestamps are tracked automatically  
✅ Pagination is built in for long lists  

---

## 🔒 Security Notes

⚠️ **Change Your Password!**
- Default password `admin123` is just for initial setup
- In production, change to a strong password
- Don't share your admin credentials

---

## 🐛 Troubleshooting

**Port Already in Use?**
```bash
python app.py
# Change port in app.py if needed
# app.run(debug=True, host='localhost', port=5001)
```

**Database Issues?**
- Delete `instance/kalpeon.db` file
- Restart the server (it will recreate the database)

**Not seeing changes?**
- Clear browser cache (Ctrl+F5)
- Make sure you clicked Save/Submit button

---

## 📱 Mobile Friendly

The admin dashboard is fully responsive and works great on:
- Desktop computers
- Tablets
- Mobile phones

---

## ✨ Your Website Features

**Public Pages:**
- Home
- About
- Industries
- Services
- News & Blog
- Careers (Jobs)
- Gallery
- Contact Form

**Admin Features:**
- Full content management
- Multi-page administration
- User authentication
- Database storage
- Automatic backups

---

**Need Help?** Refer to `ADMIN_SETUP.md` for detailed documentation.

**Happy Managing! 🎉**
