import csv
import numpy as np
import functools
import itertools
import time
import sys

#
# Pour changer le nombre de matchs
# Mettre la variable dim au nombre de match
# Rajouter autant de variables i,j,k, ... dans les 3 listes dans csv_writer
# Remplir le prono_input en fonction
#

#----------------------------------------------------------------------
dim = 7
en_entree = "prono_input_7.csv"
en_sortie = "mes_500_grilles_7.csv"
def csv_reader(file_obj):
    """
    Read a csv file
    """
    global prono
    # le tableau qui contient les pronos
    prono = [list(map(int,rec[:-1])) for rec in csv.reader(file_obj, delimiter=';')]
    prono = np.array(prono, np.int)


# ecriture du fichier de sortie
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    global prono
    global dim
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        list_a_trier = []
        # on genere toutes les combinaisons possibles avec pour chaque match 0,1 ou 2
        for (i,j,k,l,m,n,o) in itertools.product(range(3), repeat=dim):
            tupl = np.array([i,j,k,l,m,n,o], dtype=int)
            #on calcule l'esperance de cette combinaison
            esp = esperance(tupl)
            #on cree une liste qui contient toutes les grilles et l'esperance associee
            list_a_trier.append([esp,i,j,k,l,m,n,o])
            #on trie la liste par ordre decroissant d'esperance
        list_triee = sorted(list_a_trier, key=getKey, reverse=True)
        counter = int(0)
        for row in list_triee:
            if counter >= 500:
                break 
            writer.writerow(row)
            counter = counter + 1

# cle pour le tri
def getKey(item):
    return item[0]


# calcul de l'esperance pour une grille
def esperance(grille):
    global prono
    global dim
    esps = np.empty(dim)
    for i in range(dim):
        esps[i] = prono[i,int(grille[i])]
    esp = int(functools.reduce(lambda x, y: x*y, esps))
    return esp


#----------------------------------------------------------------------

#             - MAIN -              #
start_time = time.time()

# fichier csv en entier sous la forme:
# 2;4;4;1
# 2;7;1;2
# ...
prono = np.empty((0,3), int)

with open(en_entree, "rt") as f_obj:
    # load pronostics
    csv_reader(f_obj)
    csv_writer(prono, en_sortie)

print("--- %s seconds ---" % (time.time() - start_time))

