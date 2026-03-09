# 🚀 Quick Start - Condition-Based Pricing

## Already Setup? Just Run These:

```bash
# 1. Apply new migrations
python manage.py migrate

# 2. Populate device prices (20 devices)
python populate_device_prices.py

# 3. Start server
python manage.py runserver
```

Visit: http://127.0.0.1:8000/calculator/

## Fresh Setup? Follow These:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations
python manage.py makemigrations
python manage.py migrate

# 3. Create admin user
python manage.py createsuperuser

# 4. Populate device prices
python populate_device_prices.py

# 5. Start server
python manage.py runserver
```

## Test the Feature

1. Go to: http://127.0.0.1:8000/calculator/
2. Select:
   - Brand: Apple
   - Processor: M1
   - GPU: Integrated
   - **Condition: Pristine** ← NEW!
   - Age: 2 years
   - Weight: 1.5 kg
   - Material: Aluminum
3. Click Calculate
4. See accurate price: ~$850

## Try Different Conditions

Same device, different conditions:
- **Pristine**: $850 (like new)
- **Mint**: $750 (good condition)
- **Overused**: $550 (heavy wear)

## View All Prices

```bash
python view_device_prices.py
```

## Add More Devices

Edit `add_custom_devices.py` and run:
```bash
python add_custom_devices.py
```

## Manage via Admin

1. Visit: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Click "Device Prices"
4. Add/Edit/Delete devices

## That's It! 🎉

Your calculator now uses real market data with condition-based pricing!
