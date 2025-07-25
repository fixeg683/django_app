# Django Ecommerce Store

A full-featured ecommerce web application built with Django. This project provides a robust platform for selling products online, featuring user authentication, product catalog, shopping cart, order processing, and admin management.

## Features

- User registration, login, and profile management
- Browse and search products by category or keyword
- Product details page with images, description, and reviews
- Shopping cart functionality: add, update, and remove items
- Secure checkout and order placement
- Order history and tracking for users
- Admin dashboard for managing products, orders, and users
- Responsive design for mobile and desktop devices

## Tech Stack

- **Backend:** Django, Django Rest Framework
- **Frontend:** HTML5, CSS3, JavaScript (optionally React or Vue.js for SPA)
- **Database:** SQLite (default), PostgreSQL/MySQL supported
- **Authentication:** Django authentication system
- **Payments:** (Optional) Integrate Stripe, PayPal, or other gateways

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-ecommerce-store.git
   cd django-ecommerce-store
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the site**
   - Frontend: `http://localhost:8000/`
   - Admin: `http://localhost:8000/admin/`

## Configuration

- Update `settings.py` for database, email, and payment gateway settings as needed.
- To enable payment gateways, add API keys in environment variables or `settings.py`.

## Folder Structure

```
django-ecommerce-store/
│
├── ecommerce/                # Main project folder
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── store/                    # Core app for store features
├── accounts/                 # User authentication and profiles
├── cart/                     # Shopping cart logic
├── orders/                   # Order management
├── templates/                # HTML templates
├── static/                   # Static files (CSS, JS, images)
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/) (for UI)
- [Stripe](https://stripe.com/) and [PayPal](https://paypal.com/) (for payment integration)
