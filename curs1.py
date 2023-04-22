lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# Afișarea listei inițiale
print("Lista inițială:", lista)

# Afișarea listei ordonate ascendent
lista_asc = sorted(lista)
print("Lista ordonată ascendent:", lista_asc)

# Afișarea listei ordonate descendent
lista_desc = sorted(lista, reverse=True)
print("Lista ordonată descendent:", lista_desc)

# Afișarea numerelor cu indici pari din listă
numere_pare = lista[::2]
print("Numerele cu indici pari din listă:", numere_pare)

# Afișarea numerelor cu indici impari din listă
numere_impare = lista[1::2]
print("Numerele cu indici impari din listă:", numere_impare)

# Afișarea elementelor multipli ai lui 3
multipli_3 = []
for elem in lista:
    if elem % 3 == 0:
        multipli_3.append(elem)
print("Elementele multipli ai lui 3:", multipli_3)