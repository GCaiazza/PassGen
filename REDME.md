# PassGen
## Password Dictionary Generator for Penetration Testing

Questo progetto genera un dizionario di password per penetration test a partire da parole chiave.
Il programma:
- Richiede in input una parola chiave.
- Genera varianti applicando sostituzioni di lettere "visibili" in modo incrementale (da una sostituzione fino a sostituirle tutte).  
  In particolare, per la lettera "s" sono previste due sostituzioni: "5" e "$".
- Chiede all'utente quali caratteri speciali utilizzare e li aggiunge come prefisso, suffisso o in entrambe le posizioni, provando tutte le combinazioni possibili.
- Se l'utente non inserisce caratteri speciali, il dizionario viene creato senza l'aggiunta di questi.
- Evita duplicati.
- Stampa il risultato a schermo e lo salva in un file esterno.

## Come avviarlo
1. **Installare Python**: Assicurati che Python 3.7+ sia installato.
2. **Eseguire il fime main.py** 
3. **Seguire le istruzioni che compariranno a schermo.** 

Il file verrà salvato nella directory dove è contenuto il file main.py.