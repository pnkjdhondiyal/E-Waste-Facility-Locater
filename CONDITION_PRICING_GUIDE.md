# Device Condition-Based Pricing Update

## What's New

The calculator now uses a **database-driven pricing system** with **three condition tiers**:

### Condition Types

1. **✨ Pristine** - Like new, no scratches, perfect condition
   - Highest resale value (100-120% of mint price)
   
2. **⭐ Mint** - Minor wear, fully functional, good condition
   - Standard resale value (baseline price)
   
3. **🔧 Overused** - Heavy wear, visible damage, but functional
   - Lower resale value (60-70% of mint price)

## How It Works

### Database-Driven Pricing
- Real market prices stored in `DevicePrice` model
- Prices based on actual resale market data
- Covers 20+ popular device configurations
- Includes Apple, Dell, HP, Lenovo, Samsung brands

### Calculation Logic
1. System searches database for matching device (brand + processor + GPU)
2. Retrieves condition-specific base price
3. Applies age depreciation (12% per year)
4. Returns accurate resale estimate

### Fallback System
- If device not in database, uses formula-based calculation
- Ensures all devices get estimates

## Setup Instructions

### 1. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Populate Device Prices
```bash
python populate_device_prices.py
```

This adds 20 device configurations with real market prices.

### 3. Manage Prices (Admin Panel)
- Access: `http://127.0.0.1:8000/admin/`
- Navigate to "Device Prices"
- Add/edit/delete device prices
- Set custom prices for pristine, mint, and overused conditions

## Database Schema

### DevicePrice Model
```python
- brand: Device manufacturer
- model_name: Specific model
- processor: CPU type
- gpu: Graphics card
- ram_gb: RAM capacity
- storage_gb: Storage capacity
- pristine_price: Price for pristine condition
- mint_price: Price for mint condition
- overused_price: Price for overused condition
- release_year: Year of release
```

## Example Prices

| Device | Pristine | Mint | Overused |
|--------|----------|------|----------|
| MacBook Air M1 | $850 | $750 | $550 |
| Dell XPS 13 i7 | $900 | $750 | $550 |
| HP Omen RTX3050 | $950 | $800 | $600 |
| Lenovo Legion RTX3060 | $1150 | $980 | $720 |

## Benefits

✅ **Accurate Pricing** - Based on real market data
✅ **Condition-Aware** - Reflects actual device state
✅ **Easy Management** - Update prices via admin panel
✅ **Scalable** - Add unlimited device configurations
✅ **User-Friendly** - Simple dropdown selection

## Future Enhancements

- Import prices from external APIs
- Automatic price updates
- Regional pricing variations
- Historical price tracking
