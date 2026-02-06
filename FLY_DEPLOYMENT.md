# 🚀 Nasazení na Fly.io

## Požadavky

- Účet na [fly.io](https://fly.io)
- Nainstalované [Fly CLI](https://fly.io/docs/hands-on/install-flyctl/)

## Rychlý start

```bash
# 1. Přihlášení
fly auth login

# 2. První spuštění – vytvoří app a vybere region (např. fra = Frankfurt)
cd /cesta/k/odberos
fly launch --no-deploy
# Vyberte region (doporučeno: fra, ams, cdg pro Evropu)

# 3. Vytvoření volume (DŮLEŽITÉ – bez toho by se SQLite data ztratila při restartu)
fly volumes create odberos_data -r fra -s 1
# Použijte stejný region jako v kroku 2!

# 4. Nastavení SECRET_KEY (povinné pro produkci!)
fly secrets set SECRET_KEY="váš-náhodný-klíč-min-32-znaků"

# 5. Deploy
fly deploy
```

## Po deployi

- URL: `https://odberos.fly.dev` (nebo název vaší app)
- Defaultní admin: `admin` / PIN `0000` / heslo `admin123`
- **Změňte heslo a PIN ihned po prvním přihlášení!**

## Příkazy

| Příkaz | Popis |
|-------|------|
| `fly deploy` | Nasazení nové verze |
| `fly logs` | Zobrazení logů |
| `fly ssh console` | SSH do kontejneru |
| `fly secrets list` | Seznam nastavených secrets |
| `fly status` | Stav aplikace |

## Proměnné prostředí

| Proměnná | Popis | Výchozí |
|----------|-------|---------|
| `SECRET_KEY` | Tajný klíč pro session (nastavte přes `fly secrets set`) | — |
| `DATABASE_URL` | Cesta k SQLite (nastaveno v fly.toml na volume) | `sqlite:////data/odbery.db` |
| `FLASK_ENV` | `production` pro HTTPS cookies | `production` |

## Záloha databáze

```bash
# Stáhnout SQLite soubor z volume
fly ssh console -C "cat /data/odbery.db" > záloha_odbery.db
```

Nebo použijte `fly ssh sftp` pro přímý přístup k souborům.

## Řešení problémů

**Aplikace se nespustí**
- `fly logs` – zkontrolujte chyby
- Ověřte, že volume existuje: `fly volumes list`

**Data se ztrácejí**
- Volume musí být vytvořeno před prvním deployem
- Ověřte, že `DATABASE_URL` ukazuje na `/data/odbery.db`

**502 Bad Gateway**
- Aplikace možná ještě startuje – počkejte 30–60 s
- Zkontrolujte, že PORT=8080 a aplikace naslouchá na 0.0.0.0
