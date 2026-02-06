# Changelog - Bezpečnostní vylepšení a nové funkce

## ✅ Dokončené úpravy

### 1. Reset databáze
- **Soubor**: `reset_db.py`
- **Funkce**: Vytvoření nové čisté databáze s defaultními daty
- **Použití**: `python reset_db.py`
- **Defaultní přihlašovací údaje**:
  - Username: `admin`
  - PIN: `0000`
  - Password: `admin123`

### 2. Bezpečnostní vylepšení

#### CSRF ochrana
- Zapnuta CSRF ochrana ve Flask-WTF (`WTF_CSRF_ENABLED = True`)
- Časový limit pro CSRF token: 1 hodina

#### Validace vstupů
- **Jména uživatelů**: Regex validace (2-100 znaků, pouze písmena a mezery)
- **Názvy poboček**: Regex validace (2-100 znaků, písmena, čísla, mezery, pomlčky, tečky)
- **PIN**: 4-10 číslic
- **Hesla**: Minimálně 6 znaků

#### Sanitizace
- Všechny vstupy jsou ořezány (`strip()`)
- Omezení délky vstupů (max 100 znaků)
- Kontrola existence záznamů před přiřazením

#### Kontroly unikátnosti
- PIN musí být unikátní
- Název pobočky musí být unikátní
- Username musí být unikátní

#### Error handling
- Try-except bloky kolem všech databázových operací
- Rollback při chybách
- Detailní logování chyb

### 3. Vylepšený admin dashboard

#### UI vylepšení
- Čitelnější karty s barevnými hlavičkami
- Lepší organizace formulářů
- Checkboxy místo multiple select pro pobočky
- Tlačítka "Vybrat vše" / "Zrušit vše" pro checkboxy

#### Funkce
- Editace názvů poboček přímo z dashboardu
- Zobrazení počtu uživatelů u každé pobočky
- Lepší zobrazení přiřazených poboček u uživatelů

### 4. Vylepšené přiřazování poboček

#### Checkboxy místo multiple select
- **Soubor**: `templates/admin_edit_user_checkboxes.html`
- **Výhody**:
  - Intuitivnější použití
  - Viditelné všechny pobočky najednou
  - Snadné vybrání/zrušení všech
  - Lepší UX na mobilních zařízeních

#### Funkce
- Automatické načtení aktuálně přiřazených poboček
- Validace existence poboček před přiřazením
- Logování změn přiřazení

### 5. Editace poboček

#### Funkce
- Editace názvu pobočky
- Kontrola unikátnosti názvu
- Validace vstupu
- Logování změn

## 📋 Instrukce pro použití

### Reset databáze
```bash
python reset_db.py
```
**VAROVÁNÍ**: Tato operace smaže všechna existující data!

### Editace uživatele
1. Přejděte na Admin Dashboard
2. Klikněte na "Editovat" u požadovaného uživatele
3. Vyberte pobočky pomocí checkboxů
4. Uložte změny

### Editace pobočky
1. Přejděte na Admin Dashboard
2. V sekci "Seznam poboček" klikněte na "Editovat"
3. Změňte název pobočky
4. Uložte změny

## 🔒 Bezpečnostní doporučení

1. **Změňte defaultní přihlašovací údaje** po prvním přihlášení
2. **Používejte silná hesla** (minimálně 8 znaků, kombinace písmen, číslic a symbolů)
3. **Pravidelně kontrolujte logy** pro podezřelou aktivitu
4. **Omezte přístup k admin dashboardu** pouze na důvěryhodné uživatele
5. **Zálohujte databázi** pravidelně

## 📝 Poznámky

- Všechny změny jsou logovány do tabulky `Akce`
- CSRF tokeny jsou automaticky generovány Flask-WTF
- Validace probíhá jak na straně klienta (formuláře), tak na straně serveru
