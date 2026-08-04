# Footprint Quest - Modular Futuristic Django Architecture

Welcome to **Footprint Quest**, a modern, multi-app Django application centered around **Space + Digital Future + Education + Digital Footprint**.

This codebase is designed specifically for **beginner and intermediate Django developers** to learn clean, modular, production-ready Django project architecture.

---

## 📁 Project Architecture & Tree

```text
ICS-Hackathon/
│
├── manage.py                     # Django CLI command management script
├── README.md                     # Comprehensive architecture documentation
├── db.sqlite3                    # SQLite database engine
│
├── core/                         # Global Project Configuration
│   ├── settings.py               # Installed apps, middleware, static/template configs
│   ├── urls.py                   # Master root URL router including feature apps
│   ├── context_processors.py     # Global template variables (site metadata)
│   ├── wsgi.py                   # WSGI server entry point
│   └── asgi.py                   # Async ASGI entry point
│
├── static/                       # Single-Concern Static Assets
│   ├── css/
│   │   ├── base.css              # Variables, Reset, Typography, Custom Cursor
│   │   ├── navbar.css            # Glassmorphism Header & Mobile Menu
│   │   ├── hero.css              # Hero Grid & Cyber Avatar Styling
│   │   ├── buttons.css           # Neon Button System & Ripples
│   │   ├── cards.css             # Glass Cards, Badges & Risk Meters
│   │   ├── forms.css             # Form Controls, Labels & Inputs
│   │   ├── modals.css            # Glass Overlay Modal Windows
│   │   ├── space.css             # Space Canvas & Background Glow
│   │   ├── timeline.css          # Vertical Roadmap Timeline
│   │   ├── animations.css        # Keyframes (float, pulse, breath, scroll reveal)
│   │   └── responsive.css        # Breakpoint Media Queries
│   │
│   └── js/
│       ├── space-background.js   # Canvas 2D Space Particle Engine (Stars, Nebula, Meteors)
│       ├── eye-tracking.js       # SVG Cyber Avatar Pupil Tracking & Blinking Physics
│       ├── cursor.js             # Custom Cursor Lerp & Magnetic Hover
│       ├── navbar.js             # Scroll Blur Scaling, Reading Progress, Theme Toggle
│       ├── modals.js             # Login/Register Modal Handlers
│       ├── counter.js            # Animated Stats Counter
│       ├── tilt.js               # 3D Parallax Card Tilt
│       ├── carousel.js           # Testimonials Slider
│       ├── accordion.js          # FAQ Accordion
│       └── scroll.js             # Scroll Reveal & Back-to-Top Button
│
├── templates/                    # Modular Template Inheritance
│   ├── base.html                 # Master Base Template
│   ├── includes/                 # Reusable Partial Components
│   │   ├── _navbar.html
│   │   ├── _footer.html
│   │   ├── _modals.html
│   │   ├── _cursor.html
│   │   └── _canvas.html
│   │
│   ├── home/                     # Home App Landing Page
│   │   └── index.html
│   ├── accounts/                 # Auth & Profiles
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── digitalfootprints/        # Footprint Catalog
│   │   └── index.html
│   ├── journey/                  # Roadmap Timeline
│   │   └── index.html
│   ├── quiz/                     # Interactive Quizzes
│   │   ├── index.html
│   │   ├── detail.html
│   │   └── result.html
│   ├── leaderboard/              # Scoreboard Rankings
│   │   └── index.html
│   ├── dashboard/                # Student Dashboard
│   │   └── index.html
│   ├── stats_app/                # Analytics & Stats
│   │   └── index.html
│   ├── blog/                     # Educational Articles
│   │   ├── index.html
│   │   └── detail.html
│   └── contact/                  # Contact & FAQ
│       ├── index.html
│       └── faq.html
│
├── accounts/                     # User Auth & Profile Management
│   ├── models.py                 # Profile model extending User
│   ├── forms.py                  # UserRegisterForm & ProfileForm
│   ├── views.py                  # register_view, login_view, logout_view, profile_view
│   ├── urls.py                   # accounts routing
│   └── admin.py                  # Profile admin configuration
│
├── home/                         # Landing Page App
│   ├── views.py                  # home_view
│   └── urls.py
│
├── digitalfootprints/            # Footprint Knowledge System
│   ├── models.py                 # DigitalFootprintType model
│   ├── views.py                  # footprint_list_view
│   └── urls.py
│
├── journey/                      # Learning Roadmap Timeline
│   ├── models.py                 # JourneyStep model
│   ├── views.py                  # journey_view
│   └── urls.py
│
├── quiz/                         # Interactive Privacy Quizzes
│   ├── models.py                 # Quiz, Question, Choice, QuizAttempt models
│   ├── views.py                  # quiz_list_view, quiz_detail_view
│   └── urls.py
│
├── leaderboard/                  # Student Rankings & Achievements
│   ├── models.py                 # Badge, UserBadge models
│   ├── views.py                  # leaderboard_view
│   └── urls.py
│
├── dashboard/                    # Personalized Student Dashboard
│   ├── views.py                  # dashboard_view
│   └── urls.py
│
├── stats_app/                    # Live Platform Analytics & JSON API
│   ├── models.py                 # GlobalStatistic model
│   ├── views.py                  # statistics_view, stats_api_view
│   └── urls.py
│
├── blog/                         # Educational Articles & Guides
│   ├── models.py                 # Article, Category models
│   ├── views.py                  # article_list_view, article_detail_view
│   └── urls.py
│
└── contact/                      # Inquiries & FAQ Accordion
    ├── models.py                 # ContactMessage, FAQItem models
    ├── forms.py                  # ContactForm
    ├── views.py                  # contact_view, faq_view
    └── urls.py
```

---

## 🚀 How Django Works: Request-Response Lifecycle

1. **Browser Request**: User clicks a URL (e.g. `/quiz/`).
2. **Master Router (`core/urls.py`)**: Matching prefix routes request to app router `quiz/urls.py`.
3. **App Router (`quiz/urls.py`)**: Maps `/` to `views.quiz_list_view`.
4. **View (`quiz/views.py`)**: Runs Python logic, queries database using **Django ORM** (`Quiz.objects.all()`).
5. **Template Rendering (`templates/quiz/index.html`)**: Injects dynamic context dictionary into template.
6. **HTTP Response**: Formatted HTML is delivered to browser with CSS and JS static files.

---

## 🛠️ Key Beginner Commands

### 1. Run Development Server
```bash
python manage.py runserver 8085
```

### 2. Make Database Migrations
Run whenever you create or edit a `models.py` file:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Check Project Integrity
```bash
python manage.py check
```

### 4. Create Admin Superuser
```bash
python manage.py createsuperuser
```

---

## 💡 How to Extend the Project

### Adding a New View
1. Open the relevant app's `views.py` (e.g. `quiz/views.py`).
2. Define a python view function or Class-Based View returning `render(request, 'template_name.html', context)`.
3. Add a corresponding `path(...)` entry in the app's `urls.py`.

### Adding a New Model
1. Open the app's `models.py`.
2. Define a class inheriting from `models.Model`.
3. Register the model in `admin.py` using `@admin.register(MyModel)`.
4. Run `python manage.py makemigrations` and `python manage.py migrate`.

---

## 🎓 Design Principles & Clean Code
- **Separation of Concerns**: Each app handles exactly one domain (e.g. `accounts` only does auth, `quiz` only handles questions).
- **Template Inheritance**: Master layout lives in `base.html`, partial UI blocks in `templates/includes/`.
- **Modular Assets**: CSS and JS files are partitioned into focused, single-purpose scripts rather than one monolithic file.
