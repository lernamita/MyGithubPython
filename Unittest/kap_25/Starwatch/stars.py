# ----------------------------------------------------
# Dateiname:  stars.py
# Modul mit Klassen Star und Sky zur Reprsesentation
# eines Sternenhimmels
# Stern es un conjunto de puntos claros (hellen Punkten)
# al inicio contiene una estrella un punto de luz, que es una coordenada de x
# y las y de la imagen, y se las graba en una lista llamada _dots
# en la funcion integrate de star se toma una coordenada y se evalua si se encu
# -encuentra como vecina de una estrella ya registrada en la lista dots
# en caso de ser asi, se la considera la misma estrella que existe en dots y de
# ser en caso false esa coordenada no es vecina de nadie y se la deja como esta
# existe un umbral de brillantez 200, que define que desde
# ese valor en adelante se considera un punto de luz de la
# fotografia como una estrella (zu einem Stern gehören)
# Brillantez o Helligkeit es la suma de RGB
# dotlist = lighdots es lo que retorna la funcion search y
# representa las estrellas reconocidas dentro de una imagen que se cargo
# la funcion createstar de Sky integra poco a poco estas estrellas de
# la imagen en una lista de estrellas definitivas llamada stars siempre y cuand
# pasen la prueba de la funcion integrate de Star,que basicamente prueba
# que cada estrella identificada de la imagen no este repetida o ya identificad
# si los puntos de luz de la imagen (Lichpunkte) corresponden ya a una estrella
# se devuelve True y se la agrega a la lista definitiva star
# sino da False y no se toca la estrela nueva y no se la agrega
# la estrella nueva

# Python 3
# Kap. 25
# Michael Weigend 08.06.2019
# ---------------------------------------------------
# stars.py
class Star(object):
  """ modelliert einen Stern"""
  def __init__(self, dot):
        self.__dots = [dot]                           #1 list of tupel inicializado, la estrella contiene solo un punto de luz que es un
                                                        # par de x y de la foto o imagen

  def integrate (self, dot):                          #2 funcion que prueba si el dot o punto de luz corresponde o es a una estrella
    x, y = dot                                        # inicializas la funcion x y del tupel que recibes de la imagen
    r = 2                                             # 2 es la distancia maximo de punto a punto de la estrella
    for (x0, y0)  in self.__dots:
        if (x0-r <= x <= x0+r) and (y0-r <= y <= y0+r): # si el lichpunkt objeto se encuentra a menos de 2 unidades de distancia unidades las coordinadas
          self.__dots.append(dot)                     #3 entonces se delcara correcta la correspondencia del punto de luz a la estrella, si se encuentra fuera de ese rango no es pasa nada la deja como es
          return True                               
    return False                                      #4 la estrella es nueva y no pasa nada

class Sky(object):
  """ Modelliert einen Sternenhimmel"""
  def __init__ (self, image):
    self.threshold = 200                              #5 se define el umbral de brillantez para se considerada una estrella
    self.image = image
    lightdots = self.__search()                         # lightdots es dotlist y son todas las estrellas encontradas en la imagen
    self.__createStars(lightdots)                       # createstars de esos lightdots crean la lista definitiva de estrellas _stars

  def __brightness (self, pixel):
    a =  pixel[0]
    b =  pixel[1]
    c =  pixel[2]                                     #6 el pixel recibido son tres decimales que vienen de get() y se los suman
    return a + b + c

  def __createStars(self, lightdots):
    self.__stars = []
    for p in lightdots:                               #7 se inicializa la lista definitiva y se llama a comprobar la no duplicidad de coordenada
      self.__integrate(p)
      
  def __integrate (self, lightdot):                   #8 se hace la prueba de duplicidad de las coordenadas o pixeles de la lista definitiva _stars
      for star in self.__stars:
        if star.integrate(lightdot): return  
      self.__stars.append (Star(lightdot))            #9  Si la coordenada se encuentra en la lista de estrellas no pasa nada caso contrario se genera un nuevo elemento de la lista 
  
  def __search (self):                                #10 
    dotlist =[] 
    for x in range(self.image.width()):             # se recorre todas las filas de la imagen con un indice x
      for y in range(self.image.height()):          # se recorre toda las columnas de la imagen con un indice y
        brightness = self.__brightness(self.image.get(x, y))
        if brightness > self.threshold:
          dotlist.append((x,y))
    return dotlist                                  # retorna la lista solo con los elementos que son estrellas

  def count(self):
    return len(self.__stars)

# Testen 
if __name__ == "__main__":                            #11
    import profile, tkinter 
    window = tkinter.Tk()                             #12             
    image = tkinter.PhotoImage(file="bilder/wagen.gif" )                   
    profile.run("stars = Sky(image)")                 #13

