# 📸 Screenshot Upload Feature - Installation Guide

## What This Feature Does

Users can upload a screenshot of their device's "About" or "System Information" page, and the system will:
1. Extract text from the image using OCR (Optical Character Recognition)
2. Automatically detect device specifications (Brand, Processor, RAM, GPU)
3. Calculate resale value based on detected specs

## Installation Steps

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Pillow (image processing)
- pytesseract (OCR library)

### 2. Install Tesseract OCR Engine

**Windows:**
1. Download installer: https://github.com/UB-Mannheim/tesseract/wiki
2. Run installer (default location: C:\Program Files\Tesseract-OCR)
3. Add to PATH or set in code:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

**Mac:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

### 3. Configure Django Settings (if needed)

Add to `elocate/settings.py` if Tesseract not in PATH:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 4. Test the Feature

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/calculator/

Click "📸 Upload Screenshot" tab

## How to Use

### For Users:

1. **Take Screenshot:**
   - Windows: Win + Shift + S or Settings → System → About
   - Mac: Cmd + Shift + 4 or Apple Menu → About This Mac

2. **Upload:**
   - Click "📸 Upload Screenshot" tab
   - Choose your screenshot
   - Select device condition
   - Enter age
   - Click "Analyze & Calculate"

3. **Get Results:**
   - System extracts specs automatically
   - Shows detected: Brand, Processor, RAM
   - Calculates resale value

## What It Detects

✅ **Brand:** Apple, Dell, HP, Lenovo, Samsung, Asus, Acer, MSI
✅ **Processor:** i3, i5, i7, i9, Ryzen3/5/7, M1, M2
✅ **RAM:** 4GB, 8GB, 16GB, 32GB, etc.
✅ **GPU:** RTX series, GTX series, Integrated

## Fallback

If specs can't be detected:
- Uses brand-based estimation
- Still provides reasonable price estimate
- User can switch to manual entry

## Example Screenshots That Work Well

✅ Windows: Settings → System → About
✅ Mac: About This Mac window
✅ System Information screenshots
✅ Device Manager screenshots
✅ Clear, high-resolution images

## Troubleshooting

**Error: "tesseract is not installed"**
- Install Tesseract OCR (see step 2)
- Add to system PATH

**Error: "No specs detected"**
- Try clearer screenshot
- Ensure text is readable
- Use manual entry as fallback

**Low accuracy:**
- Use higher resolution screenshots
- Ensure good lighting/contrast
- Crop to relevant area only

## Technical Details

- Uses Tesseract OCR for text extraction
- Regex patterns for spec detection
- Fallback to manual calculation if needed
- Supports multiple image formats (JPG, PNG, etc.)
