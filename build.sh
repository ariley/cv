#!/bin/bash
# Build script - regenerates all CV outputs from YAML

echo "�� Building CV from Agnes_Riley_CV.yaml..."

# Generate PDF, HTML, etc with rendercv
echo "📄 Running rendercv..."
rendercv render Agnes_Riley_CV.yaml

# Generate data.js for the interactive website
echo "📊 Generating data.js..."
python3 build_data.py

echo "✅ Done! All outputs updated."
