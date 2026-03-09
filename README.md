# 🌍 ELocate - E-Waste Locator & Device Impact Calculator

A Django web application that helps users find e-waste recycling centers, calculate device resale value, and estimate carbon emission savings.

## Features

- 📍 **Interactive Map**: Find nearby e-waste recycling centers using Leaflet.js
- 💰 **Device Value Calculator**: Estimate resale value based on brand, processor, GPU, condition, and age
- 🎯 **Condition-Based Pricing**: Three pricing tiers (Pristine, Mint, Overused) with real market data
- 🗄️ **Database-Driven Prices**: 20+ device configurations with accurate resale values
- 🌱 **Carbon Savings**: Calculate CO2 emissions saved by recycling
- 👤 **User Authentication**: Track personal recycling history and impact
- 📊 **Dashboard**: View total devices recycled, value earned, and carbon saved
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

### 2. Run Migrations.......

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 4. Populate Device Prices (INR)

```bash
python populate_device_prices_inr.py
```

This adds 20 real device configurations with Indian market pricing.

### 5. Add Sample Facilities (Optional)

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

### 6. Run Development Server

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
- Manage device prices (NEW!)
- View recycling logs

### Device Condition Pricing (NEW!)

The calculator now uses **database-driven pricing** with three condition tiers:

1. **✨ Pristine** - Like new, no scratches (highest value)
2. **⭐ Mint** - Minor wear, fully functional (standard value)
3. **🔧 Overused** - Heavy wear, functional (lower value)

**Example Prices:**
- MacBook Air M1: Pristine ₹70,000 | Mint ₹62,000 | Overused ₹45,000
- Dell XPS 13 i7: Pristine ₹75,000 | Mint ₹62,000 | Overused ₹45,000
- HP Omen RTX3050: Pristine ₹78,000 | Mint ₹66,000 | Overused ₹49,000

### Calculator Logic

**Database-Driven Pricing:**
```
Base Price (from database by condition) × Age Depreciation (12% per year)
```

**Fallback Formula (if device not in database):**
```
Base Value × Processor Multiplier + GPU Bonus × Condition Multiplier × Age Depreciation
```

**Carbon Savings Formula:**
```
Device Weight (kg) × Material Factor
- Plastic: 2.5 kg CO2/kg
- Aluminum: 8.0 kg CO2/kg
- Mixed: 5.0 kg CO2/kg
```

## Adding Custom Device Prices

Use `add_custom_devices.py` template to add more devices:

```python
custom_devices = [
    {
        'brand': 'Apple',
        'model_name': 'MacBook Pro 16',
        'processor': 'M1',
        'gpu': 'Integrated',
        'pristine_price': 1800,
        'mint_price': 1550,
        'overused_price': 1150,
        'release_year': 2021
    }
]
```

See `CONDITION_PRICING_GUIDE.md` for detailed documentation.

## Future Enhancements

- User authentication
- Booking system for pickups
- Mobile app version
- Real-time facility availability
- Community forum

## License

MIT License - Feel free to use for educational purposes.
