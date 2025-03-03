"""
generator.py
-------------
Contiene le funzioni principali per generare le varianti di password:
- Sostituzione delle lettere "visibili" secondo un mapping.
- Generazione di tutte le combinazioni possibili di lettere minuscole e maiuscole per ciascuna variante.
- Aggiunta di caratteri speciali (prefisso, suffisso, entrambi) alle varianti.

La funzione di sostituzione è stata modificata per:
1. Gestire, per ciascuna lettera, più possibili sostituzioni (es. 's' con '5' e '$').
2. Generare per ogni variante tutte le possibili combinazioni di lettera minuscola/maiuscola.
"""

import itertools

def generate_case_variants(word):
    """
    Genera tutte le combinazioni possibili di lettere minuscole e maiuscole per una data parola,
    trattando ogni lettera singolarmente.

    Input:
        word (str): la parola da trasformare.
    
    Output:
        set: un insieme contenente tutte le combinazioni possibili.
    """
    possibilities = []
    for ch in word:
        if ch.isalpha():
            possibilities.append([ch.lower(), ch.upper()])
        else:
            possibilities.append([ch])
    # Calcola il prodotto cartesiano per ottenere tutte le combinazioni.
    variants = {''.join(prod) for prod in itertools.product(*possibilities)}
    return variants

def generate_substitution_variants(word, subs):
    """
    Genera varianti della parola sostituendo le lettere "visibili" (definite nel dizionario subs)
    in maniera incrementale: una lettera, poi due, fino a sostituirle tutte.
    
    Per ogni lettera che ha più sostituzioni possibili (es. 's' con '5' e '$'),
    viene considerato il prodotto cartesiano delle possibili scelte.
    Inoltre, per ciascuna variante ottenuta vengono generate tutte le combinazioni di lettere minuscole e maiuscole.
    
    Input:
        word (str): la parola base.
        subs (dict): mappatura delle sostituzioni, ad esempio:
                     {'a': ['4'], 'e': ['3'], 'i': ['1'], 'o': ['0'], 's': ['5', '$'], 'l': ['1']}.
    
    Output:
        set: un insieme di varianti della parola (compresa la parola originale) con tutte le combinazioni di case.
    """
    substitution_variants = set()
    substitution_variants.add(word)
    
    # Identifica gli indici delle lettere che possono essere sostituite.
    indices = [i for i, ch in enumerate(word) if ch.lower() in subs]
    
    # Genera tutte le combinazioni non vuote di questi indici.
    for r in range(1, len(indices)+1):
        for combo in itertools.combinations(indices, r):
            # Per ciascun indice, recupera la lista delle possibili sostituzioni.
            choices_lists = [subs[word[i].lower()] for i in combo]
            # Itera sul prodotto cartesiano delle possibili sostituzioni per questi indici.
            for replacement_combo in itertools.product(*choices_lists):
                new_word = list(word)
                for idx, replacement in zip(combo, replacement_combo):
                    new_word[idx] = replacement
                substitution_variants.add("".join(new_word))
    
    # Per ogni variante di sostituzione, genera tutte le combinazioni di case e unisci i risultati.
    all_variants = set()
    for var in substitution_variants:
        all_variants.update(generate_case_variants(var))
    
    return all_variants

def add_special_chars(variants, special_chars):
    """
    Aggiunge a ciascuna variante le combinazioni dei caratteri speciali specificati.
    Per ogni variante, viene aggiunto:
      - Il carattere speciale come prefisso.
      - Il carattere speciale come suffisso.
      - Il carattere speciale sia come prefisso che come suffisso.
    
    Input:
        variants (iterable): l'insieme (o lista) di varianti generate.
        special_chars (list): lista di caratteri speciali (str) forniti dall'utente.
    
    Output:
        set: l'insieme aggiornato di varianti comprensivo delle versioni con caratteri speciali.
    """
    final_variants = set(variants)
    
    # Per ogni variante, aggiunge le combinazioni con ciascun carattere speciale.
    for variant in variants:
        for ch in special_chars:
            final_variants.add(ch + variant)       # Prefisso
            final_variants.add(variant + ch)       # Suffisso
            final_variants.add(ch + variant + ch)  # Entrambi
    
    return final_variants