# 🚀 Quick Start Guide

## Step 1: Install Django
```bash
pip install -r requirements.txt
```

## Step 2: Setup Database
```bash
python manage.py migrate
```

## Step 3: Add Sample Recycling Centers
```bash
python add_sample_data.py
```

## Step 4: Create Admin Account (Optional)
```bash
python manage.py createsuperuser
```

## Step 5: Run Server
```bash
python manage.py runserver
```

## Step 6: Open Browser
Visit: **http://127.0.0.1:8000/**

---

## ✅ What's Fixed:

### Calculator Issue:
- Removed CSRF token requirement
- Added proper error handling
- Values now display correctly

### Map Issue:
- Added sample facilities (5 centers in Delhi)
- Shows list of centers with addresses
- Calculates distance from your location
- Click markers to see details

---

## 📝 Features Working:

1. **Home Page** - Overview and navigation
2. **Map Page** - Shows recycling centers with distances
3. **Calculator** - Calculates device value + carbon savings
4. **Info Page** - E-waste recycling information

---

## 🔧 Troubleshooting:

**If calculator shows "undefined":**
- Make sure server is running
- Check browser console (F12) for errors
- Verify all form fields are filled

**If map shows no centers:**
- Run: `python add_sample_data.py`
- Or add via admin: http://127.0.0.1:8000/admin/

**If map doesn't show your location:**
- Allow location access in browser
- Map will still show all centers
