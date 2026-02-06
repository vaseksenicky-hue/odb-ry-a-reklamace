# 🚀 Aplikace je připravena na nasazení!

## ✅ Kontrola dokončena

Aplikace prošla kontrolou a je **připravena na nasazení na PythonAnywhere**.

### Co bylo zkontrolováno:

1. ✅ **Konfigurace** - používá environment variables (bezpečné)
2. ✅ **Debug mode** - vypnutý (`debug=False`)
3. ✅ **Bezpečnost** - hashování hesel, role-based access, CSRF ochrana
4. ✅ **Error handling** - všechny kritické routes mají try-except
5. ✅ **Databáze** - automatické migrace a inicializace
6. ✅ **Závislosti** - kompletní `requirements.txt`
7. ✅ **Kód** - žádné syntax chyby, žádné linter chyby

### Vytvořené soubory:

- ✅ `wsgi.py` - WSGI konfigurace pro PythonAnywhere
- ✅ `DEPLOYMENT.md` - detailní návod pro nasazení
- ✅ `CHECKLIST.md` - kontrolní seznam

## ⚠️ DŮLEŽITÉ před nasazením:

### 1. Změňte SECRET_KEY!
Defaultní hodnota `'your-secret-key'` je **NEBEZPEČNÁ** pro produkci!

**Jak vytvořit bezpečný klíč:**
```python
import secrets
print(secrets.token_hex(32))
```

Nastavte ho jako environment variable na PythonAnywhere:
- Dashboard → Web → Environment variables
- `SECRET_KEY` = `váš-vygenerovaný-klíč`

### 2. Změňte defaultní admin údaje!
Po prvním přihlášení změňte:
- Default PIN: `0000` → změňte na bezpečný PIN
- Default password: `admin123` → změňte na silné heslo

### 3. Upravte cestu v wsgi.py
V souboru `wsgi.py` změňte:
```python
path = '/home/yourusername/odberos/site'  # ZMĚŇTE!
```
na vaši skutečnou cestu na PythonAnywhere.

## 📋 Rychlý start:

1. **Nahrajte soubory** na PythonAnywhere
2. **Nainstalujte závislosti:**
   ```bash
   pip3.10 install --user -r requirements.txt
   ```
3. **Nastavte WSGI** (použijte připravený `wsgi.py` nebo upravte v dashboardu)
4. **Nastavte SECRET_KEY** jako environment variable
5. **Reload aplikace** v dashboardu

## 📖 Detailní návod:

Viz `DEPLOYMENT.md` pro kompletní postup nasazení.

---

**Status: ✅ READY FOR DEPLOYMENT**
