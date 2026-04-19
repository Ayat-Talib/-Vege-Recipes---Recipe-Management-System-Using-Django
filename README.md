"# -Vege-Recipes---Recipe-Management-System-Using-Django" 
# 🍃 Vege Recipes - Recipe Management System

A beautiful and fully functional recipe management web application built with Django. Users can add, view, edit, and delete recipes with images and descriptions.

## ✨ Features

- ✅ User Authentication (Login/Logout)
- ✅ Add new recipes with name, description & image
- ✅ View all recipes in beautiful grid layout
- ✅ Edit existing recipes
- ✅ Delete recipes with confirmation
- ✅ Read more/less toggle for long descriptions
- ✅ Image upload support
- ✅ Responsive design for mobile & tablet
- ✅ Modern UI with hover effects

## 🛠️ Tech Stack

- **Backend:** Django 5.x
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3
- **Icons:** Font Awesome 6
- **Fonts:** Google Poppins

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/vege-recipes.git

# Enter the directory
cd vege-recipes

# Create virtual environment
python -m venv env

# Activate virtual environment (Windows)
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
