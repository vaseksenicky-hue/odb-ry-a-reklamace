#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Skript pro reset databáze - vytvoří novou čistou databázi
POUŽÍVEJTE OPATRNĚ - SMAŽE VŠECHNA DATA!

Spustit: python reset_db.py
"""

import os
import sys
from app import app, db, User, Pobocka, Odber, Reklamace, Akce, ReklamaceLog

def reset_database():
    """Vytvoří novou čistou databázi."""
    print("=" * 60)
    print("⚠️  VAROVÁNÍ: Tento skript smaže všechny existující data!")
    print("=" * 60)
    
    response = input("Opravdu chcete pokračovat? (ano/ne): ")
    if response.lower() != 'ano':
        print("Operace zrušena.")
        return
    
    with app.app_context():
        try:
            # Smazání všech tabulek
            print("\n🗑️  Mažu všechny tabulky...")
            db.drop_all()
            
            # Vytvoření nových tabulek
            print("📦 Vytvářím nové tabulky...")
            db.create_all()
            
            # Vytvoření defaultních poboček
            print("🏢 Vytvářím defaultní pobočky...")
            pobocky = [
                Pobocka(nazev='Teplice'),
                Pobocka(nazev='Děčín')
            ]
            db.session.bulk_save_objects(pobocky)
            db.session.commit()
            
            # Vytvoření defaultního admina
            print("👤 Vytvářím defaultního admina...")
            admin = User(
                username='admin',
                pin='0000',
                role='admin',
                jmeno='Administrátor'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            
            print("\n✅ Databáze byla úspěšně resetována!")
            print("\n📋 Defaultní přihlašovací údaje:")
            print("   Username: admin")
            print("   PIN: 0000")
            print("   Password: admin123")
            print("\n⚠️  DŮLEŽITÉ: Změňte tyto údaje po prvním přihlášení!")
            
        except Exception as e:
            print(f"\n❌ Chyba při resetování databáze: {str(e)}")
            import traceback
            traceback.print_exc()
            db.session.rollback()

if __name__ == '__main__':
    reset_database()
