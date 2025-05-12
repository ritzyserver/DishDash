# DishDash - Canteen Management System 🍽️

DishDash is a modern, user-friendly canteen management system built with Django that streamlines food ordering and stall management in a campus environment.

## ✨ Features

### 🛍️ For Customers
- **Easy Order Placement**: Browse through various stalls and their menus
- **Shopping Cart**: Add multiple items from different stalls
- **Order Tracking**: Track order status from placement to delivery
- **Recipe Blog**: Explore food recipes and cooking instructions
- **Stall Directory**: Access stall information and contact details

### 🏪 For Stall Owners
- **Order Management**: Real-time order notifications and status updates
- **Menu Management**: Easy menu item addition and updates
- **Dashboard**: Track orders and manage inventory
- **Profile Management**: Update stall information and contact details

## 🛠️ Technical Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **Authentication**: Django Authentication System

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/ritzyserver/DishDash.git
   cd DishDash
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Seed sample data**
   ```bash
   python manage.py seed_stalls
   python manage.py seed_recipes
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` to access the application.

## 📱 Features Overview

### Home Page
- Clean and intuitive interface
- Quick access to all stalls
- Featured recipes section

### Orders System
- Real-time order tracking
- Multiple payment options
- Order history and status updates

### Recipe Blog
- Detailed recipe instructions
- Cooking time and ingredients list
- Stall attribution for recipes

### Contact Directory
- Comprehensive stall information
- Direct contact options
- Social media integration

## 🔒 Environment Variables

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your_secret_key
```

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/enhancement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/enhancement`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ✨ Acknowledgments

- Beautiful UI design inspired by modern food delivery apps
- Bootstrap for responsive design
- Django community for excellent documentation