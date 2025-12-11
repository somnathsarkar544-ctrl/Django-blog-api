![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-darkgreen)
![DRF](https://img.shields.io/badge/DRF-3.16-red)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

# 📝 Django Blog API  
A fully-featured *RESTful Blog API* built using *Django + Django REST Framework + JWT Authentication + PostgreSQL*.  
Supports articles, comments, likes, profiles, following system, and personalized feeds.

---

## ⭐ Project Highlights

- 🔐 JWT Authentication (Login + Refresh)
- 📝 CRUD operations for Articles
- 🔖 Tags System
- 💬 Comments System
- ❤ Like / Unlike Articles
- 👤 User Profile View & Edit
- ➕ Follow / Unfollow Users
- 📰 Personalized Feed (articles from followed users)
- 🐘 PostgreSQL Database
- 📬 Fully testable using Postman Collection

---

## 🛠 Tech Stack

| Layer           | Technology                 |
|----------------|-----------------------------|
| Backend        | Django, Django REST Framework |
| Auth           | JWT (SimpleJWT)            |
| Database       | PostgreSQL                 |
| Documentation  | DRF Spectacular (OpenAPI/Swagger) |
| Testing        | Postman Collection          |

---

## 📂 Project Structure
blog_api/ │── articles/ │   ├── models.py │   ├── views.py │   ├── serializers.py │   ├── urls.py │── comments/ │── users/ │── followers/ │── blog_api/ │── manage.py

---

## 🔥 Features in Detail

### 👤 Authentication
- Register new users
- Login using username & password
- Receive access + refresh tokens
- Get current logged-in user profile

---

### 📝 Articles
- Create, update, delete articles
- Add tags
- Like / Unlike articles
- Filter by tag or author
- Public article list
- Detail view by slug

---

### 💬 Comments
- Add comments to articles  
- Delete your own comments  

---

### 👥 Profiles
- View any user's profile
- Follow / Unfollow users
- You *cannot follow yourself* (validated)

---

### 📰 Feed
- Get articles ONLY from users you follow (personalized feed)

---

## 📡 API Endpoints Overview

### 🔐 *Auth*
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /api/users/ | Register new user |
| POST | /api/login/ | Login (get JWT) |
| POST | /api/token/refresh/ | Refresh token |

---

### 👤 *User*
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | /api/user/ | Get current logged-in user |
| PUT/PATCH | /api/user/ | Update logged-in user |

---

### 📄 *Articles*
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | /api/articles/ | List all articles |
| POST | /api/articles/ | Create article |
| GET | /api/articles/{slug}/ | Article details |
| PUT/PATCH | /api/articles/{slug}/ | Update |
| DELETE | /api/articles/{slug}/ | Delete |
| GET | /api/articles/feed/ | Personalized feed |

---

### 💬 *Comments*
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | /api/articles/{slug}/comments/ | Add comment |
| DELETE | /api/comments/{id}/ | Delete comment |

---

### 👥 *Profiles*
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | /api/profiles/{username}/ | View profile |
| POST | /api/profiles/{username}/follow/ | Follow user |
| DELETE | /api/profiles/{username}/follow/ | Unfollow user |

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/Django-blog-api.git
cd Django-blog-api
```
### 2️⃣ Create & activate a virtual enviroment 
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Setup PostgresSQL database
create a database blogdb,update .env or settings.

### 5️⃣ Run migrations
```bash
python manage.py migrate
```
### 6️⃣ Start the server
```bash
python manage.py runsserver
```

🤝 Contributing

Pull requests are welcome!
Please follow clean commit messages and create feature-based branches.





