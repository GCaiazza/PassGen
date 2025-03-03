#!/usr/bin/env python3
"""
main.py
--------
Questo è il file principale del progetto.
Si occupa di:
- Richiedere all'utente i dati di input (parola chiave e caratteri speciali).
- Invocare le funzioni del modulo password_generator per generare il dizionario di password.
- Stampare i risultati a schermo e salvarli su file.
"""

import sys
from password_generator import generator, utils

def main():
    try:
        # Richiesta della parola chiave all'utente.
        base_word = input("Inserisci la parola chiave: ").strip()
        if not base_word:
            raise ValueError("La parola chiave non può essere vuota.")
        
        # Richiesta dei caratteri speciali (input separato da virgola).
        special_input = input("Inserisci i caratteri speciali da utilizzare (separati da virgola, es: !,@,#). Premi INVIO per saltare: ").strip()
        # Se l'utente non inserisce nulla, la lista sarà vuota.
        special_chars = [ch.strip() for ch in special_input.split(",") if ch.strip()] if special_input else []
        
        # Definizione del dizionario di sostituzioni per le lettere visibili.
        # Nota: per la lettera 's' sono previste due sostituzioni: '5' e '$'.
        substitutions = {
            'a': ['4'],
            'e': ['3'],
            'i': ['1'],
            'o': ['0'],
            's': ['5', '$'],
            'l': ['1']
        }
        
        # Generazione delle varianti con sostituzioni.
        sub_variants = generator.generate_substitution_variants(base_word, substitutions)
        
        # Aggiunta dei caratteri speciali alle varianti solo se sono stati inseriti.
        if special_chars:
            full_variants = generator.add_special_chars(sub_variants, special_chars)
        else:
            full_variants = sub_variants
        
        # Conversione a lista ordinata per una migliore leggibilità.
        final_passwords = sorted(full_variants)
        
        # Stampa del risultato a schermo.
        print("\n--- Dizionario Password Generato ---")
        for pwd in final_passwords:
            print(pwd)
        
        # Salvataggio su file.
        output_file = "password_dictionary.txt"
        if utils.save_to_file(output_file, final_passwords):
            print(f"\nDizionario salvato correttamente in '{output_file}'.")
        else:
            print("\nSi è verificato un errore durante il salvataggio del file.")
    
    except Exception as err:
        print(f"Errore: {err}")
        sys.exit(1)

if __name__ == "__main__":
    main()