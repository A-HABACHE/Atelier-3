class Vecteur2D:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def affichage(self):
        print("x = ",self.x," y = ",self.y) 

    def surcharge(self,v):
        return Vecteur2D(self.x+v.x,self.y+v.y)

#instanciation sans paramètres:
v1=Vecteur2D()
print("Vecteur sans paramètres: ","x=",v1.x," y=",v1.y) 
#instanciation sans parame=ètres:
v2=Vecteur2D(3,5)
print("Vecteur avec paramètres: ","x= ",v2.x," y= ",v2.y)
#affichage et addition de deux vecteurs
v2.affichage()
v3=Vecteur2D(13,7)
v3.affichage()
v3.surcharge(v2).affichage()

class Rectangle:
    def __init__(self,longueur,largeur,nom="rectangle"):
        self.nom=nom
        self.longueur=longueur
        self.largeur=largeur

    def affichageR(self):
        return self.nom+" : "+" longueur: "+str(self.longueur)+" largeur:"+str(self.largeur)

    def surface(self):
        return self.largeur*self.longueur

class Carre(Rectangle):
    def __init__(self,longueur,largeur):
        super().__init__(longueur,largeur,nom="carré")

#instanciation d'un rectangle et un carré avec affichage
r1=Rectangle(5,2)
c1=Carre(2,2)
print(r1.affichageR())
print(c1.affichageR())

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

class Segment(Point):
    def __init__(self,x1,y1,x2,y2):
        self.orig=Point(x1,y1)
        self.extrem=Point(x2,y2)

    def affichageS(self):
        return str(self.orig.x),str(self.orig.y),str(self.extrem.x),str(self.extrem.y)

s1=Segment(1,2,3,4)
print("Le segment est:",s1.affichageS()) 