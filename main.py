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

def num_players():
    while True:
        num_players = input("Inserisci numero di giocatori in gioco: ")
        if not num_players.isdigit():
            continue
        else:
            break

    return num_players

def crea_mazzo(num_mazzi):
    mazzo = {}
    valori = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Regina', 'Re', 'Asso']
    for valore in valori:
        mazzo[valore] = 4 * num_mazzi
    return mazzo

def admitted(card):
    if card == "Asso" or card == "Jack" or card == "Re" or card == "Regina":
        return True

    if card.isdigit():
        num = float(card)
        if 2 <= num <= 10:
            return True

    return False

def your_cards():
    input_1 = input("Inserisci le tue carte: ")
    input_2 = input("")
    while True:
        if admitted(input_1):
            print("Valore 1 ok")
            if admitted(input_2):
                print("Valore 2 ok")
                break
            else:
                print("Valore 2 errato, riprova")
                input_2 = input("")
        else:
            print("Valore 1 errato, riprova")
            input_1 = input("")
            continue

    return input_1, input_2

def opponent_card():
    while True:
        input_d = input("Inserisci la carta del dealer: ")
        if admitted(input_d):
            print("Carta del dealer OK")
            return input_d


def carte_uscite(mazzo):
    print("Aggiungi tutte le carte che escono")
    while True:
        carta = input("")
        if not admitted(carta):
            print("Not valid, try again")
            a = input("Vuoi inserirne un altro? si/no")
            if a !="si":
                break
        else:
            key = carta
            mazzo[key] -= 1
            print("Rimosso un " + str(key))
            a = input("Vuoi inserirne un altro? si/no: ")
            if a != "si":
                print()
                break
    return



if __name__ == '__main__':
    num_mazzi = num_mazzi()
    tot_carte = 52 * num_mazzi
    print(tot_carte)
    players = num_players()
    mazzo = crea_mazzo(num_mazzi)
    print(mazzo)
    carta1, carta2 = your_cards()
    dealer = opponent_card()

    # aggiorna mazzo
    mazzo[carta1] -= 1
    mazzo[carta2] -= 1
    mazzo[dealer] -= 1
    tot_carte -= 3
    print(tot_carte)

    carte_uscite(mazzo)



