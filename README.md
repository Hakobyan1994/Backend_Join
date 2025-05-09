# 🧩 Django REST API – Backend

Ein sauberes Django-Projekt mit Django REST Framework (DRF).  
Diese API stellt z. B. Benutzerverwaltung, Token-Authentifizierung und REST-Endpunkte bereit.

---

## 📦 Features

- Django REST Framework mit browsable API
- Token- oder JWT-Authentifizierung (je nach Bedarf)
- Unterstützung für `.env`-Dateien
- Strukturierte App-Ordner (mit Ignorierung von Migrations)
- Entwickelt für schnelle Weiterverwendung mit Frontends (Java Script)

---

## 🚀 Lokales Setup

### ✅ Voraussetzungen

- Python 3.10+
- pip
- Git
- Virtuelle Umgebung (`venv` empfohlen)

---

### ⚙️ Installationsanleitung

```bash
# 1. Projekt klonen
git https://github.com/Hakobyan1994/Join_Api_Django.git
cd dein-repo

# 2. Virtuelle Umgebung erstellen
python -m venv env

# 3. Umgebung aktivieren
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# 4. Abhängigkeiten installieren
pip install -r requirements.txt

# 5. .env Datei anlegen (siehe Abschnitt weiter unten)
copy .env.example .env    # Windows
# oder
cp .env.example .env      # macOS/Linux

# 6. Migrationen durchführen
python manage.py makemigrations
python manage.py migrate

# 7. Admin-Benutzer anlegen (optional)
python manage.py createsuperuser

# 8. Server starten
python manage.py runserver 