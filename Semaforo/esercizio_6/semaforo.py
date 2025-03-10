import pygame

class Semaforo:
    x = 0
    y = 0
    stato = 0
    sensore = "g" #ingresso
    notte = False
    luce_emessa = (0,255,0)#rappresentazione RGB
    tempoVerde = 10000 #millisecondi
    tempoGiallo = 4000 #millisecondi
    tempoRosso = 10000 #millisecondi
    messaggio = ""
    run = True
    
    def __init__(self, x, y,stato,sensore,luce_emessa, image):
        self.x = x
        self.y = y
        self.stato = stato
        self.sensore = sensore
        self.luce_emessa = luce_emessa
        self.image = image
        
    def sposta(self, x, y):
        self.x = x
        self.y = y
    
    def disegna(self,schermo, image, luce_emessa):
        schermo.fill(luce_emessa)
        schermo.blit(image, (self.x, self.y))
        pygame.display.update()
        
    def stampa(self, messaggio):
        self.messaggio = messaggio
        print(messaggio)
        pygame.display.set_caption(messaggio)

def letturaIngressi(semaforo):
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.unicode == "q":
                semaforo.run = False
            if evento.unicode == "n":
                semaforo.notte = True
            if evento.unicode == "g":
                semaforo.notte = False


pygame.init()#inizializzazione

pygame.display.set_caption("Semaforo")#scriviamo il titolo sulla finestra

schermo = pygame.display.set_mode( (800,600))#schermo ad 800 x 600 pixel
schermo.fill( (0,255,0))#coloriamo lo sfondo di rosso

immagineV = pygame.image.load("image/semaforoVerde.png")#caricato in memoria
immagineG = pygame.image.load("image/semaforoGiallo.png")#caricato in memoria
immagineR = pygame.image.load("image/semaforoRosso.png")#caricato in memoria
immagineL = pygame.image.load("image/semaforoLampeggiante.png")#caricato in memoria

semaforo = Semaforo( 0, 0,0,"g",(0,255,0), immagineV)#creato il semaforo in memoria
semaforo.sposta(100,50)
semaforo.disegna(schermo, immagineV, (0,255,0)) #vedo il semaforo sullo schermo


orologio = 0
lettura_orologio = 0


while semaforo.run:
    orologio = pygame.time.get_ticks()#tempo scandito in millisecondi
    
    letturaIngressi(semaforo)
    
    if semaforo.stato == 0: #stato 0 luce verde
        #cosa fare in uno stato, svolge questa cosa una volta solo
        if semaforo.messaggio == "":
            semaforo.messaggio = "Siamo nello stato 0, luce verde"
            semaforo.stampa(semaforo.messaggio)
            semaforo.disegna(schermo,immagineV,(0,255,0))
            lettura_orologio = orologio
            
        #cosa produce un cambiamento di stato, stato 1 luce gialla
        if orologio > lettura_orologio + semaforo.tempoVerde:
            print("sono passati 10 secondi")
            if semaforo.notte == True:
                semaforo.stato = 3	#luce lampeggiante
                semaforo.messaggio =""
            else:
                semaforo.stato = 1 #luce gialla
                semaforo.messaggio =""
    
    elif semaforo.stato == 1: #stato 0 luce gialla
        #cosa fare in uno stato, svolge questa cosa una volta solo
        if semaforo.messaggio == "":
            semaforo.messaggio = "Siamo nello stato 1, luce gialla"
            semaforo.stampa(semaforo.messaggio)
            semaforo.disegna(schermo,immagineG,(255,255,0))
            lettura_orologio = orologio
            
        #cosa produce un cambiamento di stato, stato 1 luce gialla
        if orologio > lettura_orologio + semaforo.tempoGiallo:
            print("sono passati 4 secondi")
            if semaforo.notte == True:
                semaforo.stato = 3	#luce lampeggiante
                semaforo.messaggio =""
            else:
                semaforo.stato = 2 #luce rossa
                semaforo.messaggio =""
                
    elif semaforo.stato == 2: #stato 0 luce rossa
        #cosa fare in uno stato, svolge questa cosa una volta solo
        if semaforo.messaggio == "":
            semaforo.messaggio = "Siamo nello stato 2, luce rossa"
            semaforo.stampa(semaforo.messaggio)
            semaforo.disegna(schermo,immagineR,(255,0,0))
            lettura_orologio = orologio
            
        #cosa produce un cambiamento di stato, stato 1 luce gialla
        if orologio > lettura_orologio + semaforo.tempoRosso:
            print("sono passati 10 secondi")
            if semaforo.notte == True:
                semaforo.stato = 3	#luce lampeggiante
                semaforo.messaggio =""
            else:
                semaforo.stato = 0 #luce rossa
                semaforo.messaggio =""

    elif semaforo.stato == 3: #stato 3 luce lampeggiante
        #cosa fare in uno stato, svolge questa cosa una volta solo
        if semaforo.messaggio == "":
            semaforo.messaggio = "Siamo nello stato 3, luce lampeggiante"
            semaforo.stampa(semaforo.messaggio)
            semaforo.disegna(schermo,immagineL,(0,0,255))
            lettura_orologio = orologio
            
        #cosa produce un cambiamento di stato, stato 1 luce gialla
        if semaforo.notte == False:
            semaforo.stato = 1
            semaforo.messaggio =""

pygame.quit()
                