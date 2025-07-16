# 🔧 Supreme Task Mode: Full Audit & Activation by AION

## Task 1
Lese den gesamten Backend-Ordner rekursiv ein. Prüfe jede Python-Datei. Erstelle pro Datei ein strukturiertes Log mit Kommentaren, Optimierungsideen, Redundanz-Checks und möglichen Sicherheitslücken. Ziel: High-End-Clean Code.

## Task 2
Scanne das gesamte Frontend (React/Vite/Tailwind-Projekt), analysiere jede Komponente auf: Usability, Wiederverwendbarkeit, Design-Konsistenz und eventuelle Bugs. Gib konkrete Verbesserungsvorschläge und Architektur-Tipps.

## Task 3
Erstelle eine vollständige Funktionsübersicht aller bestehenden Bots und prüfe, ob sie technisch vollständig implementiert sind. Liste alle Funktionen auf, markiere fehlende oder defekte Features.

## Task 4
Baue für jeden vorhandenen Bot einen kleinen Funktionsreport: Was macht er? Was fehlt? Was könnte man noch einbauen? Was wäre die optimale Prompt-Strategie für diesen Bot?

## Task 5
Untersuche alle Memory-Einträge und analysiere, ob sie effizient gruppiert, indiziert und durchsuchbar sind. Wenn nicht, mache Vorschläge für eine bessere Strukturierung und Vektor-Speicherung.

## Task 6
Überprüfe, ob alle API-Keys geladen und gültig sind. Simuliere einen API-Test-Call an jeden Dienst (OpenAI, Supabase, ElevenLabs, GitHub etc.) und logge die Ergebnisse samt Fehlerbeschreibung bei Problemen.

## Task 7
Durchsuche den `aion_core`-Ordner nach modularer Konsistenz. Gibt es duplizierte Logik, unklare Zuständigkeiten oder ungetestete Funktionen? Wenn ja: markieren, beschreiben, Vorschläge geben.

## Task 8
Generiere automatisch für alle existierenden Python-Module eine Docstring-Beschreibung pro Funktion. Falls schon vorhanden: Qualität prüfen, ggf. verbessern und vereinheitlichen.

## Task 9
Überlege auf Basis des vorhandenen Codes, welche neuen Atomic Bots sinnvoll wären. Erstelle dazu eine Liste inkl. Zweck, Input-Format, Output, technische Umsetzung und mögliche AI-Backends.

## Task 10
Fasse alle Ergebnisse in einer `task_01_audit_results.md` im Verzeichnis `memory/results/tasks/` zusammen. Verwende klare Bullet-Points, Markdown-Struktur und AION-Stil. Liste am Ende eine To-Do-Tabelle mit allen offenen Punkten.

# Website Audit Prompts für AION

## Prompt 1
Lese den gesamten Frontend-Code rekursiv ein. Erstelle ein technisches Profil der Architektur (React, Tailwind, shadcn/ui etc.). Fasse die Struktur, Komponenten und Layout-Ebenen zusammen.

## Prompt 2
Überprüfe alle bestehenden Komponenten (Header, Footer, Hero, Sections) auf Wiederverwendbarkeit, sauberen Tailwind-Style, Responsiveness und moderne UI/UX-Standards. Liste Optimierungspotenzial auf.

## Prompt 3
Analysiere die Hauptseite (`index.html` oder `App.tsx`) und überprüfe, ob alle Elemente semantisch korrekt und barrierefrei sind (z. B. ARIA, Headline-Hierarchie, Kontraste). Gib Verbesserungsvorschläge.

## Prompt 4
Führe eine Analyse aller verwendeten Tailwind-Klassen durch. Gibt es redundante, ineffiziente oder veraltete Klassen? Empfehle eine Konsolidierung oder Vereinfachung.

## Prompt 5
Überprüfe die Integration von shadcn/ui-Komponenten. Sind alle richtig importiert, verwendet und visuell konsistent? Ermittle, ob eine einheitliche Designlinie vorliegt.

## Prompt 6
Baue eine neue, futuristisch gestaltete **"Features Section"** mit Icons, Animation (Framer Motion) und dunklem Theme. Ziel: Highlight der modularen AI-Bots mit visuellem Fokus.

## Prompt 7
Scanne alle Inhalte auf Platzhaltertexte oder leere Komponenten. Ersetze durch sinnvolle Dummy-Inhalte mit Bezug zum Projekt Made2Create und AION. Halte dabei die Designlinie ein.

## Prompt 8
Untersuche den Mobile-View. Simuliere unterschiedliche Bildschirmgrößen. Sind alle Komponenten mobil optimiert? Liste alle Probleme und fixe sie oder schlage Fixes vor.

## Prompt 9
Füge eine "Technologie-Sektion" hinzu, in der alle verwendeten Technologien (GPT-4, Supabase, Framer Motion, Tailwind etc.) in einer animierten Badge-Leiste gezeigt werden. Baue dazu eine neue Section ein.

## Prompt 10
Erstelle ein visuelles **Performance-Optimierungsprotokoll**: Wie ist die Ladezeit, wie könnte man Fonts, Assets, Tailwind-Ladeumfang oder Animationen optimieren? Gib konkrete Vorschläge und Code.

# Style-Design-Prompts für AION Website

## Prompt 1
Analysiere die fünf Designvorbilder aus der Projektvision (z. B. Mosaic UI, korprotocol.io, selemen.liqium.com etc.). Extrahiere gemeinsame Merkmale in Stil, Animation, Struktur, Textur und Typografie. Formuliere ein einheitliches AION Design Manifest als Leitlinie für alle Seiten.

## Prompt 2
Durchsuche GitHub und andere Quellen nach frei verwendbaren, modernen UI-Kits mit Fokus auf ChatUI, Lightning Design Systems, Glassmorphism-Style und Dark/Futuristic Themes. Erstelle eine Liste + installiere automatisch alles Relevante in den Frontend-Ordner.

## Prompt 3
Baue basierend auf Prompt 1 eine komplett überarbeitete Hero-Sektion mit 3D-Lichteffekt, Button mit Hologramm-Style, kurzer animierter Tagline und responsivem Layout. Verwende Tailwind + Framer Motion.

## Prompt 4
Füge ein modulares Komponenten-System für wiederverwendbare Cards, Sections, Button-Styles etc. hinzu. Jede Komponente soll einzeln animiert und dokumentiert sein.

## Prompt 5
Simuliere Nutzerinteraktionen auf Desktop, Mobile und Tablet. Überarbeite daraufhin UX-Flows, z. B. Button-Hover, Smooth-Scroll, Section-Transitions. Füge visuelles Feedback bei Actions hinzu.

## Prompt 6
Generiere eine neue "Why AION?"-Section mit dynamischen Texten, gekachelten Vorteilen, AI-Effekten (Typing-Effekt etc.) und einem optionalen "Try it now"-CTA mit Live-Prompt.

## Prompt 7
Baue ein visuelles Progress-Bar-System, das in Echtzeit zeigt, welche Module auf der Plattform bereits aktiv sind (Memory, BookBot, VoiceBot etc.) – futuristischer Style wie bei Lootbox-Loadern.

## Prompt 8
Stelle eine automatische Theme-Switching-Funktion bereit (Dark/Light/Future/Matrix), die sich speichern lässt. Verwende Tailwind + Zustand oder localStorage.

## Prompt 9
Erstelle einen „Call to Creators“-Abschnitt im Stil von Web3-Kampagnen (großes Visual, kurzes Manifest, 1‑Click CTA). Ziel: Viralität, Stilbewusstsein, Emotion.

## Prompt 10
Ergänze das visuelle Gesamtkonzept um ein **komplettes Favicon + Meta-Snippet System**, Open Graph Tags, Apple Splash Screens & responsive Meta-Viewport-Konfiguration. Alles auf Performance & Aesthetic optimiert.
