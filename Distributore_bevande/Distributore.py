import pygame

class Distributore:
    x = 0
    y = 0
    stato = 0
    annulla = False
    moneta_inserita = False
    image =""
    messaggio =""
    run = True
    
    tempo_moneta = 3000 #3secondi
    tempo_erogazione = 6000#4 secondi
    n_coca = 4
    n_acqua = 4
    n_kitkat = 4
    
    
    #ingressi      
    i_pulsanti = {"pM":False,"p1":False,"p2":False,"p3":False,"pA":False,"pR":False}
    colore_stato = (0,255,0)#rappresentazione RGB
    #uscite
    o_prodotto = {"out_coca":False,"out_acqua":False,"out_kitkat":False,"out_moneta":False}
    
    def __init__(self, x, y,stato,colore_stato, image):
        self.x = x
        self.y = y
        self.stato = stato
        self.colore_stato = colore_stato
        self.image = image
        
    def sposta(self, x, y):
        self.x = x
        self.y = y
               
    def disegna(self,schermo, imageD, imageC, imageA, imageK, imageM, colore_stato):
        schermo.fill(colore_stato)
        schermo.blit(imageD, (self.x, self.y))

        for i in range(4):
            schermo.blit(imageC, (55+(i*40),159))
            schermo.blit(imageA, (55+(i*40),224))
            schermo.blit(imageK, (55+(i*40),295))
        if (self.moneta_inserita == True) or (self.o_prodotto["out_moneta"] == True) :
            schermo.blit(imageM, (270,350))
        elif self.o_prodotto["out_coca"] == True:
            schermo.blit(imageC, (300,350)) 
        elif self.o_prodotto["out_acqua"] == True:
            schermo.blit(imageA, (300,350))
        elif self.o_prodotto["out_kitkat"] == True:
            schermo.blit(imageK, (300,350)) 
            
        pygame.display.update()
    
    def gestioneProdotto(self, o_prodotto):
        self.o_prodotto["out_coca"] = o_prodotto[0]
        self.o_prodotto["out_acqua"] = o_prodotto[1]
        self.o_prodotto["out_kitkat"] = o_prodotto[2]
        self.o_prodotto["out_moneta"] = o_prodotto[3]
    
    def stampa(self,messaggio):
        self.messaggio = messaggio
        print(self.messaggio)
        pygame.display.set_caption(self.messaggio)
        
        
def leggi_ingressi():
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.unicode == "q": #quit
                print("il tasto premuto risulta " , evento.unicode)
                distributore.run = False
                
            if evento.unicode == "m": #inserimento moneta
                print("Inserita moneta da 1 euro")
                distributore.i_pulsanti["pM"] = True
                
            if evento.unicode == "1": #selezionata  coca cola
                print("selezionata la bevanda coca cola")
                distributore.i_pulsanti["p1"] = True

            if evento.unicode == "2": #selezionata  acqua
                distributore.i_pulsanti["p2"] = True
                
            if evento.unicode == "3": #selezionato kitkat
                distributore.i_pulsanti["p3"] = True
                
            if evento.unicode == "a": #selezionato annulla operazione
                distributore.i_pulsanti["pA"] = True

            if evento.unicode == "r": #selezionato restituzione moneta
                distributore.i_pulsanti["pR"] = True
        
pygame.init()#inizializzazione

pygame.display.set_caption("Distributore bevande e snack")#scriviamo il titolo sulla finestra
schermo = pygame.display.set_mode( (800,700))#schermo ad 800 x 600 pixel

immagineD = pygame.image.load("image/distributore.png")
immagineM = pygame.image.load("image/moneta.png")
immagineC = pygame.image.load("image/coca.png")
immagineA = pygame.image.load("image/acqua.png")
immagineK = pygame.image.load("image/kitkat.png")

distributore = Distributore( 0,0,0,(0,255,0), immagineD)#creato il distributore in memoria
distributore.disegna(schermo, immagineD,immagineC,immagineA,immagineK,immagineM,(0,255,0))

lettura_orologio = 0
orologio = 0
distributore.run = True

while distributore.run:
    orologio = pygame.time.get_ticks()#tempo scandito in millisecondi
    #print(orologio)
    leggi_ingressi()
               
    if distributore.stato == 0: #stato 0, piano terra
        #cosa si deve fare nello stato 0, una volta sola
        if distributore.messaggio =="":
            distributore.stampa("stato 0, distributore in attesa inserimento moneta")
            distributore.gestioneProdotto((False,False,False, False))#Distributore in attesa
            distributore.disegna(schermo, immagineD,immagineC,immagineA,immagineK,immagineM,(0,255,0))

        
        #cosa produce il cambiamneto di stato, inserisco la moneta
        if distributore.i_pulsanti["pM"] == True:
            distributore.i_pulsanti["pM"] = False
            distributore.moneta_inserita = True
            distributore.stampa("inserita la moneta")
            distributore.disegna(schermo, immagineD,immagineC,immagineA,immagineK,immagineM,(0,255,0))
            distributore.gestioneProdotto((False,False,False, False))
            lettura_orologio = orologio
            distributore.messaggio = "inserita_moneta"
            
        #cambiamento di stato dopo un intervallo di tempo
        if (distributore.messaggio=="inserita_moneta") :
            if orologio > lettura_orologio + distributore.tempo_moneta :
                distributore.stato = 1
                print("vado nello stato 1")
                distributore.messaggio =""
                distributore.moneta_inserita = False
            
    elif distributore.stato == 1:
        #cosa si deve fare nello stato 1, attesa selezione
        if distributore.messaggio =="":
            distributore.stampa("stato 1, attesa selezione")           
            distributore.disegna(schermo, immagineD,immagineC,immagineA,immagineK,immagineM,(255,255,0))
            distributore.gestioneProdotto((False,False,False, False))
            lettura_orologio = orologio
            distributore.messaggio = "attesa selezione"
            
        #cosa fare per cambiare stato 
        if distributore.i_pulsanti["p1"] == True:
            distributore.i_pulsanti["p1"] = False
            distributore.stato = 2
            print("stato selezione coca")
            distributore.messaggio =""
            
        if distributore.i_pulsanti["p2"] == True:
            distributore.i_pulsanti["p2"] = False
            distributore.stato = 3
            print("stato selezione acqua")
            distributore.messaggio =""
     
        if distributore.i_pulsanti["p3"] == True:
            distributore.i_pulsanti["p3"] = False
            distributore.stato = 4
            print("stato selezione kitkat")
            distributore.messaggio =""

        if distributore.i_pulsanti["pR"] == True:
            distributore.i_pulsanti["pR"] = False
            distributore.stato = 5
            print("stato restituzione moneta")
            distributore.messaggio =""

    elif distributore.stato == 2:
        #cosa si deve fare nello stato 1, attesa selezione
        if distributore.messaggio =="":
            distributore.stampa("stato 2, selezionato coca cola")
            distributore.gestioneProdotto((True,False,False, False))
            distributore.disegna(schermo, immagineD,immagineC,immagineA,immagineK,immagineM,(255,0,0))

            lettura_orologio = orologio
            distributore.messaggio = "scelta_coca"
            
        #cambiamento di stato dopo un intervallo di tempo
        if (distributore.messaggio=="scelta_coca") :
            if orologio > lettura_orologio + distributore.tempo_erogazione :
                distributore.stato = 0
                print("vado nello stato 0")
                distributore.messaggio =""
                
    elif distributore.stato == 3:
        #cosa si deve fare nello stato 3, selezione acqua
        if distributore.messaggio =="":
            distributore.stampa("stato 3, selezionato acqua")
            distributore.gestioneProdotto((False,True,False, False))
            distributore.disegna(schermo, immagineD,immagineC,immagineA,immagineK,immagineM,(0,0,255))
            lettura_orologio = orologio
            distributore.messaggio = "scelta_acqua"
            
        #cambiamento di stato dopo un intervallo di tempo
        if (distributore.messaggio=="scelta_acqua") :
            if orologio > lettura_orologio + distributore.tempo_erogazione :
                distributore.stato = 0
                print("vado nello stato 0")
                distributore.messaggio =""

    elif distributore.stato == 4:
        #cosa si deve fare nello stato 4, selezione kitkat
        if distributore.messaggio =="":
            distributore.stampa("stato 3, selezionato kitkat")
            distributore.gestioneProdotto((False,False,True, False))
            distributore.disegna(schermo, immagineD,immagineC,immagineA,immagineK,immagineM,(125,125,0))
            lettura_orologio = orologio
            distributore.messaggio = "scelta_kitkat"
            
        #cambiamento di stato dopo un intervallo di tempo
        if (distributore.messaggio=="scelta_kitkat") :
            if orologio > lettura_orologio + distributore.tempo_erogazione :
                distributore.stato = 0
                print("vado nello stato 0")
                distributore.messaggio =""

    elif distributore.stato == 5:
        #cosa si deve fare nello stato 5, restituzione moneta
        if distributore.messaggio =="":
            distributore.stampa("stato 5, restituzione moneta")
            distributore.gestioneProdotto((False,False,False, True))
            distributore.disegna(schermo, immagineD,immagineC,immagineA,immagineK,immagineM,(255,0,255))
            lettura_orologio = orologio
            distributore.messaggio = "restituzione_moneta"
            
        #cambiamento di stato dopo un intervallo di tempo
        if (distributore.messaggio=="restituzione_moneta") :
            if orologio > lettura_orologio + distributore.tempo_moneta :
                distributore.stato = 0
                print("vado nello stato 0")
                distributore.messaggio =""

pygame.quit()

           