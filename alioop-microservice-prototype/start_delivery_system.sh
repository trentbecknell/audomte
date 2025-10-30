#!/bin/bash
# Start the complete delivery system

echo "🎵 Starting Audio Delivery System..."
echo ""

# Check if we're in the right directory
if [ ! -f "app/main.py" ]; then
    echo "❌ Error: Please run this from the alioop-microservice-prototype directory"
    exit 1
fi

# Check Python environment
if ! python -c "import fastapi" 2>/dev/null; then
    echo "⚠️  Installing dependencies..."
    pip install -r requirements.txt
fi

echo "✅ Dependencies ready"
echo ""

# Start the web server in background
echo "🌐 Starting web server on http://localhost:8000 ..."
uvicorn app.main:app --reload &
WEB_PID=$!
sleep 2

echo "✅ Web server running (PID: $WEB_PID)"
echo ""

# Instructions for file watcher
echo "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "="
echo "🎯 DELIVERY SYSTEM READY!"
echo "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "=" "="
echo ""
echo "📱 Web UI: http://localhost:8000"
echo "   - Add/manage clients"
echo "   - View deliveries"
echo "   - Verify payments"
echo ""
echo "📁 Watch Folder: ~/Desktop/AudioDeliveries/"
echo ""
echo "To start file watching:"
echo "   python file_watcher.py"
echo ""
echo "Press Ctrl+C to stop the web server"
echo ""

# Wait for user interrupt
wait $WEB_PID
