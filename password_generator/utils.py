"""
utils.py
---------
Contiene funzioni di utilità per il progetto, come il salvataggio su file.
"""

def save_to_file(filename, data):
    """
    Salva l'elenco dei dati (password) su un file di testo.
    
    Input:
        filename (str): nome del file in cui salvare i dati.
        data (iterable): elenco (o set) di stringhe da salvare.
    
    Output:
        bool: True se il salvataggio ha avuto successo, False altrimenti.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data:
                file.write(item + "\n")
        return True
    except Exception as e:
        print(f"Errore durante il salvataggio su file: {e}")
        return False