import pygame

class Semaforo:
    x = 0
    y = 0
    stato = 0
    sensore = "g" #ingresso
    luce_emessa = (0,255,0)#rappresentazione RGB
    
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
        
def letturaIngressi(): #lettura tasti della tastiera
    ingresso = 0
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            ingresso = evento.unicode 
    return ingresso
    
            

pygame.init()#inizializzazione

pygame.display.set_caption("Semaforo")#scriviamo il titolo sulla finestra

schermo = pygame.display.set_mode( (800,600))#schermo ad 800 x 600 pixel
schermo.fill( (0,255,0))#coloriamo lo sfondo di rosso

immagineV = pygame.image.load("image/semaforoVerde.png")#caricato in memoria
immagineG = pygame.image.load("image/semaforoGiallo.png")#caricato in memoria
immagineR = pygame.image.load("image/semaforoRosso.png")#caricato in memoria

semaforo = Semaforo( 0, 0,0,"g",(0,255,0), immagineV)#creato il semaforo in memoria
semaforo.sposta(100,50)
semaforo.disegna(schermo, immagineV, (0,255,0)) #vedo il semaforo sullo schermo

#tempi
tempo_luce_verde = 10000 # 10 secondi
tempo_luce_rossa = 10000 # 10 secondi
tempo_luce_gialla = 4000 # 4 secondi

#messaggio nella shell
messaggio =""

#lettura orologio
lettura_orologio = 0

#sensore notturno
notte = False




orologio = 0

run = True
while run:
    orologio = pygame.time.get_ticks()#tempo scandito in millisecondi
    
    #lettura ingressi
    ingresso = letturaIngressi()
    if ingresso == "q": #esco dal programma
        run = False
    if ingresso == "n": #attivato il sensore notturno ed il funzionamento lamp.
        notte = True
    if ingresso == "g": #attivato il sensore giorno
        notte = False
        
    if semaforo.stato == 0: #funzionamento luce verde
        #cosa fare nello stato 0
        if messaggio=="":
            #questo codice viene svolto una volta sola
            messaggio = "semaforo nello stato 0, luce verde"
            print(messaggio)
            semaforo.disegna(schermo, immagineV, (0,255,0)) #vedo il semaforo verde
            lettura_orologio = orologio
        
        #cosa produce un cambiamento di stato,  passo allo stato 1, luce gialla
        # questo controllo viene sempre eseguito
        if orologio > lettura_orologio + tempo_luce_verde :
            semaforo.stato = 1
            messaggio = ""
            print("passati 10 secondi")
    
    elif semaforo.stato == 1:#funzionamento luce gialla
        #cosa fare nello stato 1
        if messaggio=="":
            #questo codice viene svolto una volta sola
            messaggio = "semaforo nello stato 1, luce gialla"
            print(messaggio)
            semaforo.disegna(schermo, immagineG, (255,255,0)) #vedo il semaforo giallo
            lettura_orologio = orologio
        
        #cosa produce un cambiamento di stato,  passo allo stato 2
        if orologio > lettura_orologio + tempo_luce_gialla :
            semaforo.stato = 2
            print("passati 4 secondi")
            messaggio = ""
    
    elif semaforo.stato == 2:#funzionameento luce rossa
        #cosa fare nello stato 1
        if messaggio=="":
            #questo codice viene svolto una volta sola
            messaggio = "semaforo nello stato 2, luce rossa"
            print(messaggio)
            semaforo.disegna(schermo, immagineR, (255,0,0)) #vedo il semaforo giallo
            lettura_orologio = orologio
        
        #cosa produce un cambiamento di stato,  passo allo stato 2
        if orologio > lettura_orologio + tempo_luce_rossa :
            semaforo.stato = 0
            print("passati 10 secondi")
            messaggio = ""
    
  
pygame.quit()
                