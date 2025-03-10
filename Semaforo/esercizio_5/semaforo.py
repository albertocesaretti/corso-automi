import pygame

class Semaforo:
    x = 0
    y = 0
    stato = 0
    sensore = "g" #ingresso
    luce_emessa = (0,255,0)#rappresentazione RGB
    #tempi accensione
    tempo_verde = 10000 #millisecondi
    tempo_giallo = 4000 #millisecondi
    tempo_rosso = 10000 #millisecondi
    
    def __init__(self, x, y,stato,sensore,luce_emessa, image):
        x = x
        y = y
        stato = stato
        sensore = sensore
        luce_emessa = luce_emessa
        image = image
        
    def sposta(self, x, y):
        self.x = x
        self.y = y
    
    def disegna(self,schermo, image, luce_emessa):
        schermo.fill(luce_emessa)
        schermo.blit(image, (self.x, self.y))
        pygame.display.update()
        
        
    

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
#semaforo.disegna(schermo, immagineV, (0,255,0))

messaggio =""
lettura_orologio = 0
notte = False

orologio = 0

run = True
while run:
    orologio = pygame.time.get_ticks()#tempo scandito in millisecondi
    #print(orologio)
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.unicode == "q": #quit
                print("il tasto premuto risulta " , evento.unicode)
                run = False
            if evento.unicode == "n": #quit
                print("sensore notte")
                notte = True
            if evento.unicode == "g": #quit
                print("sensore giorno")
                notte = False
                
    if semaforo.stato == 0: #stato 0, funzionamento luce verde
        #cosa si deve svolgere, una volta sola
        if messaggio =="":
            messaggio = "Stato 0, funzionamento luce verde"
            print(messaggio)
            semaforo.disegna(schermo, immagineV, (0,255,0)) #vedo il semaforo verdesullo schermo
            lettura_orologio = orologio
        
        #cosa produce il cambiamneto di stato, passerà nello stato 1 luce gialla
        if orologio > lettura_orologio + semaforo.tempo_verde:
            print("sono passati 10 secondi")
            if notte == True:    
                semaforo.stato = 3 # luce lampeggiante
            else:
                semaforo.stato = 1
            messaggio =""

    elif semaforo.stato == 1: #stato luce gialla
        #cosa si deve svolgere, una volta sola
        if messaggio =="":
            messaggio = "Stato 1, funzionamento luce gialla"
            print(messaggio)
            semaforo.disegna(schermo, immagineG, (255,255,0)) #vedo il semaforo verdesullo schermo
            lettura_orologio = orologio
        
        #cosa produce il cambiamneto di stato, passerà nello stato 1 luce gialla
        if orologio > lettura_orologio + semaforo.tempo_giallo:
            print("sono passati 4 secondi")
            if notte == True:    
                semaforo.stato = 3 # luce lampeggiante
            else:
                semaforo.stato = 2
            messaggio =""

            
    elif semaforo.stato == 2: #stato luce rossa
        #cosa si deve svolgere, una volta sola
        if messaggio =="":
            messaggio = "Stato 2, funzionamento luce rossa"
            print(messaggio)
            semaforo.disegna(schermo, immagineR, (255,0,0)) #vedo il semaforo verdesullo schermo
            lettura_orologio = orologio
        
        #cosa produce il cambiamneto di stato, passerà nello stato 1 luce gialla
        if orologio > lettura_orologio + semaforo.tempo_rosso:
            print("sono passati 10 secondi") 
            if notte == True:    
                semaforo.stato = 3 # luce lampeggiante
            else:
                semaforo.stato = 0 #luce verde
            messaggio =""
    elif semaforo.stato == 3: #stato luce lampeggiante ( luce blue)
        #cosa si deve svolgere, una volta sola
        if messaggio =="":
            messaggio = "Stato 3, funzionamento luce lampeggiante (blue)"
            print(messaggio)
            semaforo.disegna(schermo, immagineL, (0,0,255)) #vedo il semaforo verdesullo schermo
            lettura_orologio = orologio
        
        #cosa produce il cambiamneto di stato, passerà nello stato 1 luce gialla
        if notte == False: 
            semaforo.stato = 1 #luce gialla
            messaggio =""        
  
            
        
pygame.quit()
                