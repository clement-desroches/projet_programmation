

from needleman_wunsch import Ruler
import sys

if __name__ == "__main__":
    # permet d'executer bundle lorsqu'il est dans le script, pas lors de l'imp
    fichier_path = sys.argv[1] # stock DATASET
    with open(fichier_path , 'r') as fichier :
       chaines = []
       num_example = 1
       for ligne in fichier.readlines():
            if ligne != "\n": # un mot est donc present à la ligne
                if ligne[-1] == "\n":
                    chaine = ligne[:-1] # le mot sans la tabulation
                    chaines.append(chaine)
            if len(chaines) == 2: # le couple est formé, on peut faire la 
                                  # comparaison
                ruler = Ruler(chaines[0], chaines[1]) # on crée la comparaison
                chaines = []
                print("===== Exemple # {} - distance = {}".format(num_example, 
ruler.distance))
                print(ruler.top)
                print(ruler.bottom)
                num_example += 1
                
# La limite de cet algorithme est qu'il affichera tous les exemples d'un coup,
# si le Dataset comporte beaucoup de couples, il sera difficle de retrouver un
# exemple en particulier, il serait juducieux de soit implémenter un 
# imput() à la fin de chaque tour de boucle, soit de stocker sous forme
# de dictionnaire ou liste l'ensemble des exemples traités par Ruler et 
# d'imprimer uniquement l'exemple demander par l'utilisateur.