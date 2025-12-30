// CV Renderer - reads from cvData (loaded from data.js)
document.addEventListener('alpine:init', () => {
    Alpine.data('cvApp', () => ({
        activeTab: 'experience',
        data: cvData,
        
        getYear(date) {
            if (!date) return '';
            return String(date).split('-')[0];
        },
        
        skillStyles: [
            { icon: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z', color: 'fuchsia' },
            { icon: 'M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4', color: 'violet' },
            { icon: 'M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2', color: 'emerald' },
            { icon: 'M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z', color: 'amber' }
        ]
    }));
});
