# Doctor & Patient Management System

A full-stack web application built with Django (Python) and MySQL, designed to manage hospital operations efficiently. It features separate dashboards for Doctors and Patients, appointment booking, medical report management, and daily health tracking.

## 🚀 Features

### For Patients:
- **Registration & Profile**: Secure sign-up and login.
- **Book Appointments**: View available doctors and book slots.
- **Dashboard**: Track upcoming and past appointments.
- **Medical Reports**: View reports uploaded by doctors.
- **Use Prescriptions**: View digital prescriptions.
- **Daily Health Tracker**: Submit daily health updates (mood, symptoms, rating).

### For Doctors:
- **Registration**: Register with specialization and availability.
- **Dashboard**: View pending appointment requests and scheduled visits.
- **Patient Management**: Accept/Decline appointments.
- **Upload Reports**: Upload medical reports (PDF/Images) for patients.
- **Prescriptions**: (Planned) Create digital prescriptions.

### For Admins:
- **Django Admin Panel**: comprehensive database management.
- **User Verification**: Manage doctor and patient accounts.

---

## 🛠️ Tech Stack

- **Backend**: Django 6.0 (Python)
- **Database**: MySQL (Production-ready relational database)
- **Frontend**: HTML5, CSS3 (Custom Glassmorphism Design), JavaScript
- **Styling**: Modern, responsive UI with glassmorphism effects
- **Authentication**: Django's built-in Auth system with Custom User Model

---

## ⚙️ Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python 3.10+** installed
- **MySQL Server** installed and running
- **pip** (Python package manager)

---

## 🔧 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/hospital-management-system.git
   cd hospital-management-system
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   # Activate on Windows CMD
   venv\Scripts\activate
   # Activate on PowerShell
   .\venv\Scripts\activate
   # Activate on Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: You may need to create a `requirements.txt` first: `pip freeze > requirements.txt`)*

4. **Database Configuration**
   - Ensure your MySQL server is running.
   - Create a database named `hospital_db` (or update `settings.py` to match yours).
   - Update `hospital_management/settings.py` with your MySQL credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'hospital_db',
             'USER': 'root',      # Your MySQL User
             'PASSWORD': 'root',  # Your MySQL Password
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000/`.

---

## 📸 Screenshots

*(Add screenshots of your application here)*

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📞 Contact

Project Link: [https://github.com/yourusername/hospital-management-system](https://github.com/yourusername/hospital-management-system)
