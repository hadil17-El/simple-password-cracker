import hashlib #Python ha una libreria chiamata hashlib che ci permette di creare hash (come MD5, SHA-1, SHA-256).

#Definisci l’hash da “craccare”
#Qui metti l’hash MD5 della password che vuoi trovare.
#Per esempio, l’hash MD5 della parola "ciao" è "7d6a021b9c7c34c0bbf9a1c4de60b2e7"

target_hash = "7d6a021b9c7c34c0bbf9a1c4de60b2e7"

#Crea una lista di possibili password
#Puoi usare una lista semplice di parole comuni (wordlist).
#In un caso reale, si userebbe una wordlist molto grande, ma per imparare va benissimo così:

wordlist = ["admin", "1234","password","ciao","hello","qwerty"]

#Prova tutte le parole della lista
#Con un ciclo for, per ogni parola:
#Calcoli l’hash MD5
#Confronti l’hash calcolato con quello target
#Se combacia, hai trovato la password!

for parola in wordlist:
     # Calcola l'hash MD5 della parola (devi codificare la stringa in bytes)
    hashed = hashlib.md5(parola.encode()).hexdigest()
    print(f"Provo: {parola} -> {hashed}")

    if hashed == target_hash:
        print(f"\n Password trovata: {parola}")
        break  # Esci dal ciclo perché abbiamo trovato la password
    else:

        print("\n Nessuna corrispondenza trovata.")