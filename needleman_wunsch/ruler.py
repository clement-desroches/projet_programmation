



from colorama import Fore, Style
import numpy as np

def red_text(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"
    

class Ruler : 
    """ classe suivant l'algorithme de needelman-wunsch pour créer l'alignement
    de 2 chaines de caractères """
    
    def __init__(self, chaine1, chaine2):
        """ intialise les variables de la classe
        entrees :
        chaine1 : première chaine de caractères (type : str)
        chaine2 : deuxième chaine de caractères (type : str)  """
        
        self.chaine1 = chaine1
        self.chaine2 = chaine2
        self.top = ""
        self.bottom = ""
        self.distance = 0
    
    def compute(self):
        """ realise le calcul de l'alignement 
        calcul de la distance entre les deux chaines de caractère et
        et construction de l'affichage des différences """
        
        shape = (len(self.chaine1) + 1, len(self.chaine2) + 1)
      
        M = np.zeros(shape) # création de la matrice de similitude
        
        for i in range(1, shape[0]):
            M[i,0] = i
       
        for i in range(1, shape[1]):
            M[0,i] = i
            
        for i in range(1, shape[0]):
            for j in range(1, shape[1]):
                a = M[i-1,j-1] + int(self.chaine1[i-1] != self.chaine2[j-1])
                b = M[i-1,j] + 1
                c = M[i,j-1] + 1
                M[i,j] = min(a, b, c)
        # modification de la matrice de similitude
        
        self.distance = M[-1,-1]
        
        i, j = shape[0] - 1, shape[1] - 1
       
        while i > 0 or j > 0:
            if i == 0:
                self.top    += self.chaine1[:i][::-1]
                self.bottom += red_text(i*'=')[::-1]
                break
            if j == 0: 
                self.top    += red_text(j*'=')[::-1]
                self.bottom += self.chaine2[:j][::-1]
                break
            
            minimum = min(M[i-1,j-1], M[i,j-1], M[i-1,j])
            
            if M[i-1,j-1] == minimum:
                i -= 1
                j -= 1
                if self.chaine1[i] == self.chaine2[j]:
                    self.top    += self.chaine1[i]
                    self.bottom += self.chaine2[j]
                else:
                    self.top    += red_text(self.chaine1[i])[::-1]
                    self.bottom += red_text(self.chaine2[j])[::-1]
            elif M[i-1,j] == minimum:
                i -= 1
                self.top    += self.chaine1[i]
                self.bottom += red_text('=')[::-1]
            elif M[i,j-1] == minimum:
                j -= 1
                self.top    += red_text('=')[::-1]
                self.bottom += self.chaine2[j]
            # construction de l'affichage des différences pas à pas
            
            self.top    = self.top[::-1]
            self.bottom = self.bottom[::-1]
       
        return 0
    
    def report(self):
        return self.top, self.bottom
    
    
    
# on crée un objet pour mesurer 
# la distance entre deux chaines
ruler = Ruler("abcdefghi", "abcdfghi")

# on impose à l'utilisateur de la classe 
# de lancer explicitement le calcul
ruler.compute()

# on obtient la distance
print(ruler.distance)

# et pour afficher les différences
top, bottom = ruler.report()
print(top)
print(bottom)
  
    
