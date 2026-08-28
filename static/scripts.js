document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector('header');
    const burgerMenu = document.querySelector('.burger-menu');
    const navbarList = document.querySelector('.navbar-list');
    const navLinksAll = document.querySelectorAll('.navbar-list li a');
    const smoothNavLinks = document.querySelectorAll('.navbar-list li a[href^="#"]');

    const scrollThreshold = 100;
    let lastScrollY = window.scrollY;
    let isScrollingUp = false;
    let ticking = false;

    const setActiveLink = (targetId) => {
        navLinksAll.forEach(link => {
            const linkHref = link.getAttribute('href').replace('#', '');
            if (linkHref === targetId) {
                link.classList.add('active-link');
            } else {
                link.classList.remove('active-link');
            }
        });
    };

    const updateScroll = () => {
        const currentScrollY = window.scrollY;

        if (currentScrollY > scrollThreshold) {
            header.classList.add('sticky');
        } else {
            header.classList.remove('sticky');
        }

        isScrollingUp = currentScrollY < lastScrollY;
        lastScrollY = currentScrollY;

        const isAtTop = currentScrollY < 80;
        const isAtBottom = (window.innerHeight + currentScrollY) >= document.documentElement.scrollHeight - 20;

        if (isAtTop) {
            setActiveLink('aboutMe');
            return;
        }

        if (isAtBottom) {
            setActiveLink('contact');
            return;
        }

        updateActiveSection();
    };

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                updateScroll();
                ticking = false;
            });
            ticking = true;
        }
    });

    const updateActiveSection = () => {
        const sections = document.querySelectorAll('main section[id], footer[id]');
        let closestSection = null;
        let minDistance = Infinity;
        const viewportCenter = window.innerHeight / 2;

        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 80) {
                const sectionCenter = rect.top + rect.height / 2;
                const distance = Math.abs(viewportCenter - sectionCenter);

                if (distance < minDistance) {
                    minDistance = distance;
                    closestSection = section;
                }
            }
        });

        if (closestSection) {
            setActiveLink(closestSection.getAttribute('id'));
        }
    };

    const centerObserverOptions = {
        root: null,
        rootMargin: "-25% 0px -25% 0px",
        threshold: 0
    };

    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                if (isScrollingUp) {
                    entry.target.classList.add('scroll-up');
                } else {
                    entry.target.classList.remove('scroll-up');
                }
                entry.target.classList.add('show');
            } else {
                entry.target.classList.remove('show');
                entry.target.classList.remove('scroll-up');
            }
        });
    }, centerObserverOptions);

    const sectionsToAnimate = [
        document.querySelector('.about'),
        document.querySelector('.education'),
        document.querySelector('.techstack'),
        document.querySelector('.projects'),
        document.querySelector('.page-footer')
    ];

    sectionsToAnimate.forEach(section => {
        if (section) scrollObserver.observe(section);
    });

    if (burgerMenu && navbarList) {
        burgerMenu.addEventListener('click', () => {
            burgerMenu.classList.toggle('active');
            navbarList.classList.toggle('active');
        });
    }

    smoothNavLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();

            if (burgerMenu && navbarList) {
                burgerMenu.classList.remove('active');
                navbarList.classList.remove('active');
            }

            const targetId = link.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            }
        });
    });

    updateScroll();
});