
# AION TASK SEQUENCE: Build Full Landingpage for Made2Create (ContentHub Preview)

## Ziel:
Erstelle die vollständige Landingpage für das Projekt „Made2Create“ im Ordner `website_aionprojekt`.  
Die Seite soll visuell modern, hoch technologisch, modular aufgebaut und stark animiert sein.

Verwende dafür:

- Tailwind CSS (Dark Mode + Neon Accents)
- Reusable React-Komponenten (Hero, Modules, UseCases, Footer)
- Einbindung aller Projektinhalte aus Memory (z. B. Hubs, Tokenisierung, AION, Creator-Plattform)
- Style-Vorgaben wie: große Headlines, lebendige Layouts, Hover/Scroll-Effekte, 3D- oder Glow-Feeling
- Optional: Framer Motion, 3D-SVGs oder animierte Placeholders für KI-Elemente

---

## ⬇ TASK 1 – Komponentenstruktur aufbauen

**Dateien erstellen:**

- `src/components/Hero.jsx`
- `src/components/Modules.jsx`
- `src/components/UseCases.jsx`
- `src/components/Footer.jsx`

Stil: moderne Struktur, modulare Imports, vorbereitet für Tailwind-Styling.  
→ Kein Dummy-Text: Nutze bereits bekannten Projektkontext!

Commit: `"Create component scaffolding for AION Landingpage"`

---

## ⬇ TASK 2 – Hero Section befüllen (Hero.jsx)

Erstelle ein zentriertes Hero-Layout mit:

- Headline: **„AION. The Creator Engine.“**
- Subline: **„From Thought to Reality“**
- Button: **„Enter the System“**
- Dark Background, Glow-Pulse, animierte Schrift
- Optionaler 3D-Platzhalter im Hintergrund (SVG / Lottie / Three.js vorbereitet)

Komponenten-File: `Hero.jsx`  
Commit: `"Add Hero Section content to AION Landingpage"`

---

## ⬇ TASK 3 – Hubs anzeigen (Modules.jsx)

Erstelle ein responsives Grid mit folgenden Modulen (aus dem Memory ziehen):

- ContentHub
- ResearchHub
- MarketingHub
- PlatformHub
- MemoryHub
- EconomyHub

Jede Karte enthält:
- Name
- 1-Satz-Beschreibung
- passendes Icon (ggf. Placeholder)
- animiertes Hover-Verhalten (z. B. Scale / Shadow)

Komponenten-File: `Modules.jsx`  
Commit: `"Add Creator Hubs section to AION Landingpage"`

---

## ⬇ TASK 4 – UseCases befüllen (UseCases.jsx)

Baue eine „Showcase“-Sektion mit vier Atomic Bots:

- BookBot (Text zu Buch)
- VoiceBot (Text zu Stimme)
- VideoBot (Promo aus Text)
- NFTBot (Bilder + Metadaten)

Layout: stylisches 2-Spalten-Grid, jeder Bot in einer Karte mit leuchtendem Rahmen, kurzer Erklärung & animiertem Hover.

Komponenten-File: `UseCases.jsx`  
Commit: `"Add UseCases (Atomic Bots) section"`

---

## ⬇ TASK 5 – Footer bauen (Footer.jsx)

Erstelle einen stilvollen Footer mit:

- Branding: **Made2Create © 2025**
- Hinweis: **"Powered by AION"**
- Tokenisierung-Teaser: **"Token Launch Coming Soon"**
- Stil: zentriert, grau, kleiner Text, evtl. subtile Animation

Komponenten-File: `Footer.jsx`  
Commit: `"Add Footer to Landingpage"`

---

## ⬇ TASK 6 – App.jsx finalisieren

Verknüpfe alle Komponenten in `src/App.jsx`. Verwende:

```jsx
<Hero />
<Modules />
<UseCases />
<Footer />


# AION TASK SEQUENCE: Build Full Landingpage for Made2Create (ContentHub Preview)

## Ziel:
Erstelle die vollständige Landingpage für das Projekt „Made2Create“ im Ordner `website_aionprojekt`.  
Die Seite soll visuell modern, hoch technologisch, modular aufgebaut und stark animiert sein.

Verwende dafür:

- Tailwind CSS (Dark Mode + Neon Accents)
- Reusable React-Komponenten (Hero, Modules, UseCases, Footer)
- Einbindung aller Projektinhalte aus Memory (z. B. Hubs, Tokenisierung, AION, Creator-Plattform)
- Style-Vorgaben wie: große Headlines, lebendige Layouts, Hover/Scroll-Effekte, 3D- oder Glow-Feeling
- Optional: Framer Motion, 3D-SVGs oder animierte Placeholders für KI-Elemente

---
