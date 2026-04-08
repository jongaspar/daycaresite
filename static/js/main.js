// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function () {
    const menuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Hero slider
    initHeroSlider();

    // Gallery filters
    initGalleryFilters();

    // Active nav highlighting
    highlightActiveNav();
});

// ── Hero Slider ──
function initHeroSlider() {
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.slider-dot');
    if (slides.length <= 1) return;

    let current = 0;
    const total = slides.length;

    function showSlide(index) {
        slides.forEach(function (s, i) {
            s.style.opacity = i === index ? '1' : '0';
        });
        dots.forEach(function (d, i) {
            if (i === index) {
                d.classList.add('bg-white', 'scale-110');
                d.classList.remove('bg-white/50');
            } else {
                d.classList.remove('bg-white', 'scale-110');
                d.classList.add('bg-white/50');
            }
        });
        current = index;
    }

    // Auto-advance every 5 seconds
    setInterval(function () {
        showSlide((current + 1) % total);
    }, 5000);

    // Dot click navigation
    dots.forEach(function (dot) {
        dot.addEventListener('click', function () {
            showSlide(parseInt(this.dataset.index));
        });
    });
}

// ── Gallery Filters ──
function initGalleryFilters() {
    const filterBtns = document.querySelectorAll('.gallery-filter');
    const items = document.querySelectorAll('.gallery-item');
    if (filterBtns.length === 0) return;

    filterBtns.forEach(function (btn) {
        btn.addEventListener('click', function () {
            var filter = this.dataset.filter;

            // Update button styles
            filterBtns.forEach(function (b) {
                b.classList.remove('bg-garden-600', 'text-white');
                b.classList.add('bg-white', 'text-gray-700');
            });
            this.classList.add('bg-garden-600', 'text-white');
            this.classList.remove('bg-white', 'text-gray-700');

            // Filter items
            items.forEach(function (item) {
                if (filter === 'all' || item.dataset.category === filter) {
                    item.classList.remove('hidden-item');
                } else {
                    item.classList.add('hidden-item');
                }
            });
        });
    });
}

// ── Lightbox ──
function openLightbox(src, caption) {
    var lightbox = document.getElementById('lightbox');
    var img = document.getElementById('lightbox-img');
    var cap = document.getElementById('lightbox-caption');
    img.src = src;
    cap.textContent = caption || '';
    lightbox.classList.remove('hidden');
    lightbox.classList.add('flex');
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    var lightbox = document.getElementById('lightbox');
    lightbox.classList.add('hidden');
    lightbox.classList.remove('flex');
    document.body.style.overflow = '';
}

// Close on Escape
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeLightbox();
});

// ── FAQ Toggle ──
function toggleFaq(btn) {
    var answer = btn.nextElementSibling;
    var arrow = btn.querySelector('.faq-arrow');
    answer.classList.toggle('hidden');
    arrow.classList.toggle('rotate');
}

// ── Active Nav ──
function highlightActiveNav() {
    var path = window.location.pathname;
    var links = document.querySelectorAll('.nav-link');
    links.forEach(function (link) {
        var href = link.getAttribute('href');
        if (href === path || (path === '/' && href === '/')) {
            link.classList.add('active');
        }
    });
}
