# 🗺️ Kalpeon Website - Complete API Routes Reference

## 🌐 Public Website Routes

### Page Routes
| Method | Route | Description | Template |
|--------|-------|-------------|----------|
| GET | `/` | Home page | `index.html` |
| GET | `/about` | About page | `about.html` |
| GET | `/industries` | Industries listing | `industries.html` |
| GET | `/services` | Services listing | `services.html` |
| GET | `/news` | News listing | `news.html` |
| GET | `/news/<int:news_id>` | Individual news article | `news_detail.html` |
| GET | `/contact` | Contact form page | `contact.html` |
| POST | `/contact` | Submit contact form | Redirects with message |
| GET | `/careers` | Jobs/careers listing | `careers.html` |
| GET | `/gallery` | Photo gallery | `gallery.html` |
| GET | `/sitemap` | XML sitemap | `sitemap.xml` |

### API Routes
| Method | Route | Description | Returns |
|--------|-------|-------------|---------|
| POST | `/api/newsletter` | Newsletter signup | JSON response |

### Error Routes
| Status | Route | Description |
|--------|-------|-------------|
| 404 | `<any invalid path>` | Page not found | `404.html` |
| 500 | `<server error>` | Server error | `500.html` |

---

## 🔐 Admin Authentication Routes

| Method | Route | Description | Template | Protected |
|--------|-------|-------------|----------|-----------|
| GET | `/admin/login` | Admin login page | `admin/login.html` | ❌ |
| POST | `/admin/login` | Process login form | Redirects to dashboard | ❌ |
| GET | `/admin/logout` | Logout & clear session | Redirects to home | ✅ |

---

## 📊 Admin Dashboard Routes

| Method | Route | Description | Template | Protected |
|--------|-------|-------------|----------|-----------|
| GET | `/admin/dashboard` | Main admin dashboard | `admin/dashboard.html` | ✅ |

---

## 📰 News Management Routes

| Method | Route | Description | Template | Protected |
|--------|-------|-------------|----------|-----------|
| GET | `/admin/news` | List all news articles | `admin/news_list.html` | ✅ |
| GET | `/admin/news/new` | Create news form | `admin/news_form.html` | ✅ |
| POST | `/admin/news/new` | Create news (process) | Redirects to list | ✅ |
| GET | `/admin/news/<int:news_id>/edit` | Edit news form | `admin/news_form.html` | ✅ |
| POST | `/admin/news/<int:news_id>/edit` | Update news (process) | Redirects to list | ✅ |
| POST | `/admin/news/<int:news_id>/delete` | Delete news | Redirects to list | ✅ |

**Form Fields:**
- title (required)
- content (required)
- author
- image_url
- category
- is_published (checkbox)

---

## 🏭 Industries Management Routes

| Method | Route | Description | Template | Protected |
|--------|-------|-------------|----------|-----------|
| GET | `/admin/industries` | List all industries | `admin/industries_list.html` | ✅ |
| GET | `/admin/industries/new` | Create industry form | `admin/industry_form.html` | ✅ |
| POST | `/admin/industries/new` | Create industry (process) | Redirects to list | ✅ |
| GET | `/admin/industries/<int:industry_id>/edit` | Edit industry form | `admin/industry_form.html` | ✅ |
| POST | `/admin/industries/<int:industry_id>/edit` | Update industry (process) | Redirects to list | ✅ |
| POST | `/admin/industries/<int:industry_id>/delete` | Delete industry | Redirects to list | ✅ |

**Form Fields:**
- name (required)
- description (required)
- icon
- image_url
- is_active (checkbox)

---

## ⚙️ Services Management Routes

| Method | Route | Description | Template | Protected |
|--------|-------|-------------|----------|-----------|
| GET | `/admin/services` | List all services | `admin/services_list.html` | ✅ |
| GET | `/admin/services/new` | Create service form | `admin/service_form.html` | ✅ |
| POST | `/admin/services/new` | Create service (process) | Redirects to list | ✅ |
| GET | `/admin/services/<int:service_id>/edit` | Edit service form | `admin/service_form.html` | ✅ |
| POST | `/admin/services/<int:service_id>/edit` | Update service (process) | Redirects to list | ✅ |
| POST | `/admin/services/<int:service_id>/delete` | Delete service | Redirects to list | ✅ |

**Form Fields:**
- title (required)
- description (required)
- icon
- image_url
- is_active (checkbox)

---

## 💼 Jobs Management Routes

| Method | Route | Description | Template | Protected |
|--------|-------|-------------|----------|-----------|
| GET | `/admin/jobs` | List all jobs | `admin/jobs_list.html` | ✅ |
| GET | `/admin/jobs/new` | Create job form | `admin/job_form.html` | ✅ |
| POST | `/admin/jobs/new` | Create job (process) | Redirects to list | ✅ |
| GET | `/admin/jobs/<int:job_id>/edit` | Edit job form | `admin/job_form.html` | ✅ |
| POST | `/admin/jobs/<int:job_id>/edit` | Update job (process) | Redirects to list | ✅ |
| POST | `/admin/jobs/<int:job_id>/delete` | Delete job | Redirects to list | ✅ |

**Form Fields:**
- title (required)
- department (required)
- location (required)
- job_type (select: Full-Time, Part-Time, Contract, Temporary) (required)
- description (required)
- requirements (required)
- salary_range
- is_active (checkbox)

---

## 👥 Team Management Routes

| Method | Route | Description | Template | Protected |
|--------|-------|-------------|----------|-----------|
| GET | `/admin/team` | List all team members | `admin/team_list.html` | ✅ |
| GET | `/admin/team/new` | Add team member form | `admin/team_form.html` | ✅ |
| POST | `/admin/team/new` | Add team member (process) | Redirects to list | ✅ |
| GET | `/admin/team/<int:team_id>/edit` | Edit team member form | `admin/team_form.html` | ✅ |
| POST | `/admin/team/<int:team_id>/edit` | Update team member (process) | Redirects to list | ✅ |
| POST | `/admin/team/<int:team_id>/delete` | Delete team member | Redirects to list | ✅ |

**Form Fields:**
- name (required)
- position (required)
- department (required)
- email (required)
- phone
- bio
- photo_url
- linkedin
- twitter

---

## 📧 Contact Management Routes

| Method | Route | Description | Template | Protected |
|--------|-------|-------------|----------|-----------|
| GET | `/admin/contacts` | List contact submissions | `admin/contacts_list.html` | ✅ |
| GET | `/admin/contacts/<int:contact_id>` | View contact details | `admin/contact_detail.html` | ✅ |
| POST | `/admin/contacts/<int:contact_id>/mark_read` | Mark contact as read | Redirects | ✅ |
| POST | `/admin/contacts/<int:contact_id>/delete` | Delete contact | Redirects to list | ✅ |

---

## ⚙️ Settings Management Routes

| Method | Route | Description | Template | Protected |
|--------|-------|-------------|----------|-----------|
| GET | `/admin/settings` | View settings form | `admin/settings.html` | ✅ |
| POST | `/admin/settings` | Update settings | Redirects to settings | ✅ |

**Form Fields:**
- site_title (required)
- site_description (required)
- logo_url
- favicon_url
- contact_email (required)
- contact_phone (required)
- address (required)
- facebook_url
- twitter_url
- linkedin_url
- instagram_url
- years_established
- employees_count
- projects_completed
- clients_served

---

## 📊 Route Summary Statistics

- **Total Routes:** 50+
- **Public Routes:** 10
- **Admin Routes:** 40+
- **Protected Routes:** 40+ (require login)
- **Admin Management Pages:** 15
- **CRUD Operations:** Full support for all content types

---

## 🔑 HTTP Methods Used

| Method | Usage | Frequency |
|--------|-------|-----------|
| GET | Retrieve pages and data | Most common |
| POST | Submit forms and delete records | Common |
| PUT | (Not used - could be added) | - |
| DELETE | (Not used - POST /delete used instead) | - |

---

## 🔒 Authentication

**Protected Routes:** All `/admin/*` routes except `/admin/login`

**Authentication Method:** Flask-Login with session cookies

**Default Credentials:**
- Username: `admin`
- Password: `admin123`

---

## 🎯 Common URL Patterns

### Create Flow
1. GET `/admin/<resource>` → View list
2. GET `/admin/<resource>/new` → Show create form
3. POST `/admin/<resource>/new` → Process and save
4. Redirects to GET `/admin/<resource>` → Show updated list

### Edit Flow
1. GET `/admin/<resource>` → View list
2. GET `/admin/<resource>/<id>/edit` → Show edit form
3. POST `/admin/<resource>/<id>/edit` → Process and save
4. Redirects to GET `/admin/<resource>` → Show updated list

### Delete Flow
1. POST `/admin/<resource>/<id>/delete` → Delete record
2. Redirects to GET `/admin/<resource>` → Show updated list

---

## 📝 Query Parameters

### Pagination
- `/admin/news?page=2` - View page 2 of news articles
- `/admin/contacts?page=3` - View page 3 of contacts

### Future Extensions
- `/api/news?limit=10&offset=0` - API pagination
- `/search?q=keyword` - Search functionality

---

## 🚀 Testing Routes

### Test Login
```
Navigate to: http://localhost:5000/admin/login
Username: admin
Password: admin123
```

### Test Protected Route
```
Try accessing: http://localhost:5000/admin/dashboard
Without login: Redirects to /admin/login
With login: Shows dashboard
```

### Test Content Management
```
1. Go to: http://localhost:5000/admin/news
2. Click: + Create Article
3. Fill form and click: Create Article
4. New article appears in list and on public site
```

---

## 📋 Code Reference

### Route Naming Convention
- `admin_<resource>_list` - List all records
- `admin_<resource>_create` - Create new record
- `admin_<resource>_edit` - Edit existing record
- `admin_<resource>_delete` - Delete record

### Template Naming Convention
- `admin/<resource>_list.html` - List view
- `admin/<resource>_form.html` - Create/edit form
- `admin/contact_detail.html` - Detail view

---

## ✅ All Routes Status

✅ **Implemented:** 50+ routes  
✅ **Tested:** All working correctly  
✅ **Documented:** Complete documentation provided  
✅ **Protected:** Admin routes secured with login  
✅ **Error Handling:** 404 and 500 pages available  

---

**Last Updated:** 2024  
**Framework:** Flask 2.3.3  
**Status:** ✅ Production Ready
