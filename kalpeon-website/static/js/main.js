/* ========================================
   Kalpeon Group Website - JavaScript
   Main functionality and interactions
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {
    initializeNavigation();
    initializeInteractions();
    initializeScrollEffects();
});

// ==================== NAVIGATION ====================

function initializeNavigation() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    // Mobile Menu Toggle
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
        });

        // Close menu when link is clicked
        const navLinks = navMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                navToggle.classList.remove('active');
            });
        });
    }

    // Dropdown menu for mobile
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        const link = dropdown.querySelector('.nav-link');
        if (link) {
            link.addEventListener('click', function(e) {
                if (window.innerWidth <= 768) {
                    e.preventDefault();
                    dropdown.classList.toggle('active');
                }
            });
        }
    });

    // Active link highlight
    highlightActiveLink();
}

function highlightActiveLink() {
    const currentLocation = location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.style.color = '#f39c12';
        }
    });
}

// ==================== INTERACTIONS ====================

function initializeInteractions() {
    // Contact Form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', handleContactForm);
    }

    // FAQ Toggle
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', toggleFAQ);
    });

    // Gallery Filter
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', filterGallery);
    });

    // Apply Button in Careers
    const applyBtns = document.querySelectorAll('.apply-btn');
    applyBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
        });
    });

    // Newsletter Form
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', handleNewsletter);
    }
}

// ==================== CONTACT FORM ====================

function handleContactForm(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const messageDiv = document.getElementById('formMessage');

    // Show loading state
    const submitBtn = this.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;

    fetch('/contact', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        messageDiv.style.display = 'block';
        if (data.success) {
            messageDiv.className = 'form-message success';
            messageDiv.textContent = data.message;
            this.reset();
            submitBtn.textContent = 'Message Sent ✓';
            setTimeout(() => {
                messageDiv.style.display = 'none';
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }, 3000);
        } else {
            messageDiv.className = 'form-message error';
            messageDiv.textContent = data.error || 'An error occurred';
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    })
    .catch(error => {
        messageDiv.style.display = 'block';
        messageDiv.className = 'form-message error';
        messageDiv.textContent = 'Error: ' + error.message;
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    });
}

// ==================== FAQ TOGGLE ====================

function toggleFAQ(e) {
    const faqItem = this.parentElement;
    const isActive = faqItem.classList.contains('active');

    // Close other open items
    document.querySelectorAll('.faq-item.active').forEach(item => {
        if (item !== faqItem) {
            item.classList.remove('active');
        }
    });

    // Toggle current item
    faqItem.classList.toggle('active');
}

// ==================== GALLERY FILTER ====================

function filterGallery(e) {
    const filter = e.target.getAttribute('data-filter');
    const galleryItems = document.querySelectorAll('.gallery-item');

    // Update active button
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    e.target.classList.add('active');

    // Filter items
    galleryItems.forEach(item => {
        if (filter === 'all' || item.getAttribute('data-category') === filter) {
            item.style.display = 'block';
            setTimeout(() => {
                item.style.opacity = '1';
            }, 10);
        } else {
            item.style.display = 'none';
        }
    });
}

// ==================== NEWSLETTER ====================

function handleNewsletter(e) {
    e.preventDefault();

    const email = this.querySelector('input[type="email"]').value;

    fetch('/api/newsletter', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'email=' + encodeURIComponent(email)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        this.reset();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error subscribing to newsletter');
    });
}

// ==================== SCROLL EFFECTS ====================

function initializeScrollEffects() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Fade in on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe cards and sections
    document.querySelectorAll('.feature-card, .industry-item, .service-card, .team-card, .news-card, .job-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.6s ease';
        observer.observe(el);
    });
}

// ==================== UTILITY FUNCTIONS ====================

/**
 * Format date to readable format
 */
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}

/**
 * Validate email address
 */
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

/**
 * Show notification
 */
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 2rem;
        background-color: ${type === 'success' ? '#28a745' : '#dc3545'};
        color: white;
        border-radius: 5px;
        z-index: 5000;
        animation: slideIn 0.3s ease;
    `;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/**
 * Debounce function for performance
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ==================== EVENT LISTENERS ====================

// Handle window resize
window.addEventListener('resize', debounce(function() {
    // Close mobile menu on resize
    const navMenu = document.getElementById('navMenu');
    const navToggle = document.getElementById('navToggle');
    if (window.innerWidth > 768) {
        navMenu.classList.remove('active');
        navToggle.classList.remove('active');
    }
}, 250));

// Handle scroll
let scrollPos = 0;
window.addEventListener('scroll', debounce(function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.1)';
    } else {
        navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
    }
}, 100));

// ==================== ANIMATIONS ====================

const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);

// ==================== INITIALIZATION ====================

console.log('Kalpeon Website - All systems initialized');
