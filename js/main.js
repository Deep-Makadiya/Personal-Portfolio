/* =========================================================
   Deep Makadiya — Personal Portfolio
   Interactions, animations, and form handling
   ========================================================= */

(() => {
    'use strict';

    /* -------- Loader -------- */
    const loader = document.getElementById('loader');
    window.addEventListener('load', () => {
        setTimeout(() => loader && loader.classList.add('hidden'), 600);
    });

    /* -------- AOS init -------- */
    if (window.AOS) {
        AOS.init({
            duration: 900,
            easing: 'ease-out-cubic',
            once: true,
            offset: 80,
            disable: () => window.matchMedia('(prefers-reduced-motion: reduce)').matches
        });
    }

    /* -------- Year -------- */
    const yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    /* -------- Navbar scroll behaviour -------- */
    const navbar = document.getElementById('navbar');
    const scrollProgress = document.getElementById('scrollProgress');
    const backToTop = document.getElementById('backToTop');

    const onScroll = () => {
        const y = window.scrollY;
        if (navbar) navbar.classList.toggle('scrolled', y > 50);
        if (backToTop) backToTop.classList.toggle('visible', y > 500);
        if (scrollProgress) {
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            scrollProgress.style.width = `${Math.min(100, (y / docHeight) * 100)}%`;
        }
        updateActiveLink();
    };
    window.addEventListener('scroll', onScroll, { passive: true });

    /* -------- Mobile menu -------- */
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('open');
            document.body.style.overflow = navMenu.classList.contains('open') ? 'hidden' : '';
        });
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('open');
                document.body.style.overflow = '';
            });
        });
    }

    /* -------- Active link by section -------- */
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    function updateActiveLink() {
        let current = 'home';
        const offset = 140;
        sections.forEach(section => {
            const top = section.offsetTop - offset;
            if (window.scrollY >= top) current = section.id;
        });
        navLinks.forEach(link => {
            link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
        });
    }

    /* -------- Typed text effect -------- */
    const typedEl = document.getElementById('typedText');
    if (typedEl) {
        const phrases = [
            'Python Developer',
            'AI / ML Engineer',
            'GCP Cloud Engineer',
            'Odoo Developer',
            'RAG Specialist',
            'Full-Stack Builder'
        ];
        let pIndex = 0, cIndex = 0, deleting = false;
        const TYPE_SPEED = 80, DELETE_SPEED = 45, HOLD = 1600;

        const tick = () => {
            const phrase = phrases[pIndex];
            if (!deleting) {
                cIndex++;
                typedEl.textContent = phrase.slice(0, cIndex);
                if (cIndex === phrase.length) {
                    deleting = true;
                    setTimeout(tick, HOLD);
                    return;
                }
                setTimeout(tick, TYPE_SPEED);
            } else {
                cIndex--;
                typedEl.textContent = phrase.slice(0, cIndex);
                if (cIndex === 0) {
                    deleting = false;
                    pIndex = (pIndex + 1) % phrases.length;
                }
                setTimeout(tick, DELETE_SPEED);
            }
        };
        tick();
    }

    /* -------- Counter animation -------- */
    const counters = document.querySelectorAll('.stat-num');
    const animateCounter = el => {
        const target = parseInt(el.dataset.target, 10) || 0;
        const duration = 1800;
        const start = performance.now();
        const step = now => {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.floor(eased * target);
            if (progress < 1) requestAnimationFrame(step);
            else el.textContent = target;
        };
        requestAnimationFrame(step);
    };

    if ('IntersectionObserver' in window && counters.length) {
        const counterObserver = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateCounter(entry.target);
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.4 });
        counters.forEach(c => counterObserver.observe(c));
    } else {
        counters.forEach(animateCounter);
    }

    /* -------- Tilt effect on cards -------- */
    const tiltCards = document.querySelectorAll('.project-card, .stat-card, .skill-category');
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const rotX = ((y / rect.height) - 0.5) * -6;
            const rotY = ((x / rect.width) - 0.5) * 6;
            card.style.transform = `perspective(1000px) rotateX(${rotX}deg) rotateY(${rotY}deg) translateY(-6px)`;
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
        });
    });

    /* -------- Smooth anchor scroll fallback -------- */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', e => {
            const targetId = anchor.getAttribute('href');
            if (targetId === '#' || targetId.length < 2) return;
            const target = document.querySelector(targetId);
            if (!target) return;
            e.preventDefault();
            const offset = 70;
            window.scrollTo({
                top: target.offsetTop - offset,
                behavior: 'smooth'
            });
        });
    });

    /* Initialize on load */
    onScroll();
})();
