# Deep Makadiya — Personal Portfolio

A world-class, modern, and animated personal portfolio for **Deep Makadiya** — Python Developer & AI Engineer. Built to be share-worthy on LinkedIn, GitHub, resumes, and any professional channel.

> "Crafting code, ideas and impact — one commit at a time."

## Highlights

- Premium dark UI with cyan / purple / pink gradient accents
- Animated hero with typing effect, floating tech icons and code preview
- Glassmorphism cards, smooth scroll, scroll progress, custom cursor
- Sticky pill-style navigation with active section highlighting
- Animated number counters, AOS reveal animations, 3D tilt cards
- Fully responsive (mobile / tablet / desktop)
- SEO-friendly meta tags + Open Graph
- Zero build step — pure HTML / CSS / JavaScript
- Production-ready and deployment-friendly

## Sections

1. **Hero** — Name, role, animated typing, CTA buttons, social links, code snippet card
2. **About** — Bio, info cards, animated stat counters
3. **Skills** — 6 categorized skill stacks (Python, AI, Cloud, DBs, Odoo, Tools)
4. **Experience** — Vertical timeline with bullet-point achievements
5. **Projects** — 5 featured projects + collaborate CTA
6. **Education** — Degree card
7. **Contact** — Info cards + working contact form (mailto integration)
8. **Footer** — Brand, socials, copyright

## Project Structure

```
Personal portfolio/
├── index.html         # Full markup with all sections
├── css/
│   └── style.css      # Design system, animations, responsive layout
├── js/
│   └── main.js        # Interactions, typing, counters, cursor, form
├── assets/            # Optional: place images / docs / resume PDF here
└── README.md
```

## Quick Start

The portfolio is **100% static** — no install or build step required.

### Option 1 — Open directly

Double-click `index.html` to open it in your browser.

### Option 2 — Local server (recommended)

```bash
# Python 3
python -m http.server 8080

# or Node
npx serve .
```

Then visit `http://localhost:8080`.

## Deployment

Deploy in seconds on any static host.

- **GitHub Pages** — push to a public repo and enable Pages on the `main` branch.
- **Netlify** — drag the folder into [app.netlify.com/drop](https://app.netlify.com/drop).
- **Vercel** — `npx vercel` from the project folder.
- **Cloudflare Pages** — connect the repo and deploy.

After deployment, share the live URL on:

- LinkedIn → *Profile → Contact info → Website*
- LinkedIn → *Featured section* (with screenshot preview)
- Resume header / signature
- GitHub profile bio
- Email signature

## Customization

All key personal data lives in `index.html`. Open the file and update:

| Item | Where |
|------|-------|
| Name, headline, bio | `<section id="home">` and `<section id="about">` |
| Stats (years, projects) | `data-target="..."` on `.stat-num` elements |
| Skills | `<section id="skills">` skill tags |
| Experience | `<section id="experience">` timeline content |
| Projects | `<section id="projects">` cards + GitHub / live links |
| Contact details | `<section id="contact">` info cards + mailto in `js/main.js` |

### Theme colors

Edit the design tokens at the top of `css/style.css`:

```css
:root {
    --primary: #00d4ff;
    --primary-2: #7c3aed;
    --accent: #ec4899;
    --gradient: linear-gradient(135deg, #00d4ff 0%, #7c3aed 50%, #ec4899 100%);
}
```

### Adding a real photo

Replace the avatar initials block in `index.html`:

```html
<div class="avatar-inner">
    <img src="assets/your-photo.jpg" alt="Deep Makadiya" />
</div>
```

Add a small CSS rule:

```css
.avatar-inner img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }
```

### Adding a real resume PDF

Drop your PDF into `assets/` (e.g. `assets/Deep-Makadiya-Resume.pdf`) and update the
`Download Resume` link in the About section:

```html
<a href="assets/Deep-Makadiya-Resume.pdf" download class="btn btn-primary">
    <i class="fa-solid fa-download"></i> Download Resume
</a>
```

## Tech Used

- HTML5 / CSS3 / Vanilla JavaScript (ES6+)
- [AOS](https://michalsnik.github.io/aos/) — scroll reveal animations
- [Font Awesome 6](https://fontawesome.com/) — icons
- [Google Fonts](https://fonts.google.com/) — Plus Jakarta Sans, Space Grotesk, JetBrains Mono

## Browser Support

Optimized for all modern evergreen browsers (Chrome, Edge, Firefox, Safari, Opera) on desktop and mobile. Gracefully degrades on reduced-motion devices.

## License

Personal use — feel free to fork, customize, and make it your own.

---

Designed & built with care for **Deep Makadiya** — Ahmedabad, India.
