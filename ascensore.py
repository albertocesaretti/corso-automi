#semaforo
import pygame as p
p.init()
schermo = p.display.set_mode((800, 600))


timer = 0 #timer
stato = 0 #stato
bPT = False #bottone pt
bP1 = False #bottone p1
bP2 = False #bottone p2
m_fermo = True # motore fermo
m_Su	= False #motore Su'
m_Giu 	= False #motore Giu'
messaggio = ""



while True :

    for event in p.event.get():
        #print(f"hello {event}")
        if (event.type == p.KEYDOWN):
            if event.unicode == 't':
                bPT = True
                print('attivato bottone piano terra')
            if event.unicode == '1':
                bP1 = True
                print('attivato bottone piano primo')                
            if event.unicode == '2':
                bP2 = True
                print('attivato bottone piano secondo')     
        
    if stato == 0:
        #cosa fare nello stato 0
        if messaggio == "":            
            messaggio = "ascensore fermo al piano terra, motore fermo"
            print(messaggio)
            schermo.fill((0,255,0))
            p.display.update()
            m_fermo = True   # motore fermo
            m_Su	= False #motore Su'
            m_Giu 	= False #motore Giu'
        # rimango al piano terra stato 0
        if bPT == True:
            bPT = False
            stato = 0
        # cosa fare per passare nello stato 1
        if bP1 == True:
            bP1 = False
            m_fermo = False  # motore fermo
            m_Su	= True #motore Su'
            m_Giu 	= False #motore Giu'           
            timer = 0
            messaggio ="acensore in salita verso piano 1, motore su"
            print(messaggio)
            messaggio = "salita1"
        if (timer > 10000000) and (m_Su == True) and (messaggio=="salita1") :
            stato = 1
            messaggio =""
            
        # cosa fare per passare nello stato 2
        if bP2 == True:
            bP2 = False # disattivo il bottone 1
            m_fermo = False  # motore fermo
            m_Su	= True #motore Su'
            m_Giu 	= False #motore Giu'           
            timer = 0
            messaggio ="acensore in salita verso piano 2, motore su"
            print(messaggio)
            messaggio = "salita2"
        if (timer > 20000000) and (m_Su == True) and (messaggio =="salita2"):
            stato = 2
            messaggio =""

        # incremento il timer sempre
        timer += 1
        
    elif stato == 1:
        #cosa fare nello stato 1
        if messaggio == "":            
            messaggio = "ascensore al piano 1, motore fermo"
            print(messaggio)
            schermo.fill((255,255,0))
            p.display.update()
            m_fermo = True   # motore fermo
            m_Su	= False #motore Su'
            m_Giu 	= False #motore Giu'
        # rimango al piano primo stato = 1 
        if bP1 == True:
            bP1 = False
            stato = 1
        # cosa fare per passare allo stato 0
        if bPT == True:
            bPT = False
            m_fermo = False  # motore fermo
            m_Su	= False #motore Su'
            m_Giu 	= True #motore Giu'           
            timer = 0
            messaggio ="acensore in discesa verso piano terra, motore giu'"
            print(messaggio)
            messaggio = "discesa1"
        if (timer > 10000000) and (m_Giu == True) and (messaggio=="discesa1") :
            stato = 0
            messaggio =""            
        # cosa fare per passare nello stato 2
        if bP2 == True:
            bP2 = False
            m_fermo = False  # motore fermo
            m_Su	= True #motore Su'
            m_Giu 	= False #motore Giu'           
            timer = 0
            messaggio ="acensore in salita verso piano 2, motore su"
            print(messaggio)
            messaggio = "salita1"
        if (timer > 10000000) and (m_Su == True) and (messaggio=="salita1") :
            stato = 2
            messaggio =""
        
        # incremento il timer sempre
        timer += 1
        
    elif stato == 2:
        #cosa fare nello stato 2
        if messaggio == "":            
            messaggio = "ascensore al piano 2, motore fermo"
            print(messaggio)
            schermo.fill((0,0,255))
            p.display.update()
            m_fermo = True   # motore fermo
            m_Su	= False #motore Su'
            m_Giu 	= False #motore Giu'
            
        # rimango al piano primo stato = 2 
        if bP2 == True:
            bP2 = False
            stato = 2
        # cosa fare per passare nello stato 1
        if bP1 == True:
            bP1 = False
            m_fermo = False  # motore fermo
            m_Su	= False #motore Su'
            m_Giu 	= True #motore Giu'           
            timer = 0
            messaggio ="acensore in discesa verso piano 1, motore giu'"
            print(messaggio)
            messaggio = "discesa1"
        if (timer > 10000000) and (m_Giu == True) and (messaggio=="discesa1") :
            stato = 1
            messaggio =""
        # cosa fare per passare nello stato 0
        if bPT == True:
            bPT = False # disattivo il bottone 1
            m_fermo = False  # motore fermo
            m_Su	= False #motore Su'
            m_Giu 	= True #motore Giu'           
            timer = 0
            messaggio ="acensore in discesa verso piano terra, motore giu'"
            print(messaggio)
            messaggio = "discesa2"
        if (timer > 20000000) and (m_Giu == True) and (messaggio =="discesa2"):
            stato = 0
            messaggio =""        
        # incremento il timer sempre
        timer += 1
    
            
        
        