#!/usr/bin/env python3
"""
Generates data.js from Agnes_Riley_CV.yaml
Run this after updating the YAML to regenerate the JS data file.
"""
import yaml
import json

with open('Agnes_Riley_CV.yaml', 'r') as f:
    data = yaml.safe_load(f)

cv = data['cv']
sections = cv['sections']

# Build the data object
cv_data = {
    "name": cv['name'],
    "location": cv['location'],
    "email": cv['email'],
    "phone": cv['phone'],
    "website": cv['website'],
    "linkedin": f"https://linkedin.com/in/{cv['social_networks'][0]['username']}",
    "summary": sections['summary'][0] if sections.get('summary') else "",
    "skills": sections['skills'],
    "experience": sections['experience'],
    "education": sections['education'],
    "certifications": sections['certifications']
}

# Write as JS module
with open('data.js', 'w') as f:
    f.write('// Auto-generated from Agnes_Riley_CV.yaml - do not edit directly\n')
    f.write('const cvData = ')
    f.write(json.dumps(cv_data, indent=2))
    f.write(';\n')

print("✅ Generated data.js from YAML")
