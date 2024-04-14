def num_mazzi():
    while True:
        input_numero = input("Inserisci numero mazzi (per default=6 premere invio): ")
        if input_numero == "":
            numero = 6  # Imposta il valore predefinito a 6 se l'utente non fornisce alcun numero
            break
        else:
            try:
                numero = float(input_numero)
                break  # Esci dal ciclo se l'input è un numero valido
            except ValueError:
                print("Errore! Inserisci un numero valido.")
    return numero

def crea_mazzo(num_mazzi):
    mazzo = {}
    valori = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Regina', 'Re', 'Asso']
    for valore in valori:
        mazzo[valore] = 4 * num_mazzi
    return mazzo


if __name__ == '__main__':
    num_mazzi = num_mazzi()
    mazzo_scala = crea_mazzo(num_mazzi)

    # Stampiamo il dizionario per verificare
    for carta, numero in mazzo_scala.items():
        print(f"{carta}: {numero}")

