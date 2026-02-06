# 🚀 Připravenost na produkční nasazení

## ✅ Status: **PŘIPRAVENO S VAROVÁNÍMI**

Aplikace je **technicky připravena** na produkční nasazení, ale **vyžaduje konfiguraci** před spuštěním.

---

## ⚠️ KRITICKÉ - POVINNÉ PŘED NASAZENÍM

### 1. SECRET_KEY ⚠️ **MUSÍ BÝT ZMĚNĚN!**
- **Aktuální stav:** Aplikace má defaultní `SECRET_KEY = 'your-secret-key'`
- **Riziko:** Bezpečnostní riziko - session cookies a CSRF tokeny mohou být zranitelné
- **Řešení:** 
  ```bash
  # Vygenerujte silný náhodný klíč (min. 32 znaků):
  python -c "import secrets; print(secrets.token_urlsafe(32))"
  ```
  Nastavte jako environment variable na PythonAnywhere:
  - Dashboard → Web → Environment variables
  - `SECRET_KEY` = `váš-vygenerovaný-klíč`

### 2. Admin údaje ⚠️ **ZMĚŇTE PO PRVNÍM PŘIHLÁŠENÍ!**
- **Default:** username=`admin`, PIN=`0000`, password=`admin123`
- **Riziko:** Kdokoliv s těmito údaji má plný přístup
- **Řešení:** Po prvním přihlášení změňte PIN a heslo v admin dashboardu

---

## ✅ IMPLEMENTOVANÉ BEZPEČNOSTNÍ FUNKCE

### Autentizace a autorizace
- ✅ Hashování hesel (Werkzeug)
- ✅ PIN autentizace
- ✅ Role-based access control (admin/user)
- ✅ Branch-based access control
- ✅ Session protection (strong mode)
- ✅ Secure session cookies (HTTPS v produkci)
- ✅ HTTPOnly cookies (ochrana před XSS)
- ✅ SameSite cookies (CSRF ochrana)

### Ochrana před útoky
- ✅ CSRF ochrana (Flask-WTF)
- ✅ SQL injection ochrana (SQLAlchemy ORM)
- ✅ XSS ochrana (Jinja2 auto-escaping)
- ✅ Input validace (WTForms validators)
- ✅ Length validace (max délky polí)

### Error handling
- ✅ Error handlers pro 404, 403, 500
- ✅ Logging chyb
- ✅ Graceful error recovery
- ✅ Database rollback při chybách

### Monitoring
- ✅ Health check endpoint (`/health`)
- ✅ Logging do souboru (`logs/app.log`)
- ✅ Rotating log files (10MB, 10 backupů)

---

## 📋 CHECKLIST PŘED NASAZENÍM

### Konfigurace
- [ ] **KRITICKÉ:** Nastavit `SECRET_KEY` jako environment variable
- [ ] Nastavit `DATABASE_URL` (pokud chcete jinou než SQLite)
- [ ] Upravit cestu v `wsgi.py` na skutečnou cestu
- [ ] Nastavit `FLASK_ENV=production` (pro HTTPS cookies)

### Bezpečnost
- [ ] **KRITICKÉ:** Změnit defaultní admin PIN a heslo
- [ ] Zkontrolovat oprávnění uživatelů
- [ ] Zkontrolovat, že HTTPS je zapnuté (na PythonAnywhere automaticky)

### Databáze
- [ ] Zkontrolovat, že databáze má správná oprávnění
- [ ] Nastavit pravidelnou zálohu databáze
- [ ] Otestovat migrace databáze

### Testování
- [ ] Otestovat přihlášení
- [ ] Otestovat všechny hlavní funkce
- [ ] Otestovat exporty (CSV, Excel)
- [ ] Otestovat error handlery (zkuste neexistující URL)
- [ ] Otestovat health check (`/health`)

### Monitoring
- [ ] Zkontrolovat, že logy se zapisují (`logs/app.log`)
- [ ] Nastavit monitoring health check endpointu
- [ ] Zkontrolovat error logy v PythonAnywhere dashboardu

---

## 🔧 KONFIGURACE PRODUKCE

### Environment Variables (PythonAnywhere)
```bash
SECRET_KEY=váš-silný-náhodný-klíč-min-32-znaků
DATABASE_URL=sqlite:///odbery.db  # nebo jiná cesta
FLASK_ENV=production  # pro HTTPS cookies
```

### WSGI konfigurace
Upravte `wsgi.py`:
```python
path = '/home/vaše-username/odberos/site'  # ZMĚŇTE!
```

### Statické soubory
- URL: `/static/`
- Directory: `/home/vaše-username/odberos/site/static/`

---

## 📊 LIMITACE A DOPORUČENÍ

### SQLite databáze
- ✅ **OK pro:** Malé až střední aplikace (< 1000 uživatelů, < 100k záznamů)
- ⚠️ **Zvažte přechod na PostgreSQL/MySQL pro:**
  - Více souběžných uživatelů
  - Větší objem dat
  - Potřeba transakcí

### Performance
- ✅ Aplikace je optimalizovaná pro malé až střední použití
- ⚠️ Pro větší zátěž zvažte:
  - Caching (Redis)
  - Database connection pooling
  - CDN pro statické soubory

### Backup
- ⚠️ **DŮLEŽITÉ:** Nastavte pravidelnou zálohu databáze!
- SQLite databáze: `instance/odbery.db`
- Zálohujte minimálně denně

---

## 🐛 ZNÁMÉ PROBLÉMY / LIMITACE

1. **SQLite:** Není ideální pro vysokou zátěž, ale pro malou aplikaci OK
2. **Rate limiting:** Není implementován (zvažte pro veřejné API)
3. **Email notifikace:** Není implementováno
4. **Audit log:** Je implementován, ale není exportovatelný

---

## ✅ CO JE PŘIPRAVENO

### Funkcionalita
- ✅ Správa odběrů
- ✅ Správa reklamací
- ✅ Admin dashboard
- ✅ Statistiky
- ✅ Exporty (CSV, Excel)
- ✅ Multi-user support
- ✅ Multi-branch support

### Bezpečnost
- ✅ Všechny kritické endpointy mají autentizaci
- ✅ Validace oprávnění k pobočkám
- ✅ CSRF ochrana
- ✅ SQL injection ochrana
- ✅ Input validace

### Error handling
- ✅ Error handlers pro všechny běžné chyby
- ✅ Logging
- ✅ Graceful recovery

### Monitoring
- ✅ Health check endpoint
- ✅ Logging do souboru
- ✅ Error tracking

---

## 🎯 ZÁVĚR

**Aplikace je připravena na produkční nasazení**, ale:

1. **MUSÍTE** nastavit `SECRET_KEY` před spuštěním
2. **MUSÍTE** změnit defaultní admin údaje po prvním přihlášení
3. **DOPORUČUJI** nastavit pravidelnou zálohu databáze
4. **DOPORUČUJI** otestovat všechny funkce po nasazení

Po splnění těchto požadavků je aplikace **bezpečná a připravená** pro produkční použití! 🚀

---

**Poslední aktualizace:** {{ datum }}
**Verze:** 1.0
