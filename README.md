# 📋 Job Application Tracker

A full-stack web application built with Flask to help users track and manage their job applications efficiently. This project demonstrates modern web development practices with a clean, responsive UI and complete CRUD functionality.

## 🌐 Live Demo

**🚀 [View Live Application](https://full-stack-project-ygvp.onrender.com/)**

The application is deployed and running on Render. Feel free to explore all features!

> **Note**: Free tier apps may take 30-60 seconds to wake up on first visit.

## 🎯 Overview

The Job Application Tracker is a comprehensive web application that allows users to organize their job search process by tracking applications, monitoring status changes, and viewing analytics through an interactive dashboard. The application features a custom purple-teal gradient theme with smooth animations and modern UI/UX design.

## ✨ Features

### Core Functionality
- **Create**: Add new job applications with company name, role, date, status, and notes
- **Read**: View all applications in a sortable, filterable table
- **Update**: Edit existing application details
- **Delete**: Remove applications with confirmation modal
- **Filter**: Real-time filtering by application status (Applied, Interview, Rejected, Offer)
- **Dashboard**: Visual statistics showing total applications and status breakdown

### Technical Features
- Client-side form validation with Bootstrap 5
- Server-side validation for data integrity
- SQLite database with SQLAlchemy ORM
- Responsive design that works on all devices
- Flash messages for user feedback
- jQuery-powered dynamic filtering and DOM manipulation
- Confirmation modals for destructive actions

## 🛠️ Tech Stack

### Backend
- **Flask 3.0.3** - Python web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Lightweight database
- **Jinja2** - Template engine

### Frontend
- **HTML5** - Semantic markup
- **Bootstrap 5** - Responsive UI framework
- **CSS3** - Custom styling with gradients and animations
- **JavaScript/jQuery** - Client-side interactivity

### Deployment
- **Gunicorn** - WSGI HTTP server
- **Render** - Cloud hosting platform

## 📁 Project Structure
```
Full Stack Project/
├── app.py                      # Main Flask application with routes and models
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── Procfile                    # Deployment process file
├── render.yaml                 # Render deployment configuration
├── runtime.txt                 # Python version specification
├── static/
│   ├── css/
│   │   └── styles.css         # Custom CSS with purple-teal theme
│   └── js/
│       └── main.js            # jQuery for filtering and validation
└── templates/
    ├── base.html              # Base template with navbar and footer
    ├── index.html             # Home page
    ├── add.html               # Add application form
    ├── applications.html      # List view with filtering
    ├── edit.html              # Edit application form
    └── stats.html             # Dashboard with statistics
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

## 💻 Local Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/venkatasai3005/Full-Stack-Project.git
   cd Full-Stack-Project
   ```

2. **Create and activate a virtual environment**
   
   Windows PowerShell:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
   
   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 🌐 Deployment

### ✅ Currently Deployed on Render

**Live URL**: [https://full-stack-project-ygvp.onrender.com/](https://full-stack-project-ygvp.onrender.com/)

This application is successfully deployed on Render's free tier and is accessible to anyone with the link.

### Deploy Your Own Instance

1. **Sign up** at [render.com](https://render.com)
2. **Connect your GitHub account**
3. **Create a new Web Service**
   - Repository: `venkatasai3005/Full-Stack-Project`
   - Render auto-detects the `render.yaml` configuration
4. **Click "Create Web Service"**
5. Wait 2-3 minutes for deployment
6. Access your live app at: `https://your-app-name.onrender.com`

### Manual Configuration (if needed)
```yaml
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Python Version: 3.11.0
```

### Alternative Deployment Platforms
- **Railway** - Modern platform with GitHub integration
- **PythonAnywhere** - Free tier for Flask applications
- **Vercel** - Serverless deployment option
- **Heroku** - Paid plans available (no free tier)

## 🔐 Environment Variables

For production deployment, set the following environment variables:
- `SECRET_KEY` - Strong secret key for session management (auto-generated on Render)
- `DATABASE_URL` - Database connection string (SQLite by default)

## 📝 Usage Guide

### Adding an Application
1. Navigate to "Add Application" from the navbar
2. Fill in all required fields:
   - Company Name
   - Role/Position
   - Application Date
   - Status (Applied/Interview/Rejected/Offer)
   - Notes
3. Click "Save" to add the application

### Viewing Applications
- All applications are displayed in a table format
- Use the status filter dropdown to filter by application status
- Summary badges show real-time counts for each status

### Editing/Deleting
- Click "Edit" to modify an existing application
- Click "Delete" to remove an application (requires confirmation)

### Dashboard
- View total applications count
- See breakdown by status with color-coded cards

## 🎨 Design Features

- **Custom Color Palette**: Purple-teal gradient theme
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Smooth Animations**: Hover effects and transitions
- **Modern UI**: Bootstrap 5 components with custom styling
- **Accessibility**: Semantic HTML and ARIA labels

## Demo Images:
<img width="1858" height="952" alt="image" src="https://github.com/user-attachments/assets/f56bc214-d1d4-47f3-87bd-5659c0199e0a" />
- This is home page
<img width="1844" height="949" alt="image" src="https://github.com/user-attachments/assets/e2460d77-2c94-487a-a7c8-a4d9d912061b" />
-This is Page Where we add jobs
<img width="1857" height="953" alt="image" src="https://github.com/user-attachments/assets/6adc13bf-9a5f-4047-a723-245ab914c003" />
-This is Where we check our applications also we can edit here or delete
<img width="1860" height="949" alt="image" src="https://github.com/user-attachments/assets/d41cef22-2a9a-442b-8dc9-e2313359a9b0" />
-This is where we can see dashboard...which will have status of our job applications and all




## 🧪 Testing

The application includes:
- Client-side form validation
- Server-side data validation
- Error handling with user-friendly messages
- Confirmation dialogs for destructive actions

## 📚 Learning Outcomes

This project demonstrates:
- Full-stack web development with Flask
- RESTful routing and CRUD operations
- Database design and ORM usage
- Frontend-backend integration
- Responsive web design
- Version control with Git
- Cloud deployment practices

## 🤝 Contributing

This is an academic project. For suggestions or improvements:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is created for educational purposes.

## 👤 Author

**Venkata Sai**
- GitHub: [@venkatasai3005](https://github.com/venkatasai3005)
- Repository: [Full-Stack-Project](https://github.com/venkatasai3005/Full-Stack-Project)

## 🙏 Acknowledgments

- Bootstrap 5 for the UI framework
- Flask documentation and community
- jQuery for DOM manipulation
- Render for hosting platform

---

**Note**: The SQLite database (`jobs.db`) is created automatically on first run. For production use with multiple users, consider upgrading to PostgreSQL or MySQL.
