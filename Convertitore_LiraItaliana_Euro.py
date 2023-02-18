print ('convertitore lire italiane euro')
print ("")
def menu():
    print ('1.  Vuoi convertire Euro in ITL?')
    print ('2.  Vuoi convertire ITL in Euro?')
    print ('3.  Esci dal programma')
    print ("")
menu()
i=0
menu_choice = 0
while i == 0:
    menu_choice = (int ( input ('scegli cosa vuoi fare (1-3):   ')))
    print ('Hai scelto l operazione: ', menu_choice)
    if menu_choice == 1:
        userEuro = float(input("Scrivi l'importo in Euro che vuoi convertire in lire italiane:  €  "))
        ITL = userEuro *  1936.27
        print ("Ecco il tuo cambio: ")
        print  ("€", userEuro, " =  £ ", ITL)
        print ("")
        menu()
    elif menu_choice ==2:
        userUSD = float(input("Scrivi l'importo in lire italiane che vuoi convertire in euro:  $  "))
        Euro = userUSD * 0.0005
        print ("Ecco il tuo cambio: ")
        print  ("£", userUSD, " =  € ", Euro)
        print ("")
        menu()
    elif menu_choice == 3:
        print ("grazie per aver usato Convertitore Lire Italiane Euro!")
        break
