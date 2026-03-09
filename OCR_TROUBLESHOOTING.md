# 🔧 OCR Troubleshooting Guide

## Issue: RAM Not Detected ("RAM: undefined")

### What I Fixed:

1. **Improved RAM Detection Patterns**
   - Now detects: "8 GB RAM", "RAM: 8GB", "8GB Memory", "Installed RAM 8 GB"
   - Multiple regex patterns for different formats
   - Validates RAM is between 2GB-128GB

2. **Image Preprocessing**
   - Converts to grayscale
   - Increases contrast (2x)
   - Better OCR accuracy

3. **Better Spec Extraction**
   - More flexible processor detection
   - Storage detection added
   - GPU detection improved

4. **Debug Mode**
   - Console shows extracted text
   - Console shows detected specs
   - Easy to troubleshoot

## How to Test:

### 1. Run Server
```bash
python manage.py runserver
```

### 2. Upload Screenshot
- Go to: http://127.0.0.1:8000/calculator/
- Click "📸 Upload Screenshot"
- Upload your device screenshot

### 3. Check Console Output
Look at the terminal/console where server is running:
```
==================================================
EXTRACTED TEXT FROM IMAGE:
Processor: Intel Core i7
RAM: 8 GB
Graphics: Integrated
==================================================
DETECTED SPECS: {'brand': 'Dell', 'processor': 'i7', 'ram': 8, 'gpu': 'Integrated'}
==================================================
```

## If RAM Still Not Detected:

### Check the Console Output:
1. Is "8 GB" or "8GB" in the extracted text?
2. If YES but not detected → Pattern issue (report the text format)
3. If NO → OCR issue (try better quality image)

### Tips for Better Detection:

✅ **Good Screenshots:**
- High resolution (at least 1920x1080)
- Clear, readable text
- Good contrast (dark text on light background)
- Crop to relevant area only
- No blur or distortion

❌ **Bad Screenshots:**
- Low resolution
- Blurry or pixelated
- Poor lighting
- Too much unnecessary content
- Handwritten text

### Example Good Screenshots:

**Windows:**
- Settings → System → About
- Right-click "This PC" → Properties
- Task Manager → Performance tab

**Mac:**
- Apple Menu → About This Mac
- System Information window

### Manual Override:

If OCR fails, you can always:
1. Switch to "⌨️ Enter Manually" tab
2. Type specs yourself
3. Get accurate pricing

## Common Text Formats Detected:

✅ "8 GB RAM"
✅ "RAM: 8 GB"
✅ "8GB Memory"
✅ "Installed RAM: 8 GB"
✅ "Memory 8 GB"
✅ "8 GB DDR4"

## Test Your Screenshot:

1. Upload screenshot
2. Check console for extracted text
3. If RAM is in text but not detected, share the exact text format
4. I can add that pattern

## Quick Fix:

If you see the text in console but specs not detected, the regex patterns need adjustment. Share the console output and I'll fix it immediately.
