#!/usr/bin/env python3
import yaml

with open('Agnes_Riley_CV.yaml', 'r') as f:
    data = yaml.safe_load(f)

cv = data['cv']
sections = cv['sections']

linkedin_url = f"https://linkedin.com/in/{cv['social_networks'][0]['username']}"
summary = sections['summary'][0] if sections.get('summary') else ""

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{cv['name']} - CV</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Inter', 'sans-serif'] }},
                    colors: {{
                        brand: {{ 50: '#fdf4ff', 100: '#fae8ff', 200: '#f5d0fe', 300: '#f0abfc', 400: '#e879f9', 500: '#d946ef', 600: '#c026d3', 700: '#a21caf', 800: '#86198f', 900: '#701a75' }}
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-zinc-950 min-h-screen py-12 px-4 font-sans">
    <div class="max-w-6xl mx-auto" x-data="{{ activeTab: 'experience' }}">
        
        <!-- Hero Section -->
        <div class="relative mb-8 rounded-3xl overflow-hidden bg-gradient-to-br from-zinc-900 via-zinc-800 to-zinc-900 border border-zinc-700/50">
            <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-fuchsia-900/20 via-transparent to-transparent"></div>
            <div class="absolute top-0 right-0 w-96 h-96 bg-fuchsia-500/10 rounded-full blur-3xl"></div>
            <div class="absolute bottom-0 left-0 w-64 h-64 bg-violet-500/10 rounded-full blur-3xl"></div>
            
            <div class="relative px-8 md:px-12 py-12">
                <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-6">
                    <div>
                        <p class="text-fuchsia-400 text-sm font-medium tracking-wider uppercase mb-2">IT Professional & Solutions Architect</p>
                        <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-white tracking-tight">{cv['name']}</h1>
                    </div>
                    <div class="flex flex-wrap gap-3">
                        <a href="tel:{cv['phone']}" class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 text-zinc-300 text-sm transition">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                            {cv['phone']}
                        </a>
                        <a href="mailto:{cv['email']}" class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 text-zinc-300 text-sm transition">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                            Email
                        </a>
                        <a href="{linkedin_url}" target="_blank" class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 text-zinc-300 text-sm transition">
                            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                            LinkedIn
                        </a>
                        <a href="{cv['website']}" target="_blank" class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 text-zinc-300 text-sm transition">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                            Credly
                        </a>
                    </div>
                </div>
                
                <div class="mt-8 pt-8 border-t border-white/10">
                    <p class="text-zinc-400 text-lg leading-relaxed max-w-3xl">
                        <span class="text-fuchsia-400 font-semibold">20+ years</span> of experience. {summary}
                    </p>
                </div>
            </div>
        </div>

        <!-- Skills Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
'''

skills_icons = [
    ("M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z", "fuchsia"),
    ("M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4", "violet"),
    ("M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2", "emerald"),
    ("M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z", "amber")
]

for i, skill in enumerate(sections['skills']):
    icon_path, color = skills_icons[i]
    html += f'''            <div class="group p-6 rounded-2xl bg-zinc-900/50 border border-zinc-800 hover:border-{color}-500/50 hover:bg-zinc-900 transition-all duration-300">
                <div class="w-10 h-10 rounded-xl bg-{color}-500/10 flex items-center justify-center mb-4 group-hover:bg-{color}-500/20 transition">
                    <svg class="w-5 h-5 text-{color}-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="{icon_path}"/></svg>
                </div>
                <h3 class="font-semibold text-white mb-2">{skill['label']}</h3>
                <p class="text-sm text-zinc-500 leading-relaxed">{skill['details']}</p>
            </div>
'''

html += '''        </div>

        <!-- Tabs Section -->
        <div class="rounded-3xl bg-zinc-900/50 border border-zinc-800 overflow-hidden">
            <div class="flex border-b border-zinc-800">
                <button @click="activeTab = 'experience'" :class="activeTab === 'experience' ? 'text-white border-fuchsia-500 bg-fuchsia-500/10' : 'text-zinc-500 border-transparent hover:text-zinc-300'" class="flex-1 md:flex-none px-8 py-4 text-sm font-medium border-b-2 transition-all">
                    Experience
                </button>
                <button @click="activeTab = 'education'" :class="activeTab === 'education' ? 'text-white border-fuchsia-500 bg-fuchsia-500/10' : 'text-zinc-500 border-transparent hover:text-zinc-300'" class="flex-1 md:flex-none px-8 py-4 text-sm font-medium border-b-2 transition-all">
                    Education
                </button>
                <button @click="activeTab = 'certs'" :class="activeTab === 'certs' ? 'text-white border-fuchsia-500 bg-fuchsia-500/10' : 'text-zinc-500 border-transparent hover:text-zinc-300'" class="flex-1 md:flex-none px-8 py-4 text-sm font-medium border-b-2 transition-all">
                    Certifications
                </button>
            </div>

            <!-- Experience -->
            <div x-show="activeTab === 'experience'" x-transition class="p-6 md:p-8">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
'''

for job in sections['experience']:
    year = str(job['start_date']).split('-')[0]
    html += f'''                    <div class="group p-6 rounded-2xl bg-zinc-800/30 border border-zinc-800 hover:border-zinc-700 transition-all">
                        <div class="flex flex-col md:flex-row md:items-start md:justify-between gap-2 mb-4">
                            <div>
                                <h3 class="font-semibold text-white text-lg">{job['position']}</h3>
                                <p class="text-fuchsia-400 text-sm">{job['company']} · {job['location']}</p>
                            </div>
                            <span class="text-xs text-zinc-500 bg-zinc-800 px-3 py-1 rounded-full whitespace-nowrap">{job['start_date']} – {job['end_date']}</span>
                        </div>
                        <ul class="space-y-2">
'''
    for highlight in job['highlights'][:3]:
        html += f'''                            <li class="flex gap-3 text-sm text-zinc-400"><span class="text-fuchsia-500 mt-1">▸</span><span>{highlight}</span></li>
'''
    html += '''                        </ul>
                    </div>
'''

html += '''                </div>
            </div>

            <!-- Education -->
            <div x-show="activeTab === 'education'" x-transition class="p-6 md:p-8">
                <div class="grid md:grid-cols-2 gap-4">
'''

for edu in sections['education']:
    html += f'''                    <div class="p-5 rounded-xl bg-zinc-800/30 border border-zinc-800">
                        <h3 class="font-medium text-white">{edu['institution']}</h3>
                        <p class="text-sm text-fuchsia-400">{edu['area']}</p>
                        <p class="text-xs text-zinc-500 mt-2">{edu['location']} · {edu['start_date']} – {edu['end_date']}</p>
                    </div>
'''

html += '''                </div>
            </div>

            <!-- Certifications -->
            <div x-show="activeTab === 'certs'" x-transition class="p-6 md:p-8">
                <div class="grid md:grid-cols-2 gap-3">
'''

for cert in sections['certifications']:
    html += f'''                    <div class="flex items-center gap-3 p-4 rounded-xl bg-zinc-800/30 border border-zinc-800">
                        <div class="w-8 h-8 rounded-lg bg-emerald-500/10 flex items-center justify-center flex-shrink-0">
                            <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                        </div>
                        <span class="text-sm text-zinc-300">{cert}</span>
                    </div>
'''

html += '''                </div>
            </div>
        </div>

        <footer class="mt-8 text-center text-zinc-600 text-xs">
            <p>© 2025 Agnes B. Riley</p>
        </footer>
    </div>
</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Created modern dark theme CV - no more icky blue!")
print(f"📊 {len(sections['experience'])} jobs, {len(sections['education'])} education, {len(sections['certifications'])} certs")
