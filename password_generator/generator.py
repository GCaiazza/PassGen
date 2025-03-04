"""
generator.py
-------------
Contiene le funzioni per generare varianti di password a partire da una parola:
- Generazione di varianti con sostituzioni per le lettere "visibili".
- Generazione di tutte le combinazioni possibili di lettere minuscole e maiuscole.
- Aggiunta di caratteri speciali, applicando un solo carattere speciale per volta come prefisso, suffisso e in entrambe le posizioni.
- Generazione di varianti di data da informazioni opzionali e combinazione con le parole.
"""

import itertools

def generate_case_variants(word):
    """
    Genera tutte le combinazioni possibili di lettere minuscole e maiuscole per una data parola.
    
    Input:
        word (str): la parola da trasformare.
    Output:
        set: insieme di varianti con combinazioni di case.
    """
    possibilities = []
    for ch in word:
        if ch.isalpha():
            possibilities.append([ch.lower(), ch.upper()])
        else:
            possibilities.append([ch])
    return {''.join(prod) for prod in itertools.product(*possibilities)}

def generate_substitution_variants(word, subs):
    """
    Genera varianti della parola sostituendo le lettere "visibili" definite in subs,
    in maniera incrementale (sostituendo una lettera, poi due, ecc.). Per ogni variante,
    vengono generate tutte le combinazioni di case.
    
    Input:
        word (str): parola base.
        subs (dict): mapping delle sostituzioni (es. {'a': ['4'], ...}).
    Output:
        set: insieme di varianti generate.
    """
    substitution_variants = {word}
    indices = [i for i, ch in enumerate(word) if ch.lower() in subs]
    
    for r in range(1, len(indices) + 1):
        for combo in itertools.combinations(indices, r):
            choices_lists = [subs[word[i].lower()] for i in combo]
            for replacement_combo in itertools.product(*choices_lists):
                new_word = list(word)
                for idx, replacement in zip(combo, replacement_combo):
                    new_word[idx] = replacement
                substitution_variants.add("".join(new_word))
    
    all_variants = set()
    for var in substitution_variants:
        all_variants.update(generate_case_variants(var))
    return all_variants

def add_special_chars(variants, special_chars):
    """
    Aggiunge a ciascuna variante le combinazioni con i caratteri speciali forniti,
    applicando un singolo carattere speciale per volta.
    Per ogni variante e per ciascun carattere speciale, viene generato:
      - Il carattere speciale come prefisso.
      - Il carattere speciale come suffisso.
      - Il carattere speciale sia come prefisso che come suffisso.
    
    Input:
        variants (iterable): insieme di varianti.
        special_chars (list): lista di caratteri speciali (str).
    Output:
        set: insieme aggiornato di varianti.
    """
    final_variants = set(variants)
    for variant in variants:
        for ch in special_chars:
            final_variants.add(ch + variant)
            final_variants.add(variant + ch)
            final_variants.add(ch + variant + ch)
    return final_variants

def generate_date_component(component):
    """
    Genera le varianti per una componente di data (giorno, mese, anno).
    Se la componente è di una cifra, restituisce sia la versione singola sia quella zero-padded.
    Se la componente ha due cifre, restituisce solo quella.
    Se la componente è vuota, restituisce un set vuoto.
    Solleva ValueError se il valore non è numerico o ha più di 2 cifre.
    
    Input:
        component (str): componente della data.
    Output:
        set: insieme di varianti per il componente.
    """
    if not component:
        return set()
    if not component.isdigit():
        raise ValueError(f"Il valore '{component}' non è numerico.")
    if len(component) == 1:
        return {component, component.zfill(2)}
    elif len(component) == 2:
        return {component}
    else:
        raise ValueError(f"Il valore '{component}' non è valido. Deve essere di 1 o 2 cifre.")

def generate_date_variants(day, month, year):
    """
    Genera un insieme di varianti di data basate sulle componenti giorno, mese e anno.
    Vengono generate tutte le combinazioni possibili:
      - Se sono presenti tutte e tre le componenti, vengono generate tutte le permutazioni.
      - Se sono presenti solo due, vengono generate entrambe le combinazioni.
      - Se è presente solo una, viene restituita quella singola componente.
    
    Input:
        day (str): giorno (opzionale).
        month (str): mese (opzionale).
        year (str): anno (opzionale).
    Output:
        set: insieme di stringhe rappresentanti le date generate.
    """
    components = []
    day_set = generate_date_component(day) if day else set()
    month_set = generate_date_component(month) if month else set()
    year_set = generate_date_component(year) if year else set()
    
    if day_set:
        components.append(('day', day_set))
    if month_set:
        components.append(('month', month_set))
    if year_set:
        components.append(('year', year_set))
    
    date_variants = set()
    n = len(components)
    for r in range(1, n + 1):
        for subset in itertools.combinations(components, r):
            for perm in itertools.permutations(subset):
                lists = [item[1] for item in perm]
                for prod in itertools.product(*lists):
                    date_variants.add("".join(prod))
    return date_variants

def add_date_variants(variants, date_variants):
    """
    Combina ogni variante di parola con ogni variante di data.
    Per ciascuna parola vengono generate:
      - la concatenazione parola + data
      - la concatenazione data + parola
    
    Input:
        variants (iterable): insieme di varianti di parola.
        date_variants (iterable): insieme di varianti di data.
    Output:
        set: insieme aggiornato di varianti con le date combinate.
    """
    combined = set(variants)
    for word in variants:
        for date_str in date_variants:
            combined.add(word + date_str)
            combined.add(date_str + word)
    return combined