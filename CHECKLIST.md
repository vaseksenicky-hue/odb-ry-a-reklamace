# ✅ Kontrolní seznam před nasazením

## 🔍 Kontrola kódu

### Konfigurace
- [x] `SECRET_KEY` používá `os.environ.get()` - ✅ OK
- [x] `DATABASE_URL` používá `os.environ.get()` - ✅ OK
- [x] `debug=False` v produkčním kódu - ✅ OK
- [x] Žádné hardcoded cesty k souborům - ✅ OK
- [x] Žádné localhost/127.0.0.1 odkazy - ✅ OK

### Bezpečnost
- [x] Hesla jsou hashovaná (Werkzeug) - ✅ OK
- [x] PIN autentizace implementována - ✅ OK
- [x] Role-based access control - ✅ OK
- [x] Branch-based access control - ✅ OK
- [x] SQL injection ochrana (SQLAlchemy ORM) - ✅ OK
- [x] CSRF ochrana (Flask-WTF) - ✅ OK

### Error handling
- [x] Try-except bloky v kritických routes - ✅ OK
- [x] Logging chyb - ✅ OK
- [x] Graceful fallback pro volitelné funkce (Excel) - ✅ OK

### Databáze
- [x] Automatické migrace (`migrate_db()`) - ✅ OK
- [x] Automatická inicializace (`init_db()`) - ✅ OK
- [x] Zpětná kompatibilita s existujícími daty - ✅ OK

### Závislosti
- [x] `requirements.txt` kompletní - ✅ OK
- [x] Všechny importy mají fallback - ✅ OK
- [x] Žádné konfliktní verze - ✅ OK

## 📦 Soubory k nahrání

- [x] `app.py` - hlavní aplikace
- [x] `wsgi.py` - WSGI konfigurace (vytvořeno)
- [x] `requirements.txt` - závislosti
- [x] `templates/` - všechny HTML šablony
- [x] `static/` - statické soubory (pokud existují)
- [x] `DEPLOYMENT.md` - návod (vytvořeno)

## ⚠️ Co je potřeba udělat na PythonAnywhere

1. **Nastavit SECRET_KEY** jako environment variable
   - Vytvořte silný náhodný klíč (min. 32 znaků)
   - Nastavte v PythonAnywhere dashboardu → Web → Environment variables

2. **Upravit cestu v wsgi.py**
   - Změňte `/home/yourusername/odberos/site` na vaši skutečnou cestu

3. **Nainstalovat závislosti**
   ```bash
   pip3.10 install --user -r requirements.txt
   ```

4. **Nastavit statické soubory** (pokud máte)
   - URL: `/static/`
   - Directory: `/home/yourusername/odberos/site/static/`

5. **Změnit defaultní admin údaje** po prvním přihlášení
   - Default: username=`admin`, PIN=`0000`, password=`admin123`

## 🎯 Status: READY FOR DEPLOYMENT ✅

Aplikace je připravena na nasazení na PythonAnywhere!
