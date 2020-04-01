

class BinaryTree () :
    """ Accès aux informations sur l'arbre binaire """
    
    def __init__(self, racine = None, lettres = []):
        """ initialise la classe Binary_tree
        entrées :
            racine : racine de l'arbre binaire (type = Node) 
            lettres : ensemble des lettres présentes dans l'arbre (type = list) 
        """
        self.racine = racine
        self.lettres = lettres
        
    def chemin_binaire(self, nom) : 
        """ Renvoie le chemin binaire associé à nom 
        entrées :
            nom : lettre dont on cherche le chemin (type = str) 
        sorties :
            chemin : représentation binaire de nom par le codage de Huffman
            (type = str)
        """
        node = self.racine
        chemin = ""
        while node.nom != nom :
            if nom in node.prochain_droite.nom :
                node = node.prochain_droite
                chemin += "1"
            else :
                node = node.prochain_gauche
                chemin += "0"
        return chemin
            
            

            
            
class Node() :
    """ Informations sur le noeud de l'arbre """
    
    def __init__(self, prochain_droite = None, prochain_gauche = None, nom = None):
        """ Initialise la classe Node
        entrées :
            prochain_droite : noeud suivant à droite (type = Node)
            prochain_gauche : noeud suivant à gauche (type = Node)
            nom : chaine de caractère mié au noeud (type = str)
        """
        self.prochain_droite = prochain_droite
        self.prochain_gauche  = prochain_gauche
        self.nom = nom
        self.end = self.prochain_gauche == self.prochain_droite == None
        




class TreeBuilder():
    """ Construction de l'arbre pour le mot """
    def __init__(self, texte):
        """ Initialise la classe TreeBuilder
        entrées : 
            texte : texte dont on va construire l'arbre (type = str) 
        """
        self.texte = texte
        
    def tree(self):
        """construction de l'arbre associé au mot
        entrées :
            self : 
        """
        lettres = list(set(self.texte)) # toutes les lettres sans doublons
        frequence = {lettre : self.texte.count(lettre)/len(self.texte) for lettre in lettres}
        key = lambda i : frequence[i]
        lettres = sorted(lettres, key = key) # liste triée des lettres composant le mot
        noeuds = [Node(nom = lettre) for lettre in lettres] 
        
        while len(noeuds) > 1 :
            noeud1, noeud2 = noeuds[0], noeuds[1]
            del noeuds[0]
            noeuds[0] = Node(nom = noeud1.nom + noeud2.nom, prochain_gauche = noeud1, prochain_droite = noeud2)
            frequence[noeuds[0].nom] = frequence[noeud1.nom] + frequence[noeud2.nom]
            i = 0
            while i < len(noeuds) - 1 and frequence[noeuds[i].nom] >= frequence[noeuds[i+1].nom]:
                noeuds[i], noeuds[i+1] = noeuds[i+1], noeuds[i]
                i += 1
       
        return BinaryTree(noeuds[0], lettres)
    
    
    
class Codec():
    """ codage des mots et decodage d'un arbre"""
    
    def __init__(self, tree):
        self.tree = tree
        
    def encode(self, text):
        codage = ""
        for lettre in text :
            codage += self.tree.chemin_binaire(lettre)
        return codage

        
    def decode(self, codage):
        mot = ""
        noeud = self.tree.racine
        for chiffre in codage :
            if chiffre == '1' :
                noeud = noeud.prochain_droite
            else :
                noeud = noeud.prochain_gauche
            
            if noeud.end:
                mot += noeud.nom
                noeud = self.tree.racine
                    
        return mot
       
        
    

text = "a dead dad ceded a bad babe a beaded abaca bed"

# on analyse les fréquences d'occurrence dans text
# pour fabriquer un arbre binaire
builder = TreeBuilder(text)
binary_tree = builder.tree()


# on passe l'arbre binaire à un encodeur/décodeur
codec = Codec(binary_tree)
# qui permet d'encoder
encoded = codec.encode(text)
# et de décoder
decoded = codec.decode(encoded)
# si cette assertion est fausse il y a un gros problème avec le code
assert text == decoded

# on affiche le résultat
print(f"{text}\n{encoded}")
if decoded != text:
    print("OOPS")
            
    

            
            
            
    