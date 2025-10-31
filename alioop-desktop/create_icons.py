#!/usr/bin/env python3
"""
Generate all icon assets for Alioop Desktop app
Creates: icon.png, tray-icon.png, and platform-specific formats
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Brand colors
ORANGE = '#f05709'
BLACK = '#161614'
CREAM = '#fcf5eb'

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_app_icon(size=512):
    """Create main app icon (512x512)"""
    img = Image.new('RGBA', (size, size), hex_to_rgb(BLACK) + (255,))
    draw = ImageDraw.Draw(img)
    
    # Draw orange circle
    margin = size // 8
    draw.ellipse(
        [margin, margin, size - margin, size - margin],
        fill=hex_to_rgb(ORANGE)
    )
    
    # Draw 'A' letter
    try:
        # Try to use a nice font
        font_size = size // 2
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        # Fallback to default
        font = ImageFont.load_default()
    
    # Draw text
    text = "A"
    # Get text bbox for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - size // 20  # Slight adjustment up
    
    draw.text((x, y), text, fill=hex_to_rgb(BLACK), font=font)
    
    return img

def create_tray_icon(size=32):
    """Create system tray icon (32x32)"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw orange circle with slight padding for tray
    margin = 2
    draw.ellipse(
        [margin, margin, size - margin, size - margin],
        fill=hex_to_rgb(ORANGE)
    )
    
    # Draw simple 'A' or icon symbol
    try:
        font_size = size - 12
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "A"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - 2
    
    draw.text((x, y), text, fill=hex_to_rgb(CREAM), font=font)
    
    return img

def save_icns(img, output_path):
    """Save as .icns for macOS (multi-resolution)"""
    # Create iconset directory
    iconset_dir = output_path.replace('.icns', '.iconset')
    os.makedirs(iconset_dir, exist_ok=True)
    
    # Generate all required sizes for macOS
    sizes = [16, 32, 64, 128, 256, 512, 1024]
    for size in sizes:
        # Standard resolution
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(f'{iconset_dir}/icon_{size}x{size}.png')
        
        # Retina resolution (2x)
        if size <= 512:
            resized_2x = img.resize((size * 2, size * 2), Image.Resampling.LANCZOS)
            resized_2x.save(f'{iconset_dir}/icon_{size}x{size}@2x.png')
    
    # Convert to icns using iconutil (macOS only)
    print(f"Created iconset at {iconset_dir}")
    print(f"To create .icns on macOS, run: iconutil -c icns {iconset_dir}")

def save_ico(img, output_path):
    """Save as .ico for Windows (multi-resolution)"""
    # Create multiple sizes for Windows
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    
    # Resize and save all sizes
    img.save(output_path, format='ICO', sizes=sizes)
    print(f"Created {output_path}")

def main():
    """Generate all icons"""
    print("🎨 Generating Alioop Desktop icons...")
    
    # Create main app icon (512x512)
    print("\n📦 Creating app icon (512x512)...")
    app_icon = create_app_icon(512)
    app_icon.save('icon.png')
    print("✅ Created icon.png")
    
    # Create additional sizes
    app_icon_256 = create_app_icon(256)
    app_icon_256.save('icon-256.png')
    print("✅ Created icon-256.png")
    
    # Create tray icon (32x32)
    print("\n🔔 Creating tray icon (32x32)...")
    tray_icon = create_tray_icon(32)
    tray_icon.save('tray-icon.png')
    print("✅ Created tray-icon.png")
    
    # Create tray icon at 2x for retina
    tray_icon_64 = create_tray_icon(64)
    tray_icon_64.save('tray-icon@2x.png')
    print("✅ Created tray-icon@2x.png")
    
    # Create .ico for Windows
    print("\n🪟 Creating Windows icon (.ico)...")
    save_ico(app_icon, 'icon.ico')
    
    # Create .icns for macOS (requires iconutil on macOS)
    print("\n🍎 Creating macOS iconset...")
    save_icns(app_icon, 'icon.icns')
    
    print("\n✨ All icons generated successfully!")
    print("\nFiles created:")
    print("  - icon.png (512x512) - Main app icon")
    print("  - icon-256.png (256x256) - Medium app icon")
    print("  - tray-icon.png (32x32) - System tray icon")
    print("  - tray-icon@2x.png (64x64) - Retina tray icon")
    print("  - icon.ico - Windows icon (multi-size)")
    print("  - icon.iconset/ - macOS iconset directory")
    print("\nNote: Run 'iconutil -c icns icon.iconset' on macOS to create icon.icns")

if __name__ == '__main__':
    main()
