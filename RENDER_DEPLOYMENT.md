# 🚀 Podrobný návod: Nasazení na Render

**Render** (hosting) + **Neon** (PostgreSQL databáze) = plně zdarma, bez platební karty.

---

## Obsah

1. [Co budete potřebovat](#1-co-budete-potřebovat)
2. [Část A: Neon – vytvoření databáze](#2-část-a-neon--vytvoření-databáze)
3. [Část B: GitHub – nahrání projektu](#3-část-b-github--nahrání-projektu)
4. [Část C: Render – nasazení aplikace](#4-část-c-render--nasazení-aplikace)
5. [Po nasazení – první kroky](#5-po-nasazení--první-kroky)
6. [Řešení problémů](#6-řešení-problémů)
7. [Alternativní postup: Blueprint](#7-alternativní-postup-blueprint)

---

## 1. Co budete potřebovat

- **E-mail** pro registraci
- **Git** nainstalovaný na počítači (pro nahrání na GitHub)
- **5–10 minut** času

---

## 2. Část A: Neon – vytvoření databáze

Neon poskytuje zdarma PostgreSQL databázi. Data jsou persistentní a nikdy nevyprší.

### Krok A1: Registrace na Neon

1. Otevřete v prohlížeči: **https://neon.tech**
2. Klikněte na **Sign Up** (vpravo nahoře)
3. Zaregistrujte se pomocí:
   - e-mailu, nebo
   - GitHub účtu (doporučeno – rychlejší)
4. Po přihlášení se zobrazí dashboard Neon

### Krok A2: Vytvoření projektu

1. Na hlavní stránce klikněte na **New Project**
2. Vyplňte:
   - **Project name:** `odberos` (nebo libovolný název)
   - **Region:** vyberte nejbližší (např. **Frankfurt (eu-central-1)** pro ČR)
   - **PostgreSQL version:** ponechte výchozí (16)
3. Klikněte na **Create Project**

### Krok A3: Zkopírování connection stringu

1. Po vytvoření projektu se zobrazí přehled databáze
2. V sekci **Connection string** najděte řádek **URI**
3. Klikněte na ikonu **Copy** (vedle connection stringu)
4. Connection string vypadá přibližně takto:
   ```
   postgresql://neondb_owner:xxxxxxxx@ep-xxx-xxx.eu-central-1.aws.neon.tech/neondb?sslmode=require
   ```
5. **Uložte si ho** – budete ho potřebovat v Renderu (např. do textového souboru)
psql 'postgresql://neondb_owner:npg_KqdW6mNZiy0k@ep-shy-sunset-ag10ek47-pooler.c-2.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
> ⚠️ **Důležité:** Connection string obsahuje heslo. Nikdy ho nesdílejte a neukládejte do veřejného repozitáře.

---

## 3. Část B: GitHub – nahrání projektu

Render nasazuje aplikaci z GitHub repozitáře. Projekt musí být na GitHubu.

### Krok B1: Vytvoření repozitáře na GitHubu

1. Přihlaste se na **https://github.com**
2. Klikněte na **+** (vpravo nahoře) → **New repository**
3. Vyplňte:
   - **Repository name:** `odberos` (nebo jiný název)
   - **Visibility:** Private nebo Public (oba fungují)
   - **Nepřidávejte** README, .gitignore – projekt už existuje
4. Klikněte na **Create repository**

### Krok B2: Nahrání projektu do repozitáře

V terminálu (PowerShell nebo CMD) na vašem počítači:

```powershell
cd C:\Users\Thu\Downloads\odberos

# Inicializace Git (pokud ještě není)
git init

# Přidání všech souborů
git add .

# První commit
git commit -m "První verze - odběry a reklamace"

# Připojení k GitHubu (nahraďte YOUR_USERNAME a YOUR_REPO vaším uživatelským jménem a názvem repozitáře)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Nahrání na GitHub
git branch -M main
git push -u origin main
```

> Pokud Git ještě nemáte nainstalovaný, stáhněte ho z https://git-scm.com

---

## 4. Část C: Render – nasazení aplikace

### Krok C1: Registrace na Render

1. Otevřete **https://render.com**
2. Klikněte na **Get Started**
3. Zaregistrujte se pomocí **GitHub** (doporučeno – automatické propojení repozitářů)

### Krok C2: Vytvoření Web Service

1. Po přihlášení klikněte na **New +** (vpravo nahoře)
2. Vyberte **Web Service**
3. V seznamu repozitářů vyberte **odberos** (nebo název vašeho repozitáře)
4. Pokud repozitář nevidíte, klikněte na **Configure account** a povolte přístup k repozitáři

### Krok C3: Konfigurace služby

Vyplňte nebo zkontrolujte následující pole:

| Pole | Hodnota | Poznámka |
|------|---------|----------|
| **Name** | `odberos` | Název služby, bude v URL |
| **Region** | Frankfurt (EU Central) | Nejblíže ČR |
| **Branch** | `main` | Většinou main nebo master |
| **Root Directory** | `site` | **Důležité** – aplikace je v podsložce `site` |
| **Runtime** | Python 3 | Render detekuje automaticky |
| **Build Command** | `pip install -r requirements.txt` | Instalace závislostí |
| **Start Command** | `python run_waitress.py` | Spuštění aplikace |
| **Instance Type** | **Free** | Vyberte Free tier |

### Krok C4: Proměnné prostředí (Environment Variables)

1. Srolujte dolů k sekci **Environment Variables**
2. Klikněte na **Add Environment Variable**
3. Přidejte následující proměnné **jednu po druhé**:

| Key | Value |
|-----|-------|
| `DATABASE_URL` | Vložte celý connection string z Neon (z Kroku A3) |
| `SECRET_KEY` | Vygenerujte náhodný řetězec min. 32 znaků (např. [randomkeygen.com](https://randomkeygen.com)) |
| `FLASK_ENV` | `production` |

> **Tip pro SECRET_KEY:** Můžete vygenerovat např. v PowerShell:  
> `[Convert]::ToBase64String((1..32 | ForEach-Object { Get-Random -Maximum 256 }) -as [byte[]])`

### Krok C5: Vytvoření služby

1. Zkontrolujte, že máte vyplněné všechny položky
2. Klikněte na **Create Web Service**
3. Render začne buildovat a nasazovat aplikaci (trvá 2–5 minut)

### Krok C6: Sledování buildu

1. Na stránce služby uvidíte log z buildu
2. Počkejte, až se stav změní na **Live** (zelená)
3. URL aplikace bude např.: `https://odberos.onrender.com`

---

## 5. Po nasazení – první kroky

### První přihlášení

1. Otevřete URL vaší aplikace (např. `https://odberos.onrender.com`)
2. **První načtení** může trvat **30–60 sekund** – aplikace se probouzí ze spánku
3. Klikněte na **Přihlášení** (nebo Admin)
4. Přihlaste se s výchozími údaji:
   - **PIN:** `0000`
   - nebo **Uživatelské jméno:** `admin` + **Heslo:** `admin123`

### Bezpečnost – změna přihlašovacích údajů

1. Po přihlášení jděte do **Admin panelu**
2. Vyberte uživatele **admin**
3. Změňte **PIN** a **heslo** na vlastní hodnoty
4. Uložte změny

### Co dělat dál

- Přidejte pobočky v Admin → Pobočky
- Přidejte uživatele v Admin → Uživatelé
- Začněte používat odběry a reklamace

---

## 6. Řešení problémů

### Aplikace se nenačte / 502 Bad Gateway

- **Příčina:** Aplikace se ještě probouzí nebo build selhal
- **Řešení:** Počkejte 1–2 minuty a obnovte stránku. Free tier usíná po 15 min nečinnosti – první request pak trvá déle.

### Build failed (červená chyba)

1. Klikněte na **Logs** v Render dashboardu
2. Zkontrolujte chybovou hlášku
3. Časté příčiny:
   - **Špatný Root Directory** – musí být `site`
   - **Chybějící requirements.txt** – ověřte, že soubor existuje v `site/`
   - **Chybějící DATABASE_URL** – doplňte connection string z Neon

### Přihlášení nefunguje

- Ověřte, že používáte správné údaje: PIN `0000` nebo admin / admin123
- Zkuste jiný prohlížeč nebo anonymní okno (vyřadíte problém s cookies)

### Databáze nefunguje / chyby při ukládání

- Zkontrolujte, že `DATABASE_URL` je správně zkopíovaný z Neon (celý řetězec včetně hesla)
- V Neon dashboardu ověřte, že databáze běží (status Active)

### Jak zobrazit logy

1. V Render dashboardu otevřete vaši službu
2. Klikněte na **Logs** v levém menu
3. Zobrazí se živý výstup z aplikace

---

## 7. Alternativní postup: Blueprint

Pokud máte v repozitáři soubor `render.yaml` v kořeni projektu:

1. Na Render klikněte **New +** → **Blueprint**
2. Připojte repozitář **odberos**
3. Render načte konfiguraci z `render.yaml`
4. **Důležité:** V sekci **Environment** doplňte ručně:
   - `DATABASE_URL` – connection string z Neon
   - `SECRET_KEY` – vygenerujte vlastní
5. Klikněte na **Apply**

Blueprint vytvoří službu podle YAML. `SECRET_KEY` se může vygenerovat automaticky, ale `DATABASE_URL` je nutné doplnit vždy.

---

## Shrnutí – limity free tieru

| Služba | Limit |
|--------|-------|
| **Render** | 750 hodin/měsíc, usínání po 15 min |
| **Neon** | 0,5 GB úložiště, bez expirace |
| **První načtení** | 30–60 s (probouzení ze spánku) |

Pro malý tým a interní použití free tier obvykle stačí.

---

*Poslední aktualizace: únor 2025*
