import sys, random, time, pygame
import os

# initialisation 
pygame.init()

# la fenêtre
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Tron")


# chargement d'une fonte
# ici la fonte de la charte IMERIR
# des fontes TTF peuvent être trouvées sur https://www.dafont.com
font_text = pygame.font.Font(('assets/BlernRegular.otf'), 24)
font_title = pygame.font.Font(('assets/BlernRegular.otf'), 50)
text_victoire_rouge = font_title.render(f"victoire   du  joueur  rouge", True, (0, 255, 0))
text_victoire_bleu = font_title.render(f"victoire   du  joueur  bleu", True, (0, 255, 0))


surface = pygame.display.set_mode((1280,720))
couleur1 = (255,0,0)
couleur2 = (0,0,255)
clock = pygame.time.Clock()




# boucle du jeu
run = True

# initialisation des listes et coordonnées
x1=0
y1=0
y2=0
x2=0
listex1=[]
listey1=[]
listex2=[]
listey2=[]

# nombre de victoires initiales
vr=0
vb=0
vbstr="0"
vrstr="0"

# direction initiale de la moto
top2="false"
bottom2="true"
right2="false"
left2="false"
top1="true"
bottom1="false"
right1="false"
left1="false"


while run:
    if vb==3 or vr==3: # victoire d'un des joueurs
        if vb==3: # victoire du bleu
            pygame.display.update()
            screen.blit(text_victoire_bleu, (400, 300))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type==pygame.KEYDOWN: # une touche a été pressée
                    if event.key==pygame.K_q:  # c'est la touche q
                        run = False
        if vr==3: # victoire du rouge
            pygame.display.update()
            screen.blit(text_victoire_rouge, (400, 300))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type==pygame.KEYDOWN: # une touche a été pressée
                    if event.key==pygame.K_q:  # c'est la touche q
                        run = False
    else:
        # mise a jour affichage
        text_score = font_text.render(f"victoire  bleu  "+vbstr+"  /victoire  rouge  "+vrstr, True, (0, 255, 0))
        screen.blit(text_score, (0, 0))
        pygame.display.update()

        # déplacement de la moto selon la direction
        if left1=="true":
            x1=x1-8
        if right1=="true":
            x1=x1+8
        if top1=="true":
            y1=y1-8
        if bottom1=="true":
            y1=y1+8
        if left2=="true":
            x2=x2-8
        if right2=="true":
            x2=x2+8
        if top2=="true":
            y2=y2-8
        if bottom2=="true":
            y2=y2+8

        # mise en plpace des coordonnées de la moto
        x11=640+x1
        y11=360+y1
        x21=640+x2
        y21=352+y2

        # attribution des coordonnées des murs
        listex1.append(x11)
        listey1.append(y11)
        listex2.append(x21)
        listey2.append(y21)

        # mise en place des murs sur le passage de la moto
        pygame.draw.rect(surface,couleur1,pygame.Rect(x11, y11, 8, 8))
        pygame.draw.rect(surface,couleur2,pygame.Rect(x21, y21, 8, 8))
        clock.tick(30)

        if x11<0 or x11>1280 or y11<0 or y11>720: # check de colision du joueur rouge
            # redémarage de l'arène et attribution des points
            screen.fill(color=(0,0,0))
            top2="false"
            bottom2="true"
            right2="false"
            left2="false"
            top1="true"
            bottom1="false"
            right1="false"
            left1="false"
            x1=0
            y1=0
            y2=0
            x2=0
            listex1=[]
            listey1=[]
            listex2=[]
            listey2=[]
            vb=vb+1
            vbstr=str(vb)
            time.sleep(3)

        if x21<0 or x21>1280 or y21<0 or y21>720: # check de colision du joueur bleu
            # redémarage de l'arène et attribution des points
            screen.fill(color=(0,0,0))
            top2="false"
            bottom2="true"
            right2="false"
            left2="false"
            top1="true"
            bottom1="false"
            right1="false"
            left1="false"
            x1=0
            y1=0
            y2=0
            x2=0
            listex1=[]
            listey1=[]
            listex2=[]
            listey2=[]
            vr=vr+1
            vrstr=str(vr)
            time.sleep(3)

        for i in range (len(listey1)-1):
            if (x11 == listex1[i] and y11 == listey1[i]) or (x11 == listex2[i] and y11 == listey2[i]): # check de colision du joueur rouge
                # redémarage de l'arène et attribution des points
                screen.fill(color=(0,0,0))
                top2="false"
                bottom2="true"
                right2="false"
                left2="false"
                top1="true"
                bottom1="false"
                right1="false"
                left1="false"
                x1=0
                y1=0
                y2=0
                x2=0
                listex1=[]
                listey1=[]
                listex2=[]
                listey2=[]
                vb=vb+1
                vbstr=str(vb)
                time.sleep(3)
                break

        for i in range (len(listey1)-1):
            if (x21 == listex1[i] and y21 == listey1[i]) or (x21 == listex2[i] and y21 == listey2[i]): # check de colision du joueur bleu
                # redémarage de l'arène et attribution des points
                screen.fill(color=(0,0,0))
                top2="false"
                bottom2="true"
                right2="false"
                left2="false"
                top1="true"
                bottom1="false"
                right1="false"
                left1="false"
                x1=0
                y1=0
                y2=0
                x2=0
                listex1=[]
                listey1=[]
                listex2=[]
                listey2=[]
                vr=vr+1
                vrstr=str(vr)
                time.sleep(3)
                break



        # boucle de gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type==pygame.KEYDOWN: # une touche a été pressée
                if event.key==pygame.K_q:  # c'est la touche q
                    run = False
                if event.key==pygame.K_s: # tourne à gauche pour le joueur rouge
                    if top1=="true":
                        top1="false"
                        right1="true"
                    elif bottom1=="true":
                        bottom1="false"
                        left1="true"
                    elif right1=="true":
                        right1="false"
                        bottom1="true"
                    elif left1=="true":
                        left1="false"
                        top1="true"
                if event.key==pygame.K_d: # tourne à droite pour le joueur rouge
                    if top1=="true":
                        top1="false"
                        left1="true"
                    elif bottom1=="true":
                        bottom1="false"
                        right1="true"
                    elif right1=="true":
                        right1="false"
                        top1="true"
                    elif left1=="true":
                        left1="false"
                        bottom1="true"
                if event.key==pygame.K_LEFT: # tourne à gauche pour le joueur bleu
                    if top2=="true":
                        top2="false"
                        right2="true"
                    elif bottom2=="true":
                        bottom2="false"
                        left2="true"
                    elif right2=="true":
                        right2="false"
                        bottom2="true"
                    elif left2=="true":
                        left2="false"
                        top2="true"
                if event.key==pygame.K_RIGHT: # tourne à droite pour le joueur bleu
                    if top2=="true":
                        top2="false"
                        left2="true"
                    elif bottom2=="true":
                        bottom2="false"
                        right2="true"
                    elif right2=="true":
                        right2="false"
                        top2="true"
                    elif left2=="true":
                        left2="false"
                        bottom2="true"
                if event.key==pygame.K_SPACE: # met le jeu en pause (wip)
                    if top2=="true":
                        direct2="top2"
                        top2="false"
                    if bottom2=="true":
                        direct2="bottom2"
                        bottom2="false"
                    if right2=="true":
                        direct2="right2"
                        right2="false"
                    if left2=="true":
                        direct2="left2"
                        left2="false"
                    if top1=="true":
                        direct1="top1"
                        top1="false"
                    if bottom1=="true":
                        direct1="bottom1"
                        bottom1="false"
                    if right1=="true":
                        direct1="right1"
                        right1="false"
                    if left1=="true":
                        direct1="left1"
                        left1="false"

                    if event.key==pygame.K_k: # redémare le jeu (wip)
                        if direct2=="top2":
                            direct2=""
                            top2="true"
                        if direct2=="top2":
                            direct2=""
                            bottom2="true"
                        if direct2=="top2":
                            direct2=""
                            right2="true"
                        if direct2=="top2":
                            direct2=""
                            left2="true"
                        if direct1=="top2":
                            direct1=""
                            top1="true"
                        if direct1=="top2":
                            direct1=""
                            bottom1="true"
                        if direct1=="top2":
                            direct1=""
                            right1="true"
                        if direct1=="top2":
                            direct1=""
                            left1="true"


                        



