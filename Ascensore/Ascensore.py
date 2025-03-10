import pygame

class Ascensore:
    x = 0
    y = 0
    stato = 0
    allarme = False
    image =""
    messaggio =""
    altezza_cabina = 450
    tempo_piano = 8000 #millisecondi
    i_pulsanti = {"pT":False,"p1":False,"p2":False,"pA":False,"pM":False}
    luce_emessa = (0,255,0)#rappresentazione RGB   
    o_motore = {"m_Fermo":True,"m_Su":False,"m_Giu":False}
    
    def __init__(self, x, y,stato,luce_emessa, image):
        self.x = x
        self.y = y
        self.stato = stato
        self.luce_emessa = luce_emessa
        self.image = image
        
    def sposta(self, x, y):
        self.x = x
        self.y = y
               
    def disegna(self,schermo, imageV, imageC, imageA, luce_emessa):
        schermo.fill(luce_emessa)
        schermo.blit(imageV, (self.x, self.y))
        schermo.blit(imageC, (self.x +60, self.y+ self.altezza_cabina))
        if self.allarme == True:
           schermo.blit(imageA, (self.x +60, self.y+ self.altezza_cabina-50))          
        pygame.display.update()
    
    def gestioneMotore(self, o_motore):
        self.o_motore["m_fermo"] = o_motore[0]
        self.o_motore["m_Su"] = o_motore[1]
        self.o_motore["m_Giu"] = o_motore[2]
    
    def stampa(self,messaggio):
        self.messaggio = messaggio
        print(self.messaggio)
        pygame.display.set_caption(self.messaggio)
        
        
def leggi_ingressi():
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            if evento.unicode == "q": #quit
                print("il tasto premuto risulta " , evento.unicode)
                run = False
                
            if evento.unicode == "t": #piano terra
                print("piano terra")
                ascensore.i_pulsanti["pT"] = True
                
            if evento.unicode == "1": #piano 1
                print("piano 1")
                ascensore.i_pulsanti["p1"] = True

            if evento.unicode == "2": #piano 2
                ascensore.i_pulsanti["p2"] = True
                
            if evento.unicode == "a": #piano 2
                ascensore.i_pulsanti["pA"] = True
                
            if evento.unicode == "m": #piano 2
                ascensore.i_pulsanti["pM"] = True
        
pygame.init()#inizializzazione

pygame.display.set_caption("Ascensore")#scriviamo il titolo sulla finestra
schermo = pygame.display.set_mode( (800,700))#schermo ad 800 x 600 pixel

immagineV = pygame.image.load("image/vano.png")#caricato in memoria
immagineC = pygame.image.load("image/cabina.png")#caricato in memoria
immagineA = pygame.image.load("image/campanello.jpg")#caricato in memoria

ascensore = Ascensore( 0,0,0,(0,255,0), immagineV)#creato il semaforo in memoria
ascensore.disegna(schermo, immagineV,immagineC,immagineA,(0,255,0)) 


lettura_orologio = 0
orologio = 0
run = True

while run:
    orologio = pygame.time.get_ticks()#tempo scandito in millisecondi
    #print(orologio)
    leggi_ingressi()
               
    if ascensore.stato == 0: #stato 0, piano terra
        #cosa si deve fare nello stato 0, una volta sola
        if ascensore.messaggio =="":
            ascensore.stampa("stato 0, piano terra")           
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(0,255,0))
            ascensore.gestioneMotore((True,False,True))#motore fermo
        
        #cosa produce il cambiamneto di stato, per passare ai piani, analizzo ingressi
        if ascensore.i_pulsanti["pT"] == True:
            ascensore.stato = 0
            ascensore.i_pulsanti["pT"] = False
         
        # cosa fare per passare in ascensore in allarme
        if ascensore.i_pulsanti["pA"] == True:
            
            ascensore.stato = 3
            ascensore.messaggio = ""
            ascensore.i_pulsanti["pA"] = False
            
        # cosa fare per passare in ascensore in allarme
        if ascensore.i_pulsanti["pM"] == True:
            ascensore.stato = 4
            ascensore.messaggio = ""
            ascensore.i_pulsanti["pM"] = False
            
        # cosa fare nel passare allo stato 1    
        if ascensore.i_pulsanti["p1"]==True:
            ascensore.i_pulsanti["p1"] = False
            
            ascensore.gestioneMotore((False,True,False))#motore in salita
            lettura_orologio = orologio
            ascensore.stampa("acensore in salita verso piano 1, motore su") 
            ascensore.messaggio = "salita1"
            
        if (ascensore.o_motore["m_Su"] == True) and (ascensore.messaggio=="salita1") :
            if orologio > lettura_orologio + ascensore.tempo_piano :
                ascensore.stato = 1
                ascensore.messaggio =""
                        
        if ascensore.messaggio == "salita1":
            ascensore.altezza_cabina -=0.1
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(0,255,0))

        # cosa fare nel passare allo stato 2    
        if ascensore.i_pulsanti["p2"]==True:
            ascensore.i_pulsanti["p2"] = False
            
            ascensore.gestioneMotore((False,True,False))#motore in salita
            lettura_orologio = orologio
            ascensore.stampa("acensore in salita verso piano 2, motore su")
            ascensore.messaggio = "salita2"
            
        if (ascensore.o_motore["m_Su"] == True) and (ascensore.messaggio=="salita2") :
            if orologio > lettura_orologio + ascensore.tempo_piano*2 :
                ascensore.stato = 2
                print("ciao")
                ascensore.messaggio =""
                        
        if ascensore.messaggio == "salita2":
            ascensore.altezza_cabina -=0.1
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(0,255,0))

    elif ascensore.stato == 1:
        #cosa si deve fare nello stato 1, una volta sola
        if ascensore.messaggio =="":
            ascensore.stampa("stato 1, piano primo")           
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(255,255,0))
            ascensore.gestioneMotore((True,False,True))#motore fermo
        
        #cosa produce il cambiamneto di stato, per passare ai piani, analizzo ingressi

            
        # cosa fare nel passare allo stato 1    
        if ascensore.i_pulsanti["p1"]==True:
            ascensore.i_pulsanti["p1"] = False
            ascensore.stato = 1
        
        # cosa fare per passare in ascensore in allarme
        if ascensore.i_pulsanti["pA"] == True:
            ascensore.i_pulsanti["pA"] = False
            ascensore.stato = 3
            ascensore.messaggio = ""

        if ascensore.i_pulsanti["pT"] == True:
            ascensore.i_pulsanti["pT"] = False
            
            ascensore.gestioneMotore((False,False,True))#motore in discesa
            lettura_orologio = orologio
            ascensore.stampa("acensore in discesa verso piano terra, motore giu") 
            ascensore.messaggio = "discesa1"
            
        if (ascensore.o_motore["m_Giu"] == True) and (ascensore.messaggio=="discesa1") :
            if orologio > lettura_orologio + ascensore.tempo_piano :
                ascensore.stato = 0
                ascensore.messaggio =""
                        
        if ascensore.messaggio == "discesa1":
            ascensore.altezza_cabina +=0.1
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(255,255,0))

        # cosa fare nel passare allo stato 2    
        if ascensore.i_pulsanti["p2"]==True:
            ascensore.i_pulsanti["p2"] = False
            
            ascensore.gestioneMotore((False,True,False))#motore in salita
            lettura_orologio = orologio
            ascensore.stampa("acensore in salita verso piano 2, motore su")
            ascensore.messaggio = "salita1"
            
        if (ascensore.o_motore["m_Su"] == True) and (ascensore.messaggio=="salita1") :
            if orologio > lettura_orologio + ascensore.tempo_piano :
                ascensore.stato = 2
                ascensore.messaggio =""
                        
        if ascensore.messaggio == "salita1":
            ascensore.altezza_cabina -=0.1
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(255,255,0))
            
    elif ascensore.stato == 2:
        #cosa si deve fare nello stato 2, una volta sola
        if ascensore.messaggio =="":
            ascensore.stampa("stato 2, piano secondo")           
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(0,0,255))
            ascensore.gestioneMotore((True,False,True))#motore fermo
            
        # rimango nello stato 2    
        if ascensore.i_pulsanti["p2"]==True:
            ascensore.i_pulsanti["p2"] = False
            ascensore.stato = 2
        
        # cosa fare per passare in ascensore in allarme
        if ascensore.i_pulsanti["pA"] == True:
            ascensore.i_pulsanti["pA"] = False
            ascensore.stato = 3
            ascensore.messaggio = ""
            
        # cosa fare nel passare allo stato 1
        if ascensore.i_pulsanti["p1"] == True:
            ascensore.i_pulsanti["p1"] = False
            
            ascensore.gestioneMotore((False,False,True))#motore in discesa
            lettura_orologio = orologio
            ascensore.stampa("acensore in discesa verso piano primo, motore giu") 
            ascensore.messaggio = "discesa1"
            
        if (ascensore.o_motore["m_Giu"] == True) and (ascensore.messaggio=="discesa1") :
            if orologio > lettura_orologio + ascensore.tempo_piano :
                ascensore.stato = 1
                ascensore.messaggio =""
                        
        if ascensore.messaggio == "discesa1":
            ascensore.altezza_cabina +=0.1
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(0,0,255))

        # cosa fare nel passare allo stato 0    
        if ascensore.i_pulsanti["pT"]==True:
            ascensore.i_pulsanti["pT"] = False
            
            ascensore.gestioneMotore((False,False,True))#motore in discesa
            lettura_orologio = orologio
            ascensore.stampa("acensore in discesa verso piano terra, motore giu")
            ascensore.messaggio = "discesa2"
            
        if (ascensore.o_motore["m_Giu"] == True) and (ascensore.messaggio=="discesa2") :
            if orologio > lettura_orologio + ascensore.tempo_piano*2 :
                ascensore.stato = 0
                ascensore.messaggio =""
                        
        if ascensore.messaggio == "discesa2":
            ascensore.altezza_cabina +=0.1
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(0,0,255))

    elif ascensore.stato == 3:
        #cosa si deve fare nello stato 3 di allarme, una volta sola 
        if ascensore.messaggio =="":
            ascensore.allarme = True
            ascensore.stampa("stato 3, ascensore con chiamata di allarme")           
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(255,0,0))
            ascensore.gestioneMotore((True,False,True))#motore fermo
            
        # cosa fare per passare in modalità manuale
        if ascensore.i_pulsanti["pM"] == True:
            ascensore.i_pulsanti["pM"] = False
            ascensore.stato = 4
            ascensore.messaggio = ""
        
    elif ascensore.stato == 4:
        #cosa si deve fare nello stato 4 modalità manuale, una volta sola 
        if ascensore.messaggio =="":
            ascensore.allarme = False
            ascensore.stampa("stato 4, ascensore in modalità manuale")           
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(255,0,255))
            ascensore.gestioneMotore((False,False,True))#motore giu
            ascensore.messaggio ="discesa1"
         
            
        if ascensore.messaggio == "discesa1":
            ascensore.altezza_cabina +=0.1
            ascensore.disegna(schermo, immagineV,immagineC,immagineA,(0,255,255))
            if ascensore.y + ascensore.altezza_cabina > 450:
                ascensore.stato = 0
                ascensore.messaggio = ""
        
            
pygame.quit()

           