# PassGen – Password Generator

## Sommario

1. [Panoramica](#panoramica)  
2. [Analisi del Problema](#analisi-del-problema)  
    1. [Password Prevedibili](#password-prevedibili)  
    2. [Supporto da Studi e Dataset](#supporto-da-studi-e-dataset)  
3. [Funzionalità](#funzionalità)  
4. [Guida Utente](#guida-utente)  
    1. [Requisiti di Sistema](#requisiti-di-sistema)  
    2. [Installazione](#installazione)  
    3. [Uso del Programma](#uso-del-programma)  
5. [Conclusioni](#conclusioni)

---

## Panoramica

**SecPassGen** è uno strumento pensato per generare dizionari di password, utile in ambito di *penetration testing* e sicurezza informatica.  
Questo programma si basa sull’idea che molti utenti scelgono password facili da ricordare, spesso legate a nomi e informazioni personali (ad esempio, date di nascita). Partendo da queste informazioni e applicando diverse trasformazioni (sostituzioni, variazioni di maiuscole/minuscole, aggiunta di caratteri speciali e integrazione di date), SecPassGen crea un elenco di possibili password salvandole in un file di testo.

---

## Analisi del Problema

### Password Prevedibili

Le persone scelgono spesso password semplici, contenenti nomi di familiari, animali domestici, date di nascita o altre informazioni significative. Questa abitudine rende la password **prevedibile** e vulnerabile. Spesso, tali informazioni sono facilmente reperibili dai social media o da altre fonti online.

### Supporto da Studi e Dataset

- **NIST Special Publication 800-63B**  
  Raccomanda password lunghe ma mette in luce che molti utenti adottano credenziali insicure, basate su **elementi personali**.
- **Dataset RockYou**  
  Ha mostrato come gran parte delle password contenga parole comuni o sostituzioni banali (ad es. “s” → “5” o “$”).
- **Verizon Data Breach Investigations Report**  
  Rivela che un numero elevato di violazioni è causato da password facilmente indovinabili grazie all’uso di informazioni personali.

SecPassGen sfrutta questi dati: conoscendo abitudini e informazioni personali di un obiettivo (familiari, date importanti, soprannomi, ecc.), è possibile **generare dizionari mirati** e potenzialmente efficaci nei test di sicurezza.

---

## Funzionalità

- **Sostituzioni e Variazioni di Case**  
  - Le lettere più comuni vengono sostituite con numeri o simboli (es. “a” → “4”, “s” → “5” o “$”).  
  - Ogni parola viene trasformata generando tutte le possibili combinazioni di maiuscole/minuscole.

- **Integrazione di Date**  
  - Per ogni parola si possono inserire (facoltativamente) giorno, mese e anno.  
  - Il programma combina e permuta tali componenti, riflettendo l’abitudine di molti utenti di aggiungere alla password la data di nascita o altre date significative.

- **Caratteri Speciali**  
  - Vengono applicati unicamente come singolo carattere (prefisso, suffisso o entrambi) per ogni variante.  
  - Ciò rispecchia il comportamento reale di molti utenti, che aggiungono *uno* o *pochi* caratteri speciali alle password.

- **Generazione “Lazy”**  
  - L’algoritmo elabora **una parola per volta** e **scrive le combinazioni direttamente** su un file di testo (`password_dictionary.txt`), evitando di caricare in memoria enormi elenchi di password.

- **Controllo Input e Limiti**  
  - Il numero di caratteri speciali è **limitato a 5**, per contenere il rischio di esplosione combinatoria.  
  - Il programma svuota il file `password_dictionary.txt` all’avvio, garantendo output pulito a ogni esecuzione.

---

## Guida Utente

### Requisiti di Sistema

- **Python 3.9+**  
  È consigliato l’uso di un ambiente virtuale per una gestione più ordinata delle dipendenze.

### Installazione

1. **Clonare il repository GitHub**  
   ```bash
   git clone https://github.com/GCaiazza/SecPassGen.git
   cd SecPassGen

	2.	Creare e attivare un ambiente virtuale (opzionale ma consigliato)

python -m venv venv
# Su Linux/macOS:
source venv/bin/activate
# Su Windows:
venv\Scripts\activate


3.	**Verificare eventuali dipendenze**
In questo progetto non sono richiesti pacchetti esterni, ma se in futuro dovessero aggiungersi, basterà installarli con pip install -r requirements.txt.

## Uso del Programma
	1.	Avviare il programma

python main.py


	2.	Step 1 – Parole Chiave
	•	Inserire le parole chiave (una alla volta).
	•	Premere CTRL+C quando si è terminato (se almeno una parola è stata inserita) o per uscire (se nessuna parola è stata inserita).
	3.	Step 2 – Date
	•	Per ogni parola chiave, il programma chiederà di inserire facoltativamente giorno, mese e anno.
	•	Premendo CTRL+C in un campo, verrà saltata la data per quella parola.
	4.	Step 3 – Caratteri Speciali
	•	Inserire i caratteri speciali in un’unica stringa (senza spazi).
	•	Se il numero di caratteri speciali supera 5, il programma si fermerà.
	•	Premendo CTRL+C in questa fase, si esce senza creare il dizionario.
	5.	Generazione del Dizionario
	•	Il programma genera le varianti per ogni parola e data eventualmente fornita.
	•	Tutte le combinazioni vengono scritte (una per riga) in password_dictionary.txt.
	•	Al termine, un messaggio avvisa del completamento e il file conterrà il dizionario definitivo.

## Conclusioni

PassGen è progettato per coprire un’ampia gamma di possibili varianti di password, partendo da informazioni personali (parole chiave e date). Gli studi di enti qualificati (NIST, analisi RockYou, report Verizon, ecc.) confermano che molti utenti scelgono password deboli e prevedibili. Questo strumento nasce per fornire ai penetration tester un metodo semplice ed efficace di creare liste di password altamente mirate, senza sovraccaricare la memoria grazie alla generazione “lazy”.

Sebbene non sia una garanzia assoluta di trovare tutte le password, PassGen rappresenta un ottimo compromesso fra realismo e contenimento delle combinazioni, garantendo un dizionario sufficientemente vasto ma pratico da utilizzare negli scenari di test.

Per segnalare problemi, proporre miglioramenti o porre domande, è possibile aprire una issue direttamente su GitHub o contattare il manutentore del progetto.

Sviluppato con ❤️ per la sicurezza informatica.
