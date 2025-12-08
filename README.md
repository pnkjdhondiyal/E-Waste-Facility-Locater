# 🌍 ELocate - E-Waste Locator & Device Impact Calculator

A Django web application that helps users find e-waste recycling centers, calculate device resale value, and estimate carbon emission savings.

## Features

- 📍 **Interactive Map**: Find nearby e-waste recycling centers using Leaflet.js
- 💰 **Device Value Calculator**: Estimate resale value based on brand, processor, GPU, and age
- 🌱 **Carbon Savings**: Calculate CO2 emissions saved by recycling
- 📚 **Information Hub**: Learn about e-waste recycling importance

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Map**: Leaflet.js
- **Database**: SQLite

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 4. Add Sample Data (Optional)

You can add recycling facilities through the admin panel at `http://127.0.0.1:8000/admin/`

Or use Django shell:

```bash
python manage.py shell
```

Then run:

```python
from core.models import Facility

Facility.objects.create(
    name="Green E-Waste Recycling Center",
    address="123 Main Street, Delhi",
    latitude=28.6139,
    longitude=77.2090,
    phone="+91-1234567890",
    email="info@greenewaste.com"
)

Facility.objects.create(
    name="EcoTech Recyclers",
    address="456 Park Avenue, Delhi",
    latitude=28.5355,
    longitude=77.3910,
    phone="+91-9876543210",
    email="contact@ecotech.com"
)
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure

```
elocate/
├── core/                      # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # URL routing
│   ├── admin.py              # Admin configuration
│   ├── static/               # Static files
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       ├── calculator.js
│   │       └── map.js
│   └── templates/            # HTML templates
│       └── core/
│           ├── home.html
│           ├── map.html
│           ├── calculator.html
│           └── info.html
├── elocate/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Usage

### Admin Panel
- Access: `http://127.0.0.1:8000/admin/`
- Add/manage recycling facilities
- View recycling logs

### Calculator Logic

**Resale Value Formula:**
```
Base Value (by brand) × Processor Multiplier + GPU Bonus × Depreciation Factor
```

**Carbon Savings Formula:**
```
Device Weight (kg) × Material Factor
- Plastic: 2.5 kg CO2/kg
- Aluminum: 8.0 kg CO2/kg
- Mixed: 5.0 kg CO2/kg
```

## Future Enhancements

- User authentication
- Booking system for pickups
- Mobile app version
- Real-time facility availability
- Community forum

## License

MIT License - Feel free to use for educational purposes.
