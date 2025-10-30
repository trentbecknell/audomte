# Design Assets

This folder contains images and design assets for the Alioop audio delivery platform.

## 📁 Folder Structure

```
images/
├── logos/          - Brand logos and variations
├── screenshots/    - Application screenshots
├── icons/          - UI icons and graphics
└── backgrounds/    - Background images and patterns
```

## 🎨 Recommended Image Specs

### Logos
- **Main Logo:** 512x512px PNG with transparency
- **Favicon:** 32x32px ICO or PNG
- **Social Media:** 1200x630px for OpenGraph previews

### Screenshots
- **Desktop:** 1920x1080px or higher
- **Mobile:** 375x812px (iPhone X dimensions)
- **Tablet:** 768x1024px (iPad dimensions)

### Icons
- **SVG preferred** for scalability
- **PNG fallback:** 64x64px minimum
- Use transparent backgrounds

## 📝 Usage in Templates

To use images in your templates:

```html
<!-- In landing.html or delivery.html -->
<img src="{{ url_for('static', path='/images/logos/logo.png') }}" alt="Alioop Logo">

<!-- Or direct path -->
<img src="/static/images/logos/logo.png" alt="Alioop Logo">
```

## 🎯 Quick Tips

1. **Optimize images** before uploading (use TinyPNG or similar)
2. **Name files descriptively:** `hero-background.jpg` not `img1.jpg`
3. **Use web-friendly formats:** JPG for photos, PNG for graphics with transparency
4. **Include 2x versions** for retina displays: `logo@2x.png`

## 📦 Current Assets

Drop your design files here! Supported formats:
- PNG, JPG, GIF, SVG, WebP
- ICO for favicons
- Any other static assets
