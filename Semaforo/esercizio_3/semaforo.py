import pygame

class Semaforo:
    x = 0
    y = 0
    stato = 0
    sensore = "g"
    luce_emessa = (0,255,0)
    
    def __init__(self,x,y,stato,sensore,luce_emessa, image):
            x = x
            y = y
            stato = stato
            sensore = sensore
            luce_emessa = luce_emessa
            image = image
            
    def sposta(self,x,y):
        self.x = x
        self.y = y
        
    def disegna(self,schermo, image, luce_emessa):
        schermo.fill(luce_emessa)
        schermo.blit(image, (self.x,self.y))
        pygame.display.update()#refresh pagina molto,molto importante
                    
pygame.init()#inizializzazione
pygame.display.set_caption("Semaforo")#scriviamo il titolo sulla finestra
schermo = pygame.display.set_mode( (800,600))#schermo ad 800 x 600 pixel

immagineV = pygame.image.load("image/semaforoVerde.png")#caricato in memoria
immagineG = pygame.image.load("image/semaforoGiallo.png")#caricato in memoria
immagineR = pygame.image.load("image/semaforoRosso.png")#caricato in memoria

semaforo = Semaforo(0,0,0,"g",(0,255,0), immagineV)
semaforo.sposta(100,0)
semaforo.disegna(schermo, immagineV,(0,255,0))




    



