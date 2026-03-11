# 🌍 ELocate - E-Waste Facility Locator & Device Resale Platform

A comprehensive Django web application that helps users find certified e-waste recycling centers, calculate device resale value with AI-powered screenshot analysis, and track environmental impact.

## ✨ Features

### 🗺️ Interactive Map
- Find 10+ certified e-waste recycling centers across India
- Real-time distance calculation from user location
- Auto-sorted facility list (nearest first)
- Interactive markers with facility details
- Powered by Leaflet.js

### 💰 Smart Device Calculator
- **Manual Entry**: Input device specifications manually
- **📸 Screenshot Upload**: AI-powered OCR extracts specs from screenshots
- **Condition-Based Pricing**: Pristine, Mint, Overused tiers
- **Working Status**: Fully working, Minor issues, Major issues, Not working
- **Database-Driven**: 20+ device configurations with real INR prices
- **Age Depreciation**: Automatic value calculation based on device age

### 🔐 User Authentication
- Secure login/registration system
- Protected routes (login required for map & calculator)
- Personal dashboard with statistics

### 📊 User Dashboard
- Total devices recycled
- Total value earned (₹)
- CO2 emissions saved (kg)
- Recent recycling activity history

### 🌱 Environmental Impact
- Carbon footprint calculation
- CO2 savings tracking
- Educational information hub

## 🛠️ Tech Stack

- **Backend**: Django 4.2+ (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Database**: SQLite
- **Maps**: Leaflet.js with OpenStreetMap
- **OCR**: Tesseract OCR + Pillow
- **Authentication**: Django Auth System

## 📦 Installation

### Prerequisites
- Python 3.8+
- Tesseract OCR (for screenshot feature)

### 1. Clone Repository
```bash
git clone <repository-url>
cd E-Waste-Facility-Locater
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

**Windows:**
- Download: https://github.com/UB-Mannheim/tesseract/wiki
- Install to: `C:\Program Files\Tesseract-OCR`
- Update path in `elocate/settings.py` if needed

**Mac:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User
```bash
python manage.py createsuperuser
```

### 6. Populate Device Prices (INR)
```bash
python populate_device_prices_inr.py
```

### 7. Add E-Waste Facilities
```bash
python update_facilities.py
```

This adds 10 certified e-waste centers across India.

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

## 🚀 Usage

### For Users

1. **Register/Login**: Create account to access features
2. **Find Centers**: View map with nearest recycling centers
3. **Calculate Value**: 
   - Enter device specs manually, OR
   - Upload screenshot of device info
4. **Track Impact**: View dashboard with recycling statistics

### For Admins

- Admin Panel: `http://127.0.0.1:8000/admin/`
- Manage facilities, device prices, users
- View all recycling logs

## 💡 Key Features Explained

### Screenshot Upload (OCR)
Users can upload screenshots of their device's "About" page:
- **Windows**: Settings → System → About
- **Mac**: Apple Menu → About This Mac

AI extracts:
- Brand (Apple, Dell, HP, Lenovo, etc.)
- Processor (i3/i5/i7, Ryzen, M1/M2)
- RAM (4GB-128GB)
- GPU (Integrated, RTX, GTX series)
- Storage (256GB-2TB)

### Pricing System

**Database Prices (20+ devices):**
- MacBook Air M1: ₹70,000 (Pristine) → ₹62,000 (Mint) → ₹45,000 (Overused)
- Dell XPS 13 i7: ₹75,000 → ₹62,000 → ₹45,000
- HP Omen RTX3050: ₹78,000 → ₹66,000 → ₹49,000

**Working Status Multipliers:**
- Fully Working: 100%
- Minor Issues: 85%
- Major Issues: 60%
- Not Working: 30%

**Formula:**
```
Final Price = Base Price × Age Depreciation × Working Status
```

### Certified E-Waste Centers

10 real facilities included:
- Attero Recycling (Roorkee, Uttarakhand)
- E-Parisaraa (Bangalore, Karnataka)
- Eco Recycling (Mumbai, Maharashtra)
- Greenscape Eco (Delhi)
- Techchef E-Waste (New Delhi)
- And 5 more across India

## 📁 Project Structure

```
E-Waste-Facility-Locater/
├── core/                          # Main Django app
│   ├── models.py                 # Database models
│   ├── views.py                  # View logic + OCR
│   ├── urls.py                   # URL routing
│   ├── admin.py                  # Admin config
│   ├── static/
│   │   ├── css/style.css        # Styling
│   │   └── js/
│   │       ├── calculator.js    # Calculator logic
│   │       └── map.js           # Map + sorting
│   └── templates/core/
│       ├── home.html
│       ├── map.html
│       ├── calculator.html
│       ├── dashboard.html
│       ├── login.html
│       └── register.html
├── elocate/                      # Project settings
│   ├── settings.py
│   └── urls.py
├── db.sqlite3                    # Database
├── manage.py
├── requirements.txt
├── populate_device_prices_inr.py
└── update_facilities.py
```

## 🔒 Security Features

- Login required for map and calculator
- CSRF protection enabled
- Password hashing (Django default)
- Secure session management

## 🌟 Highlights

✅ Real certified e-waste centers
✅ AI-powered screenshot analysis
✅ INR pricing (Indian market)
✅ Distance-based sorting
✅ User dashboard with stats
✅ Responsive design
✅ Interactive animations
✅ Environmental impact tracking

## 📝 License

MIT License - Free for educational and commercial use.

## 🤝 Contributing

Contributions welcome! Please open an issue or submit a pull request.

## 📧 Support

For issues or questions, please open a GitHub issue.

---

**Made with 💚 for a sustainable future**
