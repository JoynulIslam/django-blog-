# 📰 Django Advanced Blogging Platform

A full-featured, production-style blogging platform built with Django.  
This project demonstrates a real-world blog system with role-based access control, content workflows, and clean UI using Bootstrap.

---

## 🚀 Features

### 👥 Multiple User Roles

- **Admin** – Full system control
- **Manager** – Manage users & content
- **Editor** – Review and publish posts
- **Author** – Create and manage own posts

### 📝 Blog Management

- Create, edit, delete blog posts
- Draft & publish workflow
- Rich text editor integration
- Featured image support

### 📂 Category & Tag System

- Create & manage categories
- Filter posts by category
- Tag-based organization

### 💬 Comments System

- Users can comment on blog posts
- Display comments with timestamp
- Authenticated user-based commenting

### 🔐 Authentication & Authorization

- User registration & login
- Role-based permissions
- Access control for dashboard

### 🎨 Frontend

- Bootstrap-based responsive UI
- Clean and modern template design
- Custom 404 & forbidden pages

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML5, CSS3, Bootstrap
- **Database:** SQLite (default)
- **Authentication:** Django built-in auth system

---

## 📁 Project Structure

```
BLOG/
│
├── blog_main/          # Main project settings
├── blogs/              # Blog application
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── context_processors.py
│
├── dashboards/         # Dashboard management app
├── templates/
│   ├── dashboard/
│   ├── base.html
│   ├── blog.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── post_by_category.html
│   ├── search.html
│   ├── 404_template.html
│   └── forbidden_or_notfound.html
│
├── static/             # CSS, JS, Images
├── media/              # Uploaded files
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository

```bash
git clone https://github.com/JoynulIslam/django-blog-.git
cd django-blog-
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

Activate environment:

**Windows**

```bash
env\Scripts\activate
```

**Mac/Linux**

```bash
source env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔑 Role-Based Workflow

| Role    | Permissions             |
| ------- | ----------------------- |
| Admin   | Full control            |
| Manager | Manage content & users  |
| Editor  | Review & publish posts  |
| Author  | Create & edit own posts |

## 👨‍💻 Author

Your Name  
GitHub: https://github.com/JoynulIslam

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

⭐ If you like this project, don't forget to give it a star!
