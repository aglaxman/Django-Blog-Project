# 🚀 Django  Blog Project

A comprehensive, production-ready blogging platform built with **Django**. This project features a dual-interface system: a dynamic public-facing blog for readers and a secure, role-based management dashboard for editors and managers.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python / Django |
| **Database** | SQLite (Dev)  |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Auth** | Django Auth System (Groups & Permissions) |
| **Utilities** | Pillow (Image Handling), Git |

---

## 🌟 Key Features

### 📖 Public Blog Interface
* **Dynamic Content:** Home page featuring **Featured Posts**, **Recent Articles**, and category-based filtering.
* **Advanced Search:** Full-text search functionality across all blog titles and content.
* **Commenting System:** Interactive comment section restricted to authenticated users.
* **SEO Optimized:** Automated **Slug Generation** for clean, human-readable URLs.
* **Custom Error Handling:** Personalized **404 error pages** for a seamless user experience.

### 🔐 Multi-User Dashboard (CMS)
* **Role-Based Access Control (RBAC):**
    * **Managers:** Full control over users, permissions, and site content.
    * **Editors:** Specialized access to manage categories and write/edit their own posts.
* **Content CRUD:** Full Create, Read, Update, and Delete capabilities for Blogs and Categories.
* **User Management:** Administrative interface to add, edit, or remove staff members.
* **Analytics:** Live dashboard statistics showing total post counts and category distributions.

---

## ⚙️ Technical Implementations

* **Context Processors:** Global data availability (e.g., categories appearing in every navbar).
* **Template Inheritance:** **DRY (Don't Repeat Yourself)** architecture using base templates and partials.
* **Media Handling:** Secure configuration for uploading and displaying blog thumbnails.
* **Security:** Protection of dashboard routes using `@login_required` decorators and custom permission checks.

---

## 📂 Project Workflow

The project was developed in professional stages:
1.  **Environment Setup:** Project initialization and Superuser creation.
2.  **Database Modeling:** Designing `Category`, `Blog`, `Comment`, and `SocialLink` models.
3.  **Frontend Logic:** Implementing Template Inheritance and Static/Media configurations.
4.  **Security:** Building custom Registration, Login, and Logout flows.
5.  **Admin Logic:** Developing Manager/Editor dashboards with unique permissions.

---




## 🖼️ Project Showcase

###  Public Homepage
<img width="2160" height="1440" alt="image" src="https://github.com/user-attachments/assets/e676e12f-549d-4b93-9057-a988c9d17576" />

---

### Blog Page
<img width="2160" height="1440" alt="image" src="https://github.com/user-attachments/assets/6da4f9db-a67e-446b-b195-1b4fa2173274" />

---

### Categories Page (Selected)
<img width="2160" height="1440" alt="image" src="https://github.com/user-attachments/assets/f5ed11c0-1195-447c-a91a-3a1f4d935127" />

---
---

## 🎓 Credits & Acknowledgments

This project was developed as part of the **Premium Django Project Course** by **Tech With Rathan**. 

I would like to express my gratitude to **Rathan Kumar** for providing this high-quality, industry-standard curriculum for free. Through this project, I successfully implemented:
* **Advanced Django Logic:** Mastering multi-user roles and complex permissions.
* **Professional Workflow:** Building a feature-rich CMS from scratch rather than a basic blog.
* **Production Standards:** Learning the importance of clean project structure and deployment readiness.

**Resources used:**
* 📺 **Tutorial:** [Build a Complete Blogging System](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
* 🌐 **Instructor Website:** [Tech With Rathan](https://techwithrathan.com/)
* 💬 **Community:** Part of the Tech With Rathan Discord community.

---
