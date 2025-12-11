![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-darkgreen)
![DRF](https://img.shields.io/badge/DRF-3.16-red)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

Django Blog API

A fully functional RESTful Blog API built with Django, Django REST Framework, PostgreSQL, and JWT authentication.
This project demonstrates practical backend engineering skills such as user authentication, profile management, following system, article creation, tags, comments, likes, and personalized feeds.


---

Features

Authentication

Register new users

Login using JWT

Refresh access tokens


Users

Retrieve current logged-in user

Update authenticated user details


Profiles

View any user's profile

Follow or unfollow users

Check following status


Articles

Create, retrieve, update, and delete articles

Filter articles by tags

Filter articles by authors

Sort articles by creation date or number of likes

Mark and unmark articles as favorite

Personalized feed showing articles from followed users


Comments

Add comments to articles

View all comments for a specific article

Delete own comments



---

Tech Stack

Python 3

Django

Django REST Framework

PostgreSQL

JWT (djangorestframework-simplejwt)

drf-spectacular for API documentation



---

API Endpoints Overview

Authentication

Method	Endpoint	Description

POST	/api/users/	Register a new user
POST	/api/login/	Login and receive JWT tokens
POST	/api/token/refresh/	Refresh access token


Users

Method	Endpoint	Description

GET	/api/user/	Retrieve current authenticated user
PUT/PATCH	/api/user/	Update authenticated user


Profiles

Method	Endpoint	Description

GET	/api/profiles/{username}/	Retrieve a public profile
POST	/api/profiles/{username}/follow/	Follow a user
DELETE	/api/profiles/{username}/follow/	Unfollow a user


Articles

Method	Endpoint	Description

GET	/api/articles/	List all articles with filters
POST	/api/articles/	Create new article
GET	/api/articles/{slug}/	Retrieve single article
PUT/PATCH	/api/articles/{slug}/	Update article
DELETE	/api/articles/{slug}/	Delete article
GET	/api/articles/feed/	Personalized feed


Comments

Method	Endpoint	Description

GET	/api/articles/{slug}/comments/	List comments for article
POST	/api/articles/{slug}/comments/	Add new comment
DELETE	/api/comments/{id}/	Delete comment
