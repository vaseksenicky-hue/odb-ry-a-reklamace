#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spuštění aplikace přes Waitress – dostupná z celé sítě (0.0.0.0).
Použití: python run_waitress.py
"""

import os
import sys

# Cesta k adresáři site (kde je app.py)
SITE_DIR = os.path.dirname(os.path.abspath(__file__))
if SITE_DIR not in sys.path:
    sys.path.insert(0, SITE_DIR)
os.chdir(SITE_DIR)

from app import app
from waitress import serve

# Host 0.0.0.0 = naslouchá na všech rozhraních (přístup z jiných počítačů v síti)
# Port lze změnit přes proměnnou prostředí PORT (např. PORT=5000)
HOST = os.environ.get("WAITRESS_HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8080"))

if __name__ == "__main__":
    print(f"Waitress: http://{HOST}:{PORT}")
    print("Ukončení: Ctrl+C")
    serve(app, host=HOST, port=PORT)
