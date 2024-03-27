# Nuit du c0de 2023
import pyxel

def tram():
    
    
    partie = Jeu()
    
    partie_lancee = False
    
    pyxel.init(256, 128, title="Nuit du c0de")
        
    pyxel.load("theme.pyxres")
    pyxel.run(partie.update, partie.draw)
    
    while partie_lancee == False:
        pyxel.mouse(True)
    
    
    
    
    
class Joueur():
    def __init__(self, couleur):
        self.x=40
        self.y=40
        self.couleur = couleur
        self.perso = None #1,2 ou 3 en fonction de quel personnage
        self.vie = 100 #100%
        self.endurance = 100 #100%
       
    def choix_perso(self):
        self.perso == ""

class Jeu():
    def __init__(self):
        self.joueur1 = Joueur("rouge")
        self.joueur2 = Joueur("bleu")
        
    def joueur_deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.joueur1.x<240:
            self.joueur1.x += 2
        if pyxel.btn(pyxel.KEY_LEFT) and self.joueur1.x>0:
            self.joueur1.x += -2
        if pyxel.btn(pyxel.KEY_DOWN) and self.joueur1.y<52:
            self.joueur1.y += 2
        if pyxel.btn(pyxel.KEY_UP) and self.joueur1.y>0:
            self.joueur1.y += -2
            
        if pyxel.pget(self.joueur1.x+12,self.joueur1.y+16)!=4 and pyxel.pget(self.joueur1.x+4,self.joueur1.y+16)!=4:
            self.joueur1.y += 1
            
            
            
            
            
        
        if pyxel.btn(pyxel.KEY_D) and self.joueur2.x<240:
            self.joueur2.x += 2
        if pyxel.btn(pyxel.KEY_Q) and self.joueur2.x>0:
            self.joueur2.x += -2
        if pyxel.btn(pyxel.KEY_S) and self.joueur2.y<52:
            self.joueur2.y += 2
        if pyxel.btn(pyxel.KEY_Z) and self.joueur2.y>0:
            self.joueur2.y += -2
            
        if pyxel.pget(self.joueur2.x+12,self.joueur2.y+16)!=4 and pyxel.pget(self.joueur2.x+4,self.joueur2.y+16)!=4:
            self.joueur2.y += 1
        
    
    def joueur_coup(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if self.joueur2.x <= self.joueur1.x+16 and self.joueur2.y <= self.joueur1.y+16 and self.joueur2.x+16 >= self.joueur1.x and self.joueur2.y+16 >= self.joueur1.y:
                self.joueur2.vie-=1
            
        if pyxel.btn(pyxel.KEY_SPACE):
            if self.joueur1.x <= self.joueur2.x+16 and self.joueur1.y <= self.joueur2.y+16 and self.joueur1.x+16 >= self.joueur2.x and self.joueur1.y+16 >= self.joueur2.y:
                self.joueur1.vie-=1
            
    
    def update(self):
        """mise à jour des variables (30 fois par seconde)"""

        self.joueur_deplacement()
        self.joueur_coup()
        
    
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)
        pyxel.blt(0,0,0,0,32,256,128)
        
        pyxel.blt(240,114,0,145,16,158,28,13)
        
        
        if self.joueur2.vie>75:
            pyxel.blt(0,114,0,0,16,14,25,13)
        if self.joueur2.vie<=75:
            pyxel.blt(0,114,0,16,16,14,25,13)
        if self.joueur2.vie<=50:
            pyxel.blt(0,114,0,32,16,14,25,13)
        if self.joueur2.vie<=25:
            pyxel.blt(0,114,0,48,16,14,25,13)
        if self.joueur2.vie<=0:
            pyxel.blt(0,114,0,64,16,14,25,13)
            
        if self.joueur1.vie>75:
            pyxel.blt(240,114,0,145,16,158,28,13)
        if self.joueur1.vie<=75:
            pyxel.blt(240,114,0,81,16,158,28,13)
        if self.joueur1.vie<=50:
            pyxel.blt(240,114,0,97,16,158,28,13)
        if self.joueur1.vie<=25:
            pyxel.blt(240,114,0,113,16,158,28,13)
        if self.joueur1.vie<=0:
            pyxel.blt(240,114,0,129,16,158,28,13)
            
            
            
        
        #print(self.joueur1.vie)
        
        
        # Skin des joueurs
        pyxel.blt(self.joueur1.x, self.joueur1.y, 0, 176, 0, 16, 16, 13)
        
        pyxel.blt(self.joueur2.x, self.joueur2.y, 0, 192, 0, 16, 16, 13)
        
tram()