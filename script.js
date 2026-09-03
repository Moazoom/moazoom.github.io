// Animated counter for hero stats
document.addEventListener('DOMContentLoaded', () => {
    const stats = document.querySelectorAll('.stat-number');
    
    const animateStats = () => {
        stats.forEach(stat => {
            const target = parseInt(stat.dataset.target);
            const suffix = stat.nextElementSibling?.textContent || '';
            let current = 0;
            const increment = target / 60;
            
            const updateCounter = () => {
                current += increment;
                if (current < target) {
                    stat.textContent = Math.round(current);
                    requestAnimationFrame(updateCounter);
                } else {
                    stat.textContent = target;
                }
            };
            updateCounter();
        });
    };

    // Intersection Observer for stats
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) observer.observe(heroStats);

    // Animate bars on scroll
    const bars = document.querySelectorAll('.bar-fill');
    const barObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => {
                    bar.style.width = width;
                }, 100);
                barObserver.unobserve(bar);
            }
        });
    }, { threshold: 0.3 });

    bars.forEach(bar => barObserver.observe(bar));

    // CPU meter animation
    const cpuFills = document.querySelectorAll('.cpu-fill');
    cpuFills.forEach(fill => {
        const width = fill.style.width;
        fill.style.width = '0%';
        setTimeout(() => {
            fill.style.width = width;
        }, 500);
    });

    // Smooth scroll for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Terminal-like cursor blink for hero (optional)
    const heroH1 = document.querySelector('.hero h1');
    if (heroH1) {
        const cursor = document.createElement('span');
        cursor.textContent = '█';
        cursor.style.cssText = `
            display: inline-block;
            color: var(--accent-cyan);
            animation: blink 1s step-end infinite;
            font-weight: 300;
            margin-left: 2px;
        `;
        // Uncomment to add cursor
        // heroH1.appendChild(cursor);
    }
});

// Add blink keyframe dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
`;
document.head.appendChild(style);