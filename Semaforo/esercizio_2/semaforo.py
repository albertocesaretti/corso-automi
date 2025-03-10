import pygame

pygame.init()#inizializzazione
pygame.display.set_caption("Semaforo")#scriviamo il titolo sulla finestra

schermo = pygame.display.set_mode( (800,600))#schermo ad 800 x 600 pixel
schermo.fill( (0,255,0))#coloriamo lo sfondo di rosso

semaforoV = pygame.image.load("image/semaforoVerde.png")#caricato in memoria
schermo.blit(semaforoV, (0,0))#copiamo l'immagine sullo schermo

def letturaIngressi():
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            print(evento.unicode)
            return evento.unicode
            """if evento.unicode == "q":
                print("Ha schiacciato il tasto q (quit) per uscire")
                run = False
            """
run = True
while run:
    #l'orologio conta il passare del tempo in millisecondi
    orologio = p.time.get_ticks()
    
    ingresso = letturaIngressi()
    if ingresso == "q":
        run = False
        
    pygame.display.update()#refresh pagina molto,molto importante
    
pygame.quit()