import csv
import numpy as np
import functools
import itertools
import time
import sys
import random
#
# Pour changer le nombre de matchs
# Mettre la variable dim au nombre de match
# Remplir le prono_input en fonction
#

#----------------------------------------------------------------------
dim = 7
nb_grilles = 1000
nb_top_grilles = 500
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
    print(prono)
    grilles = []
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for i in range(nb_grilles):
            grille = []
            esp = 1
            for j in range(dim):
                n = random.randint(0, 2)
                grille.append(n)
                esp = esp + int(prono[j][n])
            grille.append(esp)
            grilles.append(grille)
        list_triee = sorted(grilles, key=getKey, reverse=True)
        count = 0
        for row in list_triee:
            if count < nb_top_grilles:
                count+=1
                writer.writerow(row)

# cle pour le tri
def getKey(item):
    print(item[dim])
    return item[dim]

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

