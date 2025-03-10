import pygame

class Ascensore:
    x = 0
    y = 0
    stato = 0
    allarme = False
    image = ""
    altezza_cabina = 450
    tempo_piano = 8000 #millisecondi
    i_pulsanti = {"pT":False, "p1":False, "p2":False, "pA":False, "pM":False}
    luce_emessa = (0,255,0) #RGB
    o_motore = {"m_Fermo":False, "m_Su":False, "m_Giu":False}
    messaggio = ""
    run = True 
    
    def __init__(self, x, y, stato, luce_emessa, image):
        self.x = x
        self.y = y
        self.stato = stato
        self.luce_emessa = luce_emessa
        self.image = image
        
    def sposta(self, x, y):
        self.x = x
        self.y = y
        
    def disegna(self, schermo, imageV, imageC, imageA, luce_emessa):
        schermo.fill(luce_emessa)
        schermo.blit(imageV, (self.x, self.y))
        schermo.blit(imageC, (self.x + 60, self.y + self.altezza_cabina))
        if self.allarme == True:
           schermo.blit(imageA, (self.x + 60, self.y+self.altezza_cabina -50))
        pygame.display.update()
        
    def gestioneMotore(self, o_motore):
        self.o_motore["m_Fermo"] = o_motore[0]
        self.o_motore["m_Su"]   = o_motore[1]
        self.o_motore["m_Giu"] = o_motore[2]
        
    def stampa(self, messaggio):
        self.messaggio = messaggio
        print(messaggio)
        pygame.display.set_caption(messaggio)
        

pygame.init()

pygame.display.set_caption("Ascensore")
schermo = pygame.display.set_mode( (800,600))




pygame.quit()
        
        
        
        
        
        
        
        
        
        
        
        
        
        