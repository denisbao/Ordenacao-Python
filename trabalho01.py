import platform
import os
import time
import string
import tabulate
# ==============================================================================

def clearScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# ==============================================================================

def savePokemon():
    clearScreen()
    arquivo = open("poke.txt", 'a')
    nome = str(input("Qual é o nome do pokemon: "))
    ok = False
    while not ok:
        try:
            cp = int(input("Quanto é o seu CombatPower?: "))
            ok = True
        except Exception as e:
            print("\nCombatPower só aceita valores inteiros!")
    ok = False
    while not ok:
        try:
            raridade = int(input("Qual é a sua raridade?: "))
            ok = True
        except Exception as e:

            print("\nRaridade só aceita valores inteiros!")


    arquivo.write(nome.title())
    arquivo.write("\n")
    arquivo.write(str(cp))
    arquivo.write("\n")
    arquivo.write(str(raridade))
    arquivo.write("\n")
    arquivo.close()
    time.sleep(1)
    print("\n\n      Pokemon Capturado com Sucesso!\n\n")
    wait = input("...Pressione enter para voltar ao menu...")
    clearScreen()

# ==============================================================================

def lerArquivo():
    listTemp = [line.rstrip('\n') for line in open('poke.txt')]
    n_linhas = 0
    with open("poke.txt", "r") as ins:
        for line in ins:
            n_linhas += 1
    ins.close
    count = 0
    n_pokemons = int(n_linhas/3)
    listaPokemons = []
    for i in range(0,n_pokemons):
        umPokemom = []
        for j in range(3): #numero de dados sobre cada pokemom
            if j == 1 or j == 2:
                umPokemom.append(int(listTemp[count]))
            else:
                umPokemom.append(listTemp[count])
            count += 1
        listaPokemons.append(umPokemom)
    return listaPokemons

# ==============================================================================

def quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = partition(lista, inicio, fim)
        quicksort(lista, inicio, pivo-1)
        quicksort(lista, pivo+1, fim)
    return(lista)

def partition(lista, inicio, fim):
    pivo = lista[inicio]
    esquerda = inicio+1
    direita = fim
    ok = False
    while not ok:
        while esquerda <= direita and lista[esquerda] <= pivo:
            esquerda += 1
        while esquerda <= direita and lista[direita] >= pivo:
            direita -= 1
        if direita < esquerda:
            ok = True
        else:
            aux = lista[esquerda]
            lista[esquerda] = lista[direita]
            lista[direita] = aux
    aux = lista[inicio]
    lista[inicio] = lista[direita]
    lista[direita] = aux
    return direita

# ==============================================================================

def orderAlfa(lista,inicio,fim):
    quicksort(lista,0,len(lista)-1)
    clearScreen()
    print("%-20s%-20s%-20s" % ("NOME","COMBAT-POWER","RARIDADE"))
    for i in range(0,len(lista)):
        print("%-20s%-20i%-20i" % (lista[i][0],lista[i][1],lista[i][2]))
    print("\n\n")
    wait = input("...Pressione enter para voltar ao menu...")
    clearScreen()

# ==============================================================================

def printRareVIO(lista, rareVIO):
    print("%-20s%-20s%-20s" % ("NOME","COMBAT-POWER","RARIDADE"))
    for i in range(0,len(lista)):
        print("%-20s%-20i%-20i" % (lista[rareVIO[i]][0],lista[rareVIO[i]][1],lista[rareVIO[i]][2]))
    print("\n\n")

def printCPVIO(lista, cpVIO):
    print("%-20s%-20s%-20s" % ("NOME","COMBAT-POWER","RARIDADE"))
    for i in range(0,len(lista)):
        print("%-20s%-20i%-20i" % (lista[cpVIO[i]][0],lista[cpVIO[i]][1],lista[cpVIO[i]][2]))
    print("\n\n")
# ==============================================================================

def orderRare(lista):
    listaAux = list(lista)
    rareVIO = []
    for i in range(0,len(listaAux)):
        menor=i
        for k in range(i,len(listaAux)):
            if listaAux[k][2]<listaAux[menor][2]:
                menor=k
        aux = listaAux[menor]
        listaAux[menor] = listaAux[i]
        listaAux[i] = aux
    #monta o VIO:
    for i in range(0,len(lista)):
        for j in range(0,len(lista)):
            if listaAux[i] == lista[j]:
                rareVIO.append(j)
    print("Lista Impressa pelo VIO: ")
    clearScreen()
    printRareVIO(lista, rareVIO)
    rareVIO = []
    wait = input("...Pressione enter para voltar ao menu...")
    clearScreen()

def orderCP(lista):
    listaAux = list(lista)
    cpVIO = []
    for i in range(0,len(listaAux)):
        menor=i
        for k in range(i,len(listaAux)):
            if listaAux[k][1]<listaAux[menor][1]:
                menor=k
        aux = listaAux[menor]
        listaAux[menor] = listaAux[i]
        listaAux[i] = aux
    #monta o VIO:
    for i in range(0,len(lista)):
        for j in range(0,len(lista)):
            if listaAux[i] == lista[j]:
                cpVIO.append(j)
    print("Lista Impressa pelo VIO: ")
    clearScreen()
    printCPVIO(lista, cpVIO)
    wait = input("...Pressione enter para voltar ao menu...")
    clearScreen()

# ==============================================================================

def menu():
    clearScreen()
    choise = 0
    while choise != 5:
        lista = lerArquivo()
        print("  ||   1 - Adicionar Pokemon")
        print("  ||   2 - Listar Alfabeticamente")
        print("  ||   3 - Listar por Raridade")
        print("  ||   4 - Listar por CombatPower")
        print("  ||   5 - Sair")
        choise = int(input("Opção: "))
        if (choise == 1):
            savePokemon()
        elif (choise == 2):
            orderAlfa(lista,0,len(lista)-1)
        elif (choise == 3):
            orderRare(lista)
        elif (choise == 4):
            orderCP(lista)
        elif (choise == 5):
            pass
        elif choise < 1 or choise > 5:
            print("Opção inválida.")



# ==============================================================================
# PRINCIPAL:
menu()

# ==============================================================================
