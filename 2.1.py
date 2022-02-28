print('QUESTO SCRIPT CONVERTE IL TUO ORARIO IN SECONDI')

ore = int(input('quante ore devo convertire? : '))
minuti = int(input('quanti minuti devo convertire? : '))
secondi = int(input('quanti secondi devo convertire? : '))

risultato = ore*60*60 + minuti*60 + secondi

print("L'orario inserito e convertito in secondi equivale a: ", risultato)
