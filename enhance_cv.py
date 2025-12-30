#!/usr/bin/env python3
"""
Enhance rendercv HTML output with TailwindCSS, cards, tabs, and JavaScript
"""

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Agnes B. Riley - Interactive CV</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
    <style>
        .tab-content { display: none; }
        .tab-content.active { display: block; }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 min-h-screen py-8 px-4">
    
    <div class="max-w-7xl mx-auto" x-data="{ activeTab: 'experience' }">
        
        <!-- Hero Card -->
        <div class="bg-white rounded-2xl shadow-2xl overflow-hidden mb-6 transform hover:scale-[1.01] transition-all duration-300">
            <div class="bg-gradient-to-r from-blue-600 via-blue-700 to-indigo-700 px-8 py-12 relative overflow-hidden">
                <div class="absolute top-0 right-0 w-64 h-64 bg-white opacity-5 rounded-full -mr-32 -mt-32"></div>
                <div class="absolute bottom-0 left-0 w-48 h-48 bg-white opacity-5 rounded-full -ml-24 -mb-24"></div>
                <div class="relative z-10">
                    <h1 class="text-5xl md:text-6xl font-bold text-white mb-3">Agnes B. Riley</h1>
                    <p class="text-2xl text-blue-100 mb-6">IT Professional & Solutions Architect</p>
                    <div class="flex flex-wrap gap-4 text-sm text-white">
                        <a href="tel:+19176607221" class="flex items-center gap-2 bg-white/10 hover:bg-white/20 px-4 py-2 rounded-lg backdrop-blur-sm transition">
                            📞 +1 917 660 7221
                        </a>
                        <a href="mailto:ariley@gmail.com" class="flex items-center gap-2 bg-white/10 hover:bg-white/20 px-4 py-2 rounded-lg backdrop-blur-sm transition">
                            ✉️ ariley@gmail.com
                        </a>
                        <a href="https://linkedin.com/in/agnesriley" target="_blank" class="flex items-center gap-2 bg-white/10 hover:bg-white/20 px-4 py-2 rounded-lg backdrop-blur-sm transition">
                            🔗 LinkedIn
                        </a>
                        <a href="https://www.credly.com/users/agnes-riley" target="_blank" class="flex items-center gap-2 bg-white/10 hover:bg-white/20 px-4 py-2 rounded-lg backdrop-blur-sm transition">
                            🏆 Credly
                        </a>
                        <span class="flex items-center gap-2 bg-white/10 px-4 py-2 rounded-lg backdrop-blur-sm">
                            📍 Sacramento, CA
                        </span>
                    </div>
                </div>
            </div>
            
            <div class="px-8 py-6 bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-100">
                <p class="text-gray-700 text-lg leading-relaxed">
                    <span class="text-3xl text-blue-600 font-bold">20+</span> years of IT and process management experience. 
                    Change agent and problem solver with a passion for technology.
                </p>
            </div>
        </div>

        <!-- Skills Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
            <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transform hover:-translate-y-1 transition-all duration-300 border-t-4 border-blue-500">
                <h3 class="font-bold text-gray-800 text-lg mb-2 flex items-center gap-2">
                    <span class="text-2xl">💼</span> Core Competencies
                </h3>
                <p class="text-sm text-gray-600">Business analysis, Project management, Process and standards definition, Software Engineering</p>
            </div>
            
            <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transform hover:-translate-y-1 transition-all duration-300 border-t-4 border-green-500">
                <h3 class="font-bold text-gray-800 text-lg mb-2 flex items-center gap-2">
                    <span class="text-2xl">💻</span> Development
                </h3>
                <p class="text-sm text-gray-600">FileMaker, HTML, CSS, JavaScript, SQL, Git, CI/CD, NextJS, AstroJS, TailwindCSS</p>
            </div>
            
            <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transform hover:-translate-y-1 transition-all duration-300 border-t-4 border-purple-500">
                <h3 class="font-bold text-gray-800 text-lg mb-2 flex items-center gap-2">
                    <span class="text-2xl">🖥️</span> Infrastructure
                </h3>
                <p class="text-sm text-gray-600">Servers (Mac, Linux, Windows), Networking, Firewalls, Google Cloud, AWS</p>
            </div>
            
            <div class="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transform hover:-translate-y-1 transition-all duration-300 border-t-4 border-orange-500">
                <h3 class="font-bold text-gray-800 text-lg mb-2 flex items-center gap-2">
                    <span class="text-2xl">🛠️</span> Tools
                </h3>
                <p class="text-sm text-gray-600">Adobe Suite, Photography, Video Editing, Project Management (Jira, Miro), Tableau</p>
            </div>
        </div>

        <!-- Tabs -->
        <div class="bg-white rounded-2xl shadow-lg overflow-hidden">
            <div class="flex border-b border-gray-200 bg-gray-50 overflow-x-auto">
                <button @click="activeTab = 'experience'" :class="activeTab === 'experience' ? 'text-white bg-blue-600 border-blue-600' : 'text-gray-600 hover:text-blue-600 hover:bg-white'" class="px-6 py-4 font-semibold transition border-b-2 border-transparent whitespace-nowrap">
                    💼 Experience
                </button>
                <button @click="activeTab = 'education'" :class="activeTab === 'education' ? 'text-white bg-blue-600 border-blue-600' : 'text-gray-600 hover:text-blue-600 hover:bg-white'" class="px-6 py-4 font-semibold transition border-b-2 border-transparent whitespace-nowrap">
                    🎓 Education
                </button>
                <button @click="activeTab = 'certifications'" :class="activeTab === 'certifications' ? 'text-white bg-blue-600 border-blue-600' : 'text-gray-600 hover:text-blue-600 hover:bg-white'" class="px-6 py-4 font-semibold transition border-b-2 border-transparent whitespace-nowrap">
                    🏆 Certifications
                </button>
            </div>

            <!-- Experience Tab -->
            <div x-show="activeTab === 'experience'" class="p-8">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <!-- Job cards will be inserted here -->
                    <div class="bg-gradient-to-br from-white to-blue-50 rounded-xl shadow-md hover:shadow-xl p-6 border-l-4 border-blue-500 transform hover:-translate-y-1 transition-all duration-300">
                        <div class="flex justify-between items-start mb-3">
                            <h3 class="font-bold text-lg text-gray-900">Sr. Product Manager (IC)</h3>
                            <span class="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded-full">2025</span>
                        </div>
                        <p class="text-blue-600 font-semibold text-sm mb-1">Claris, An Apple Company</p>
                        <p class="text-gray-600 text-xs mb-3">📍 Sunnyvale, CA | 📅 Jan 2025 – Oct 2025</p>
                        <ul class="text-xs text-gray-700 space-y-1">
                            <li class="flex gap-2"><span class="text-blue-500">▸</span><span>Lead product discovery and development for features enhancing security, user experience, and platform</span></li>
                            <li class="flex gap-2"><span class="text-blue-500">▸</span><span>Defined and prioritized product initiatives in collaboration with engineering, design, and cross-functional teams</span></li>
                        </ul>
                    </div>
                    <!-- More job cards... -->
                </div>
            </div>

            <!-- Education Tab -->
            <div x-show="activeTab === 'education'" class="p-8">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-lg transition">
                        <h3 class="font-bold text-gray-900">AWS Cloud Institute</h3>
                        <p class="text-sm text-blue-600">Cloud Computing</p>
                        <p class="text-xs text-gray-600 mt-1">Jan 2024 – present | Online</p>
                    </div>
                    <!-- More education cards... -->
                </div>
            </div>

            <!-- Certifications Tab -->
            <div x-show="activeTab === 'certifications'" class="p-8">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="flex items-center gap-3 bg-green-50 border border-green-200 rounded-lg p-4">
                        <span class="text-2xl">✓</span>
                        <span class="text-sm text-gray-700">AI For Everyone (Coursera) - 2024</span>
                    </div>
                    <!-- More certifications... -->
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="mt-6 text-center text-white text-sm">
            <p>© 2025 Agnes B. Riley | Generated with rendercv + Enhanced with TailwindCSS & Alpine.js</p>
        </div>
    </div>

</body>
</html>
'''

# Write the enhanced HTML
with open('index.html', 'w') as f:
    f.write(html_template)

print("✅ Created enhanced interactive CV with TailwindCSS, cards, tabs, and Alpine.js!")
print("📝 Note: This is a template. Full job data will be added next.")
