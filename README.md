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
<img width="2160" height="1440" alt="image" src="https://github.com/user-attachments/assets/bb47a943-2963-4cb9-85e4-76f293f33053" />


---

### Blog Page
<img width="2160" height="1440" alt="image" src="https://github.com/user-attachments/assets/a8faf5dd-6dec-4a57-9f07-d3ca8bbe792b" />


---

### Categories Page (Selected)
<img width="2160" height="1440" alt="image" src="https://github.com/user-attachments/assets/0099df46-2132-4413-af14-4e2a62b6b285" />



---
---

## 🎓 Credits & Acknowledgments

This project was developed as part of the **Premium Django Project Course** by **Tech With Rathan**. 

**Resources used:**
* 📺 **Tutorial:** [Build a Complete Blogging System](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
* 🌐 **Instructor Website:** [Tech With Rathan](https://techwithrathan.com/)
* 💬 **Community:** Part of the Tech With Rathan Discord community.

---
