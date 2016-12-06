import csv
import numpy as np
import functools
import itertools
import time

#


#----------------------------------------------------------------------
dim = 7
en_entree = "gagnant_input_7.csv"
en_entree_grilles = "mes_500_grilles_7.csv"
en_sortie = "sortie_grilles_gagnantes.csv"
def csv_reader(file_obj):
    """
    Read a csv file
    """
    global gagnant
    global gain
    # le tableau qui contient les gagnants
    reader = csv.reader(file_obj, delimiter=';')
    gagnant = next(reader)
    gain = next(reader)
    gagnant = [list(map(int,gagnant))]
    gagnant=gagnant[0]
    gain = [list(map(int,gain))]
    gain=gain[0]

def csv_reader2(file_obj):
    """
    Read a csv file
    """
    global grilles
    # le tableau qui contient les gagnants
    grilles = [list(map(int,rec[1:])) for rec in csv.reader(file_obj, delimiter=';')]


# ecriture du fichier de sortie
def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    global dim
    somme = 0
    count_win=[0,0,0]
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        list_a_trier = []
        # on genere toutes les combinaisons possibles avec pour chaque match 0,1 ou 2
        for row in grilles:
            count = 0
            for i in range(dim): # 0,1,.. ,dim-1
                if row[i] == gagnant[i]:
                    count+=1
                if count < i - 1 : # si t'en as deja 3 de faux
                    break
            if count > dim - 3: # au moins 4 sur 6 pour dim=6
                row.append(count)
                writer.writerow(row)
                count_win[dim - count] +=1
                print (gain[dim - count])
                somme += gain[dim - count] # soit 0 le gros lot 1 le 2eme
        print("you win ", somme, " $, bitch !")
        print("with ", count_win[0], " gros lot")
        print("with ", count_win[1], " middle lot")
        print("with ", count_win[2], " small lot")



#----------------------------------------------------------------------

#             - MAIN -              #
start_time = time.time()

# fichier csv en entier sous la forme:
# 2;4;4;1
# 2;7;1;2
# ...
gagnant = np.empty((0,dim), int)

with open(en_entree, "rt") as f_obj:
    # load gagnantstics
    csv_reader(f_obj)

with open(en_entree_grilles, "rt") as f_obj:
    # load mes grilles
    csv_reader2(f_obj)
    csv_writer(gagnant, en_sortie)

print("--- %s seconds ---" % (time.time() - start_time))

