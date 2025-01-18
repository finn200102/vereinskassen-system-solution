# Vereinskassen-System

## EPR WiSe 2024/2025 - Übungsblatt ÜE-08

Ein virtuelles Vereinskassen-System mit GUI basierend auf Tkinter, das die Verwaltung von Abteilungskonten und deren Transaktionen ermöglicht.

### Projektstruktur

```

vereinskassen_system/
│
├── src/ # Quellcode
│ ├── models/ # Datenmodelle
│ ├── views/ # GUI-Komponenten
│ ├── controllers/ # Geschäftslogik
│ └── utils/ # Hilfsfunktionen
│
├── data/ # Datenspeicherung
├── docs/ # Dokumentation
├── tests/ # Testfälle
├── main.py # Hauptprogramm
├── setup.py # Installation
└── README.md

```

### Installation

1. Python 3.1x oder höher wird benötigt
2. Repository klonen:

```bash
git clone https://github.com/finn200102/vereinskassen-system-solution.git
cd vereinskassen-system-solution
```

3. Virtuelle Umgebung erstellen und aktivieren:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

4. Installation der Abhängigkeiten:

```bash
pip install -e .
```

### Ausführung

```bash
python main.py
```

### Funktionalitäten

#### Benutzerrollen

- **Administrator**

  - Anlegen von Vereinskonten
  - Erstellen von Benutzern
  - Systemzustand speichern

- **Kassenwart**

  - Einzahlungen
  - Auszahlungen
  - Umbuchungen
  - Transaktionshistorie einsehen

- **Referentin-Finanzen**
  - Kontostände einsehen
  - Transaktionshistorie einsehen
  - Gesamtübersicht generieren

### Technische Details

- **Authentifizierung**: Benutzerauthentifizierung über Login-System
- **Datenpersistenz**: CSV-Dateien für Benutzer, Konten und Transaktionen
- **GUI**: Tkinter-basierte Benutzeroberfläche
- **Validierung**: Überziehungsschutz für Konten

### Tests

```bash
python tests/*.py
```

### Dokumentation

- Benutzerhandbuch: `docs/user_manual.pdf`
- Technische Dokumentation: `docs/technical_docs.pdf`
