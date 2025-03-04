#!/usr/bin/env python3
"""
main.py
--------
File principale del progetto.
Funzionalità:
- Step 1: Inserisci le parole chiave una alla volta.
    • Premi CTRL+C per terminare l'inserimento se hai già inserito almeno una parola.
    • Se non hai parole da inserire, premi CTRL+C per uscire.
- Step 2: Per ogni parola, inserisci le informazioni di data (giorno, mese, anno).
    • Premi CTRL+C in un campo per saltare l'inserimento della data per quella parola.
    • Se l'input per la data è errato, viene ripetuto fino a 3 volte.
- Step 3: Inserisci i caratteri speciali globali (scrivili tutti insieme senza spazi).
    • Premi CTRL+C per uscire senza creare il dizionario.
- Il file "password_dictionary.txt" viene riscritto all'avvio e, per ogni parola, le varianti vengono generate e scritte immediatamente.
"""

import sys
from password_generator import generator

MAX_SPECIAL = 5

def validate_date_component_manual(s):
    if not s:
        return ""
    if not s.isdigit():
        raise ValueError("Deve essere un numero.")
    if len(s) > 2:
        raise ValueError("Deve essere composto da 1 o 2 cifre.")
    return s

def get_input(prompt, validation_func=None):
    """
    Chiede un input all'utente, permettendo fino a 3 tentativi in caso di errore.
    Se l'utente preme CTRL+C, il campo viene considerato saltato (ritorna stringa vuota).
    """
    attempts = 0
    while attempts < 3:
        try:
            user_input = input(f"{prompt}: ")
        except KeyboardInterrupt:
            print()  # va a capo
            return ""
        user_input = user_input.strip()
        if validation_func:
            try:
                return validation_func(user_input)
            except Exception as e:
                print("Errore:", e)
                attempts += 1
                if attempts < 3:
                    print("Riprova ancora.")
        else:
            return user_input
    print("Torna quando hai le idee più chiare! Premi un tasto per terminare il programma...")
    input()
    sys.exit(1)

def main():
    try:
        # Step 1: Inserimento parole chiave una alla volta
        keywords = []
        print("Step 1: Inserisci le parole chiave una alla volta.")
        print("• Premi CTRL+C per terminare l'inserimento (se hai già inserito almeno una parola).")
        print("• Se non hai parole da inserire, premi CTRL+C per uscire.")
        while True:
            try:
                word = input("Inserisci una parola chiave: ").strip()
            except KeyboardInterrupt:
                if keywords:
                    print()
                    break
                else:
                    print("\nNessuna parola inserita. Uscita dal programma.")
                    sys.exit(0)
            if word == "":
                if keywords:
                    break
                else:
                    print("Devi inserire almeno una parola chiave o premi CTRL+C per uscire.")
                    continue
            keywords.append(word)
        
        if not keywords:
            print("Nessuna parola chiave inserita. Uscita dal programma.")
            sys.exit(0)
        
        # Step 2: Per ogni parola, inserisci le informazioni di data (opzionali)
        words_with_dates = []  # Lista di tuple: (parola, (giorno, mese, anno))
        for word in keywords:
            print(f"\nStep 2: Inserisci le informazioni di data per la parola '{word}'.")
            print("• Premi CTRL+C in un campo per saltare la data per questa parola.")
            day = get_input("Giorno (1 o 2 cifre)", validate_date_component_manual)
            month = get_input("Mese (1 o 2 cifre)", validate_date_component_manual)
            year = get_input("Anno (1 o 2 cifre)", validate_date_component_manual)
            words_with_dates.append((word, (day, month, year)))
        
        # Step 3: Inserisci i caratteri speciali globali
        print("\nStep 3: Inserisci i caratteri speciali da utilizzare (scrivili tutti insieme senza spazi).")
        print("• Premi CTRL+C per uscire senza creare il dizionario.")
        try:
            special_input = input("Inserisci i caratteri speciali: ").strip()
        except KeyboardInterrupt:
            print("\nUscita dal programma per richiesta dell'utente.")
            sys.exit(0)
        special_chars = list(special_input) if special_input else []
        if len(special_chars) > MAX_SPECIAL:
            print(f"Hai inserito troppi caratteri speciali ({len(special_chars)}). Il massimo consentito è {MAX_SPECIAL}.")
            sys.exit(1)
        
        # Sostituzioni per le lettere "visibili"
        substitutions = {
            'a': ['4'],
            'e': ['3'],
            'i': ['1'],
            'o': ['0'],
            's': ['5', '$'],
            'l': ['1']
        }
        
        # Prepara il file: svuota il file all'avvio
        output_file = "password_dictionary.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            pass
        
        print("\nGenerazione in corso...")
        # Elaborazione lazy: per ogni parola, genera le varianti e scrivile sul file
        for word, (day, month, year) in words_with_dates:
            word_variants = generator.generate_substitution_variants(word, substitutions)
            if day or month or year:
                date_variants = generator.generate_date_variants(day, month, year)
                if date_variants:
                    word_variants = generator.add_date_variants(word_variants, date_variants)
            if special_chars:
                word_variants = generator.add_special_chars(word_variants, special_chars)
            with open(output_file, "a", encoding="utf-8") as f:
                for variant in word_variants:
                    f.write(variant + "\n")
        print("\nGenerazione completata.")
        print(f"Dizionario salvato in '{output_file}'.")
    
    except Exception as err:
        print(f"Errore: {err}")
        sys.exit(1)

if __name__ == "__main__":
    main()