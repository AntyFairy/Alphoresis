from random import *
from math import *

programme=True
action_faite=False

def calcul_distance(x1, y1, x2, y2):
    ys=y1-y2
    xs=x1-x2
    distance=sqrt(ys*ys+xs*xs)
    return(distance)

print("###")
print("Project Alphoresis")
print("Version 0.1.3  |  State : indev  |  Made with Python 3.11.1")
print("###")
print(" ")

while programme==True:

    print("###")
    print("Vous êtes sur le menu principal. Voici une liste de commandes :")
    print("[1] Jouer")
    print("[2] Paramètres")
    print("[3] Quitter le jeu")
    print("###")

    reponse=int(input("-> "))
    if reponse==1:
        print(" ")
        print("Choisissez le mode de jeu :")
        print("[1] 1v1 Classique")
        print("")
        choix_mode_de_jeu=int(input())
        if choix_mode_de_jeu==1:
            print(" ")
            print("1v1 Classique | Partie lancée !")
            print(" ")
            en_jeu=True


        #selection des personnages

            print("Commandant rebelle, choisissez vos unités ! (3 max)")
            print(" ")
            print("[1] Luke Skywalker | HP: 60 | Stamina: 4 | Portée: Corps-à-corps | Capacité spéciale: Brûlure de sabre laser (passif)")
            print("[2] Princesse Leia | HP: 40 | Stamina: 4 | Portée: à distance")
            print("[3] Han Solo | HP: 60 | Stamina: 3 | Portée: à distance")
            print("[4] Chewbacca | HP: 60 | Stamina: 2 | Portée: à distance | Capacité spéciale: Cri (passif)")
            print("")

            hp_luke=0
            x_luke=1
            y_luke=4
            stamina_luke=4

            hp_leia=0
            x_leia=1
            y_leia=3
            stamina_leia=4

            hp_han=0
            x_han=3
            y_han=1
            stamina_han=3

            hp_chew=0
            x_chew=4
            y_chew=1
            stamina_chew=2

            for i in range(3):
                unite_choisie=int(input("-> "))
                if unite_choisie==1:
                    hp_luke=60
                    print("Vous avez choisi : Luke Skywalker!")
                if unite_choisie==2:
                    hp_leia=40
                    print("Vous avez choisi : Princesse Leia!")
                if unite_choisie==3:
                    hp_han=60
                    print("Vous avez choisi : Han Solo!")
                if unite_choisie==4:
                    hp_chew=60
                    print("Vous avez choisi : Chewbacca!")



            print(" ")
            print("Commandant impérial, choisissez vos unités ! (3 max)")
            print(" ")
            print("[1] Dark Vador | HP: 60 | Stamina: 4 | Portée: Corps-à-corps | Capacité spéciale: Brûlure de sabre laser (passif)")
            print("[2] Stormtroopers | HP: 40 | Stamina: 4 | Portée: à distance")
            print("[3] Snowtroopers | HP: 60 | Stamina: 3 | Portée: à distance")
            print("[4] Boba Fett  | HP: 60 | Stamina: 2 | Portée: à distance")
            print("")

            hp_vador=0
            x_vador=7
            y_vador=10
            stamina_vador=4

            hp_storm=0
            x_storm=8
            y_storm=10
            stamina_storm=4

            hp_snow=0
            x_snow=10
            y_snow=8
            stamina_snow=3

            hp_boba=0
            x_boba=10
            y_boba=7
            stamina_boba=2

            for i in range(3):
                unite_choisie=int(input("-> "))
                if unite_choisie==1:
                    hp_vador=60
                    print("Vous avez choisi : Dark Vador!")
                if unite_choisie==2:
                    hp_storm=40
                    print("Vous avez choisi : Stormtroopers!")
                if unite_choisie==3:
                    hp_snow=60
                    print("Vous avez choisi : Snowtroopers!")
                if unite_choisie==4:
                    hp_boba=60
                    print("Vous avez choisi : Boba Fett!")

# Fin de séléction des personnages
# Début des tours

            while en_jeu==True:
                print(" ")
                print("Début du tour !")
                print(" ")
                print("-_-_-_-")

                stamina_luke=4
                stamina_leia=4
                stamina_han=3
                stamina_chew=2
                stamina_vador=4
                stamina_storm=4
                stamina_snow=3
                stamina_boba=2
                
            #INFORMATIONS EN DIRECT
             
                if hp_luke>0:
                    print("~ Luke Skywalker | HP restants : ", hp_luke, " | X=", x_luke, " ; Y=", y_luke)
                if hp_leia>0:
                    print("~ Princesse Leia | HP restants : ", hp_leia, " | X=", x_leia, " ; Y=", y_leia)
                if hp_han>0:
                    print("~ Han Solo | HP restants : ", hp_han, " | X=", x_han, " ; Y=", y_han)
                if hp_chew>0:
                    print("~ Chewbacca | HP restants : ", hp_chew, " | X=", x_chew, " ; Y=", y_chew)
                print(" ")
                if hp_vador>0:
                    print("~ Dark Vador | HP restants : ", hp_vador, " | X=", x_vador, " ; Y=", y_vador)
                if hp_storm>0:
                    print("~ Stormtroopers | HP restants : ", hp_storm, " | X=", x_storm, " ; Y=", y_storm)
                if hp_snow>0:
                    print("~ Snowtroopers | HP restants : ", hp_snow, " | X=", x_snow, " ; Y=", y_snow)
                if hp_boba>0:
                    print("~ Boba Fett | HP restants : ", hp_boba, " | X=", x_boba, " ; Y=", y_boba)
                print("-_-_-_-")

                print(" ")
                print("Commandant rebelle, choisissez une unité à utiliser !")
                if hp_luke>0:
                    print("[1] Luke Skywalker | HP restant : ", end="")
                    print(hp_luke)
                if hp_leia>0:
                    print("[2] Princesse Leia | HP restant : ", end="")
                    print(hp_leia)
                if hp_han>0:
                    print("[3] Han Solo | HP restant : ", end="")
                    print(hp_han)
                if hp_chew>0:
                    print("[4] Chewbacca | HP restant : ", end="")
                    print(hp_chew)

                reponse_unite_choisie=int(input("-> "))


                if reponse_unite_choisie==1 and hp_luke>0:
                    while stamina_luke>0:

                        print("-> Luke Skywalker | Stamina : ", stamina_luke, " | Voulez vous :")
                        if hp_luke<60:
                            print("[1] Soin (10 HP)")
                        print("[2] Attaque")
                        print("[3] Déplacement")
                        print("[4] Passer le tour")
                        print(" ")

                        reponse_action=int(input("-> "))

                    #SOIN: OK

                        if reponse_action==1 and hp_luke<=59:
                            if hp_luke>50:
                                hp_luke=60
                            else:
                                hp_luke=hp_luke+10
                            print(" ")
                            print("Luke Skywalker a désormais ", end="")
                            print(hp_luke, end="")
                            print(" HP.")
                            stamina_luke=0

                    #ATTAQUE:

                        if reponse_action==2:
                            print(" ")
                            print("Qui voulez-vous attaquer ?")
                            if hp_vador>0 and calcul_distance(x_luke, y_luke, x_vador, y_vador) <=2:
                                print("[1] Dark Vador | HP restant : ", end="")
                                print(hp_vador)
                            if hp_storm>0 and calcul_distance(x_luke, y_luke, x_storm, y_storm) <=2:
                                print("[2] Stormtroopers | HP restant : ", end="")
                                print(hp_storm)
                            if hp_snow>0 and calcul_distance(x_luke, y_luke, x_snow, y_snow) <=2:
                                print("[3] Snowtroopers | HP restant : ", end="")
                                print(hp_snow)
                            if hp_boba>0 and calcul_distance(x_luke, y_luke, x_boba, y_boba) <=2:
                                print("[4] Boba Fett | HP restant : ", end="")
                                print(hp_boba)
                            print("[0] Retour en arrière")
                            print(" ")
                            reponse_attaque=int(input("-> "))
                            
                            if reponse_attaque==0:
                                print(" ")
                            if reponse_attaque==1 and calcul_distance(x_luke, y_luke, x_vador, y_vador) <=2:
                                
                                print(" ")
                                print("Attaque contre Dark Vador, puissance de ", stamina_luke, " Stamina...")
                                for i in range(stamina_luke):
                                    puissance_attaque=range(1, 11)
                                    hp_vador=hp_vador-choice(puissance_attaque)
                                    print(" ")
                                print("Dark Vador a désormais ", end="")
                                print(hp_vador, end=" ")
                                print("HP.")
                                stamina_luke=0
                            if reponse_attaque==2 and calcul_distance(x_luke, y_luke, x_storm, y_storm) <=2:
                                print(" ")
                                print("Attaque contre Stormtroopers, puissance de ", stamina_luke, " Stamina...")
                                for i in range(stamina_luke):
                                    puissance_attaque=range(1, 11)
                                    hp_storm=hp_storm-choice(puissance_attaque)
                                    print(" ")
                                print("Stormtroopers ont désormais ", end="")
                                print(hp_storm, end=" ")
                                print("HP.")
                                stamina_luke=0
                            if reponse_attaque==3 and calcul_distance(x_luke, y_luke, x_snow, y_snow) <=2:
                                print(" ")
                                print("Attaque contre Snowtroopers, puissance de ", stamina_luke, " Stamina...")
                                for i in range(stamina_luke):
                                    puissance_attaque=range(1, 11)
                                    hp_snow=hp_snow-choice(puissance_attaque)
                                    print(" ")
                                print("Snowtroopers ont désormais ", end="")
                                print(hp_snow, end=" ")
                                print("HP.")
                                stamina_luke=0
                            if reponse_attaque==4 and calcul_distance(x_luke, y_luke, x_boba, y_boba) <=2:
                                print(" ")
                                print("Attaque contre Boba Fett, puissance de ", stamina_luke, " Stamina...")
                                for i in range(stamina_luke):
                                    puissance_attaque=range(1, 11)
                                    hp_boba=hp_boba-choice(puissance_attaque)
                                    print(" ")
                                print("Boba Fett a désormais ", end="")
                                print(hp_boba, end=" ")
                                print("HP.")
                                stamina_luke=0
                    
                    #DÉPLACEMENT: OK

                        if reponse_action==3:
                            print(" ")
                            print("Déplacement (3 cases par stamina)")
                            print(" ")
                            x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                            y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                            print(" ")
                            distance_entre_voulue_et_actuelle=calcul_distance(x_luke, y_luke, x_deplacement_voulu, y_deplacement_voulu)
                            if  distance_entre_voulue_et_actuelle <= 3*stamina_luke:
                                if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                    x_luke=x_deplacement_voulu
                                    y_luke=y_deplacement_voulu
                                    stamina_luke=stamina_luke - 1
                                if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                    x_luke=x_deplacement_voulu
                                    y_luke=y_deplacement_voulu
                                    stamina_luke=stamina_luke - 2
                                if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                    x_luke=x_deplacement_voulu
                                    y_luke=y_deplacement_voulu
                                    stamina_luke=stamina_luke - 3
                                if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                    x_luke=x_deplacement_voulu
                                    y_luke=y_deplacement_voulu
                                    stamina_luke=stamina_luke - 4
                                print("Luke Skywalker est désormais en X=", end=" ")
                                print(x_luke)
                                print(", Y=", end=" ")
                                print(y_luke)
                            else:
                                print(" ")
                                print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                    #PASSER LE TOUR: OK
                        if reponse_action==4:
                            stamina_luke=0
                    
                if reponse_unite_choisie==2 and hp_leia>0:

                    while stamina_leia>0:

                        print("-> Leia | Stamina : ", stamina_leia, " | Voulez vous :")
                        if hp_leia<40:
                            print("[1] Soin (10 HP)")
                        print("[2] Attaque")
                        print("[3] Déplacement")
                        print("[4] Passer le tour")
                        print(" ")

                        reponse_action=int(input("-> "))

                    #SOIN: OK

                        if reponse_action==1 and hp_leia<=59:
                            if hp_leia>30:
                                hp_leia=40
                            else:
                                hp_leia=hp_leia+10
                            print(" ")
                            print("Leia a désormais ", end="")
                            print(hp_leia, end="")
                            print(" HP.")
                            stamina_leia=0

                    #ATTAQUE:

                        if reponse_action==2:
                            print(" ")
                            print("Qui voulez-vous attaquer ?")
                            if hp_vador>0 and calcul_distance(x_leia, y_leia, x_vador, y_vador) <=4:
                                print("[1] Dark Vador | HP restant : ", end="")
                                print(hp_vador)
                            if hp_storm>0 and calcul_distance(x_leia, y_leia, x_storm, y_storm) <=4:
                                print("[2] Stormtroopers | HP restant : ", end="")
                                print(hp_storm)
                            if hp_snow>0 and calcul_distance(x_leia, y_leia, x_snow, y_snow) <=4:
                                print("[3] Snowtroopers | HP restant : ", end="")
                                print(hp_snow)
                            if hp_boba>0 and calcul_distance(x_leia, y_leia, x_boba, y_boba) <=4:
                                print("[4] Boba Fett | HP restant : ", end="")
                                print(hp_boba)
                            print("[0] Retour en arrière")
                            print(" ")
                            reponse_attaque=int(input("-> "))
                            
                            if reponse_attaque==0:
                                print(" ")
                            if reponse_attaque==1 and calcul_distance(x_leia, y_leia, x_vador, y_vador) <=4:
                                
                                print(" ")
                                print("Attaque contre Dark Vador, puissance de ", stamina_leia, " Stamina...")
                                for i in range(stamina_leia):
                                    puissance_attaque=range(1, 11)
                                    hp_vador=hp_vador-choice(puissance_attaque)
                                    print(" ")
                                print("Dark Vador a désormais ", end="")
                                print(hp_vador, end=" ")
                                print("HP.")
                                stamina_leia=0
                            if reponse_attaque==2 and calcul_distance(x_leia, y_leia, x_storm, y_storm) <=4:
                                print(" ")
                                print("Attaque contre Stormtroopers, puissance de ", stamina_leia, " Stamina...")
                                for i in range(stamina_leia):
                                    puissance_attaque=range(1, 11)
                                    hp_storm=hp_storm-choice(puissance_attaque)
                                    print(" ")
                                print("Stormtroopers ont désormais ", end="")
                                print(hp_storm, end=" ")
                                print("HP.")
                                stamina_leia=0
                            if reponse_attaque==3 and calcul_distance(x_leia, y_leia, x_snow, y_snow) <=4:
                                print(" ")
                                print("Attaque contre Snowtroopers, puissance de ", stamina_leia, " Stamina...")
                                for i in range(stamina_leia):
                                    puissance_attaque=range(1, 11)
                                    hp_snow=hp_snow-choice(puissance_attaque)
                                    print(" ")
                                print("Snowtroopers ont désormais ", end="")
                                print(hp_snow, end=" ")
                                print("HP.")
                                stamina_leia=0
                            if reponse_attaque==4 and calcul_distance(x_leia, y_leia, x_boba, y_boba) <=4:
                                print(" ")
                                print("Attaque contre Boba Fett, puissance de ", stamina_leia, " Stamina...")
                                for i in range(stamina_leia):
                                    puissance_attaque=range(1, 11)
                                    hp_boba=hp_boba-choice(puissance_attaque)
                                    print(" ")
                                print("Boba Fett a désormais ", end="")
                                print(hp_boba, end=" ")
                                print("HP.")
                                stamina_leia=0
                    
                    #DÉPLACEMENT: OK

                        if reponse_action==3:
                            print(" ")
                            print("Déplacement (3 cases par stamina)")
                            print(" ")
                            x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                            y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                            print(" ")
                            distance_entre_voulue_et_actuelle=calcul_distance(x_leia, y_leia, x_deplacement_voulu, y_deplacement_voulu)
                            if  distance_entre_voulue_et_actuelle <= 3*stamina_leia:
                                if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                    x_leia=x_deplacement_voulu
                                    y_leia=y_deplacement_voulu
                                    stamina_leia=stamina_leia - 1
                                if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                    x_leia=x_deplacement_voulu
                                    y_leia=y_deplacement_voulu
                                    stamina_leia=stamina_leia - 2
                                if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                    x_leia=x_deplacement_voulu
                                    y_leia=y_deplacement_voulu
                                    stamina_leia=stamina_leia - 3
                                if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                    x_leia=x_deplacement_voulu
                                    y_leia=y_deplacement_voulu
                                    stamina_leia=stamina_leia - 4
                                print("leia est désormais en X=", end=" ")
                                print(x_leia)
                                print(", Y=", end=" ")
                                print(y_leia)
                            else:
                                print(" ")
                                print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                    #PASSER LE TOUR: OK
                        if reponse_action==4:
                            stamina_leia=0

                if reponse_unite_choisie==3 and hp_han>0:

                    while stamina_han>0:

                        print("-> Han Solo | Stamina : ", stamina_han, " | Voulez vous :")
                        if hp_han<50:
                            print("[1] Soin (10 HP)")
                        print("[2] Attaque")
                        print("[3] Déplacement")
                        print("[4] Passer le tour")
                        print(" ")

                        reponse_action=int(input("-> "))

                    #SOIN: OK

                        if reponse_action==1 and hp_han<=59:
                            if hp_han>50:
                                hp_han=60
                            else:
                                hp_han=hp_han+10
                            print(" ")
                            print("Han Solo a désormais ", end="")
                            print(hp_han, end="")
                            print(" HP.")
                            stamina_han=0

                    #ATTAQUE:

                        if reponse_action==2:
                            print(" ")
                            print("Qui voulez-vous attaquer ?")
                            if hp_vador>0 and calcul_distance(x_han, y_han, x_vador, y_vador) <=4:
                                print("[1] Dark Vador | HP restant : ", end="")
                                print(hp_vador)
                            if hp_storm>0 and calcul_distance(x_han, y_han, x_storm, y_storm) <=4:
                                print("[2] Stormtroopers | HP restant : ", end="")
                                print(hp_storm)
                            if hp_snow>0 and calcul_distance(x_han, y_han, x_snow, y_snow) <=4:
                                print("[3] Snowtroopers | HP restant : ", end="")
                                print(hp_snow)
                            if hp_boba>0 and calcul_distance(x_han, y_han, x_boba, y_boba) <=4:
                                print("[4] Boba Fett | HP restant : ", end="")
                                print(hp_boba)
                            print("[0] Retour en arrière")
                            print(" ")
                            reponse_attaque=int(input("-> "))
                            
                            if reponse_attaque==0:
                                print(" ")
                            if reponse_attaque==1 and calcul_distance(x_han, y_han, x_vador, y_vador) <=4:
                                
                                print(" ")
                                print("Attaque contre Dark Vador, puissance de ", stamina_han, " Stamina...")
                                for i in range(stamina_han):
                                    puissance_attaque=range(1, 11)
                                    hp_vador=hp_vador-choice(puissance_attaque)
                                    print(" ")
                                print("Dark Vador a désormais ", end="")
                                print(hp_vador, end=" ")
                                print("HP.")
                                stamina_han=0
                            if reponse_attaque==2 and calcul_distance(x_han, y_han, x_storm, y_storm) <=4:
                                print(" ")
                                print("Attaque contre Stormtroopers, puissance de ", stamina_han, " Stamina...")
                                for i in range(stamina_han):
                                    puissance_attaque=range(1, 11)
                                    hp_storm=hp_storm-choice(puissance_attaque)
                                    print(" ")
                                print("Stormtroopers ont désormais ", end="")
                                print(hp_storm, end=" ")
                                print("HP.")
                                stamina_han=0
                            if reponse_attaque==3 and calcul_distance(x_han, y_han, x_snow, y_snow) <=4:
                                print(" ")
                                print("Attaque contre Snowtroopers, puissance de ", stamina_han, " Stamina...")
                                for i in range(stamina_han):
                                    puissance_attaque=range(1, 11)
                                    hp_snow=hp_snow-choice(puissance_attaque)
                                    print(" ")
                                print("Snowtroopers ont désormais ", end="")
                                print(hp_snow, end=" ")
                                print("HP.")
                                stamina_han=0
                            if reponse_attaque==4 and calcul_distance(x_han, y_han, x_boba, y_boba) <=4:
                                print(" ")
                                print("Attaque contre Boba Fett, puissance de ", stamina_han, " Stamina...")
                                for i in range(stamina_han):
                                    puissance_attaque=range(1, 11)
                                    hp_boba=hp_boba-choice(puissance_attaque)
                                    print(" ")
                                print("Boba Fett a désormais ", end="")
                                print(hp_boba, end=" ")
                                print("HP.")
                                stamina_han=0

                if reponse_unite_choisie==4 and hp_chew>0:

                    while stamina_chew>0:

                        print("-> Chewbacca | Stamina : ", stamina_chew, " | Voulez vous :")
                        if hp_chew<50:
                            print("[1] Soin (10 HP)")
                        print("[2] Attaque")
                        print("[3] Déplacement")
                        print("[4] Passer le tour")
                        print(" ")

                        reponse_action=int(input("-> "))

                    #SOIN: OK

                        if reponse_action==1 and hp_chew<=59:
                            if hp_chew>50:
                                hp_chew=60
                            else:
                                hp_chew=hp_chew+10
                            print(" ")
                            print("Chewbacca a désormais ", end="")
                            print(hp_chew, end="")
                            print(" HP.")
                            stamina_chew=0

                    #ATTAQUE:

                        if reponse_action==2:
                            print(" ")
                            print("Qui voulez-vous attaquer ?")
                            if hp_vador>0 and calcul_distance(x_chew, y_chew, x_vador, y_vador) <=4:
                                print("[1] Dark Vador | HP restant : ", end="")
                                print(hp_vador)
                            if hp_storm>0 and calcul_distance(x_chew, y_chew, x_storm, y_storm) <=4:
                                print("[2] Stormtroopers | HP restant : ", end="")
                                print(hp_storm)
                            if hp_snow>0 and calcul_distance(x_chew, y_chew, x_snow, y_snow) <=4:
                                print("[3] Snowtroopers | HP restant : ", end="")
                                print(hp_snow)
                            if hp_boba>0 and calcul_distance(x_chew, y_chew, x_boba, y_boba) <=4:
                                print("[4] Boba Fett | HP restant : ", end="")
                                print(hp_boba)
                            print("[0] Retour en arrière")
                            print(" ")
                            reponse_attaque=int(input("-> "))
                            
                            if reponse_attaque==0:
                                print(" ")
                            if reponse_attaque==1 and calcul_distance(x_chew, y_chew, x_vador, y_vador) <=4:
                                
                                print(" ")
                                print("Attaque contre Dark Vador, puissance de ", stamina_chew, " Stamina...")
                                for i in range(stamina_chew):
                                    puissance_attaque=range(1, 11)
                                    hp_vador=hp_vador-choice(puissance_attaque)
                                    print(" ")
                                print("Dark Vador a désormais ", end="")
                                print(hp_vador, end=" ")
                                print("HP.")
                                stamina_chew=0
                            if reponse_attaque==2 and calcul_distance(x_chew, y_chew, x_storm, y_storm) <=4:
                                print(" ")
                                print("Attaque contre Stormtroopers, puissance de ", stamina_chew, " Stamina...")
                                for i in range(stamina_chew):
                                    puissance_attaque=range(1, 11)
                                    hp_storm=hp_storm-choice(puissance_attaque)
                                    print(" ")
                                print("Stormtroopers ont désormais ", end="")
                                print(hp_storm, end=" ")
                                print("HP.")
                                stamina_chew=0
                            if reponse_attaque==3 and calcul_distance(x_chew, y_chew, x_snow, y_snow) <=4:
                                print(" ")
                                print("Attaque contre Snowtroopers, puissance de ", stamina_chew, " Stamina...")
                                for i in range(stamina_chew):
                                    puissance_attaque=range(1, 11)
                                    hp_snow=hp_snow-choice(puissance_attaque)
                                    print(" ")
                                print("Snowtroopers ont désormais ", end="")
                                print(hp_snow, end=" ")
                                print("HP.")
                                stamina_chew=0
                            if reponse_attaque==4 and calcul_distance(x_chew, y_chew, x_boba, y_boba) <=4:
                                print(" ")
                                print("Attaque contre Boba Fett, puissance de ", stamina_chew, " Stamina...")
                                for i in range(stamina_chew):
                                    puissance_attaque=range(1, 11)
                                    hp_boba=hp_boba-choice(puissance_attaque)
                                    print(" ")
                                print("Boba Fett a désormais ", end="")
                                print(hp_boba, end=" ")
                                print("HP.")
                                stamina_chew=0


#au tour de l'empire de jouer
                print(" ")
                print("_-_-_-")
                if hp_luke>0:
                    print("~ Luke Skywalker | HP restants : ", hp_luke, " | X=", x_luke, " ; Y=", y_luke)
                if hp_leia>0:
                    print("~ Princesse Leia | HP restants : ", hp_leia, " | X=", x_leia, " ; Y=", y_leia)
                if hp_han>0:
                    print("~ Han Solo | HP restants : ", hp_han, " | X=", x_han, " ; Y=", y_han)
                if hp_chew>0:
                    print("~ Chewbacca | HP restants : ", hp_chew, " | X=", x_chew, " ; Y=", y_chew)
                print(" ")
                if hp_vador>0:
                    print("~ Dark Vador | HP restants : ", hp_vador, " | X=", x_vador, " ; Y=", y_vador)
                if hp_storm>0:
                    print("~ Stormtroopers | HP restants : ", hp_storm, " | X=", x_storm, " ; Y=", y_storm)
                if hp_snow>0:
                    print("~ Snowtroopers | HP restants : ", hp_snow, " | X=", x_snow, " ; Y=", y_snow)
                if hp_boba>0:
                    print("~ Boba Fett | HP restants : ", hp_boba, " | X=", x_boba, " ; Y=", y_boba)
                print("-_-_-_-")


                print(" ")
                print("Commandant impérial, choisissez une unité à utiliser !")
                if hp_vador>0:
                    print("[1] Dark Vador | HP restant : ", end="")
                    print(hp_vador)
                if hp_storm>0:
                    print("[2] Stormtroopers | HP restant : ", end="")
                    print(hp_storm)
                if hp_snow>0:
                    print("[3] Snowtroopers | HP restant : ", end="")
                    print(hp_snow)
                if hp_boba>0:
                    print("[4] Boba Fett | HP restant : ", end="")
                    print(hp_boba)
                print(" ")
                reponse_unite_choisie=int(input("-> "))
                print(" ")

                if reponse_unite_choisie==1 and hp_vador>0:

                    while stamina_vador>0:

                        print("-> Dark Vador | Stamina : ", stamina_vador, " | Voulez vous :")
                        if hp_vador<50:
                            print("[1] Soin (10 HP)")
                        print("[2] Attaque")
                        print("[3] Déplacement")
                        print("[4] Passer le tour")
                        print(" ")

                        reponse_action=int(input("-> "))

                    #SOIN: OK

                        if reponse_action==1 and hp_vador<=59:
                            if hp_vador>50:
                                hp_vador=60
                            else:
                                hp_vador=hp_vador+10
                            print(" ")
                            print("Dark Vador a désormais ", end="")
                            print(hp_vador, end="")
                            print(" HP.")
                            stamina_vador=0

                    #ATTAQUE:

                        if reponse_action==2:
                            print(" ")
                            print("Qui voulez-vous attaquer ?")
                            if hp_vador>0 and calcul_distance(x_vador, y_vador, x_vador, y_vador) <=2:
                                print("[1] Luke Skywalker | HP restant : ", end="")
                                print(hp_luke)
                            if hp_leia>0 and calcul_distance(x_vador, y_vador, x_leia, y_leia) <=2:
                                print("[2] Princesse Leia | HP restant : ", end="")
                                print(hp_leia)
                            if hp_han>0 and calcul_distance(x_vador, y_vador, x_han, y_han) <=2:
                                print("[3] Han Solo | HP restant : ", end="")
                                print(hp_han)
                            if hp_chew>0 and calcul_distance(x_vador, y_vador, x_chew, y_chew) <=2:
                                print("[4] Chewbacca | HP restant : ", end="")
                                print(hp_chew)
                            print("[0] Retour en arrière")
                            print(" ")
                            reponse_attaque=int(input("-> "))
                            
                            if reponse_attaque==0:
                                print(" ")
                            if reponse_attaque==1 and calcul_distance(x_luke, y_vador, x_luke, y_vador) <=2:
                                
                                print(" ")
                                print("Attaque contre Luke Skywalker, puissance de ", stamina_vador, " Stamina...")
                                for i in range(stamina_vador):
                                    puissance_attaque=range(1, 11)
                                    hp_vador=hp_vador-choice(puissance_attaque)
                                    print(" ")
                                print("Luke Skywalker a désormais ", end="")
                                print(hp_luke, end=" ")
                                print("HP.")
                                stamina_vador=0
                            if reponse_attaque==2 and calcul_distance(x_vador, y_vador, x_leia, y_leia) <=2:
                                print(" ")
                                print("Attaque contre Princesse Leia, puissance de ", stamina_vador, " Stamina...")
                                for i in range(stamina_vador):
                                    puissance_attaque=range(1, 11)
                                    hp_leia=hp_leia-choice(puissance_attaque)
                                    print(" ")
                                print("Princesse Leia a désormais ", end="")
                                print(hp_leia, end=" ")
                                print("HP.")
                                stamina_vador=0
                            if reponse_attaque==3 and calcul_distance(x_vador, y_vador, x_han, y_han) <=2:
                                print(" ")
                                print("Attaque contre Han Solo, puissance de ", stamina_vador, " Stamina...")
                                for i in range(stamina_vador):
                                    puissance_attaque=range(1, 11)
                                    hp_han=hp_han-choice(puissance_attaque)
                                    print(" ")
                                print("Han Solo ont désormais ", end="")
                                print(hp_han, end=" ")
                                print("HP.")
                                stamina_vador=0
                            if reponse_attaque==4 and calcul_distance(x_vador, y_vador, x_chew, y_chew) <=2:
                                print(" ")
                                print("Attaque contre Chewbacca, puissance de ", stamina_vador, " Stamina...")
                                for i in range(stamina_vador):
                                    puissance_attaque=range(1, 11)
                                    hp_chew=hp_chew-choice(puissance_attaque)
                                    print(" ")
                                print("Chewbacca a désormais ", end="")
                                print(hp_chew, end=" ")
                                print("HP.")
                                stamina_vador=0
            
                if reponse_unite_choisie==2 and hp_storm>0:

                    while stamina_storm>0:

                        print("-> Stormtroopers | Stamina : ", stamina_storm, " | Voulez vous :")
                        if hp_storm<30:
                            print("[1] Soin (10 HP)")
                        print("[2] Attaque")
                        print("[3] Déplacement")
                        print("[4] Passer le tour")
                        print(" ")

                        reponse_action=int(input("-> "))

                    #SOIN: OK

                        if reponse_action==1 and hp_storm<=59:
                            if hp_storm>30:
                                hp_storm=40
                            else:
                                hp_storm=hp_storm+10
                            print(" ")
                            print("Stormtroopers a désormais ", end="")
                            print(hp_storm, end="")
                            print(" HP.")
                            stamina_storm=0

                    #ATTAQUE:

                        if reponse_action==2:
                            print(" ")
                            print("Qui voulez-vous attaquer ?")
                            if hp_storm>0 and calcul_distance(x_storm, y_storm, x_luke, y_luke) <=4:
                                print("[1] Luke Skywalker | HP restant : ", end="")
                                print(hp_luke)
                            if hp_leia>0 and calcul_distance(x_storm, y_storm, x_leia, y_leia) <=4:
                                print("[2] Princesse Leia | HP restant : ", end="")
                                print(hp_leia)
                            if hp_han>0 and calcul_distance(x_storm, y_storm, x_han, y_han) <=4:
                                print("[3] Han Solo | HP restant : ", end="")
                                print(hp_han)
                            if hp_chew>0 and calcul_distance(x_storm, y_storm, x_chew, y_chew) <=4:
                                print("[4] Chewbacca | HP restant : ", end="")
                                print(hp_chew)
                            print("[0] Retour en arrière")
                            print(" ")
                            reponse_attaque=int(input("-> "))
                            
                            if reponse_attaque==0:
                                print(" ")
                            if reponse_attaque==1 and calcul_distance(x_luke, y_storm, x_luke, y_storm) <=4:
                                
                                print(" ")
                                print("Attaque contre Luke Skywalker, puissance de ", stamina_storm, " Stamina...")
                                for i in range(stamina_storm):
                                    puissance_attaque=range(1, 11)
                                    hp_storm=hp_storm-choice(puissance_attaque)
                                    print(" ")
                                print("Luke Skywalker a désormais ", end="")
                                print(hp_luke, end=" ")
                                print("HP.")
                                stamina_storm=0
                            if reponse_attaque==2 and calcul_distance(x_storm, y_storm, x_leia, y_leia) <=4:
                                print(" ")
                                print("Attaque contre Princesse Leia, puissance de ", stamina_storm, " Stamina...")
                                for i in range(stamina_storm):
                                    puissance_attaque=range(1, 11)
                                    hp_leia=hp_leia-choice(puissance_attaque)
                                    print(" ")
                                print("Princesse Leia a désormais ", end="")
                                print(hp_leia, end=" ")
                                print("HP.")
                                stamina_storm=0
                            if reponse_attaque==3 and calcul_distance(x_storm, y_storm, x_han, y_han) <=4:
                                print(" ")
                                print("Attaque contre Han Solo, puissance de ", stamina_storm, " Stamina...")
                                for i in range(stamina_storm):
                                    puissance_attaque=range(1, 11)
                                    hp_han=hp_han-choice(puissance_attaque)
                                    print(" ")
                                print("Han Solo ont désormais ", end="")
                                print(hp_han, end=" ")
                                print("HP.")
                                stamina_storm=0
                            if reponse_attaque==4 and calcul_distance(x_storm, y_storm, x_chew, y_chew) <=4:
                                print(" ")
                                print("Attaque contre Chewbacca, puissance de ", stamina_storm, " Stamina...")
                                for i in range(stamina_storm):
                                    puissance_attaque=range(1, 11)
                                    hp_chew=hp_chew-choice(puissance_attaque)
                                    print(" ")
                                print("Chewbacca a désormais ", end="")
                                print(hp_chew, end=" ")
                                print("HP.")
                                stamina_storm=0
            
                if reponse_unite_choisie==3 and hp_snow>0:

                    while stamina_snow>0:

                        print("-> Snowtroopers | Stamina : ", stamina_snow, " | Voulez vous :")
                        if hp_snow<50:
                            print("[1] Soin (10 HP)")
                        print("[2] Attaque")
                        print("[3] Déplacement")
                        print("[4] Passer le tour")
                        print(" ")

                        reponse_action=int(input("-> "))

                    #SOIN: OK

                        if reponse_action==1 and hp_snow<=59:
                            if hp_snow>50:
                                hp_snow=60
                            else:
                                hp_snow=hp_snow+10
                            print(" ")
                            print("Snowtroopers a désormais ", end="")
                            print(hp_snow, end="")
                            print(" HP.")
                            stamina_snow=0

                    #ATTAQUE:

                        if reponse_action==2:
                            print(" ")
                            print("Qui voulez-vous attaquer ?")
                            if hp_snow>0 and calcul_distance(x_snow, y_snow, x_luke, y_luke) <=4:
                                print("[1] Luke Skywalker | HP restant : ", end="")
                                print(hp_luke)
                            if hp_leia>0 and calcul_distance(x_snow, y_snow, x_leia, y_leia) <=4:
                                print("[2] Princesse Leia | HP restant : ", end="")
                                print(hp_leia)
                            if hp_han>0 and calcul_distance(x_snow, y_snow, x_han, y_han) <=4:
                                print("[3] Han Solo | HP restant : ", end="")
                                print(hp_han)
                            if hp_chew>0 and calcul_distance(x_snow, y_snow, x_chew, y_chew) <=4:
                                print("[4] Chewbacca | HP restant : ", end="")
                                print(hp_chew)
                            print("[0] Retour en arrière")
                            print(" ")
                            reponse_attaque=int(input("-> "))
                            
                            if reponse_attaque==0:
                                print(" ")
                            if reponse_attaque==1 and calcul_distance(x_luke, y_snow, x_luke, y_snow) <=4:
                                
                                print(" ")
                                print("Attaque contre Luke Skywalker, puissance de ", stamina_snow, " Stamina...")
                                for i in range(stamina_snow):
                                    puissance_attaque=range(1, 11)
                                    hp_snow=hp_snow-choice(puissance_attaque)
                                    print(" ")
                                print("Luke Skywalker a désormais ", end="")
                                print(hp_luke, end=" ")
                                print("HP.")
                                stamina_snow=0
                            if reponse_attaque==2 and calcul_distance(x_snow, y_snow, x_leia, y_leia) <=4:
                                print(" ")
                                print("Attaque contre Princesse Leia, puissance de ", stamina_snow, " Stamina...")
                                for i in range(stamina_snow):
                                    puissance_attaque=range(1, 11)
                                    hp_leia=hp_leia-choice(puissance_attaque)
                                    print(" ")
                                print("Princesse Leia a désormais ", end="")
                                print(hp_leia, end=" ")
                                print("HP.")
                                stamina_snow=0
                            if reponse_attaque==3 and calcul_distance(x_snow, y_snow, x_han, y_han) <=4:
                                print(" ")
                                print("Attaque contre Han Solo, puissance de ", stamina_snow, " Stamina...")
                                for i in range(stamina_snow):
                                    puissance_attaque=range(1, 11)
                                    hp_han=hp_han-choice(puissance_attaque)
                                    print(" ")
                                print("Han Solo ont désormais ", end="")
                                print(hp_han, end=" ")
                                print("HP.")
                                stamina_snow=0
                            if reponse_attaque==4 and calcul_distance(x_snow, y_snow, x_chew, y_chew) <=4:
                                print(" ")
                                print("Attaque contre Chewbacca, puissance de ", stamina_snow, " Stamina...")
                                for i in range(stamina_snow):
                                    puissance_attaque=range(1, 11)
                                    hp_chew=hp_chew-choice(puissance_attaque)
                                    print(" ")
                                print("Chewbacca a désormais ", end="")
                                print(hp_chew, end=" ")
                                print("HP.")
                                stamina_snow=0

                if reponse_unite_choisie==4 and hp_boba>0:

                    while stamina_boba>0:

                        print("-> Boba Fett | Stamina : ", stamina_boba, " | Voulez vous :")
                        if hp_boba<50:
                            print("[1] Soin (10 HP)")
                        print("[2] Attaque")
                        print("[3] Déplacement")
                        print("[4] Passer le tour")
                        print(" ")

                        reponse_action=int(input("-> "))

                    #SOIN: OK

                        if reponse_action==1 and hp_boba<=59:
                            if hp_boba>50:
                                hp_boba=60
                            else:
                                hp_boba=hp_boba+10
                            print(" ")
                            print("Boba Fett a désormais ", end="")
                            print(hp_boba, end="")
                            print(" HP.")
                            stamina_boba=0

                    #ATTAQUE:

                        if reponse_action==2:
                            print(" ")
                            print("Qui voulez-vous attaquer ?")
                            if hp_boba>0 and calcul_distance(x_boba, y_boba, x_luke, y_luke) <=4:
                                print("[1] Luke Skywalker | HP restant : ", end="")
                                print(hp_luke)
                            if hp_leia>0 and calcul_distance(x_boba, y_boba, x_leia, y_leia) <=4:
                                print("[2] Princesse Leia | HP restant : ", end="")
                                print(hp_leia)
                            if hp_han>0 and calcul_distance(x_boba, y_boba, x_han, y_han) <=4:
                                print("[3] Han Solo | HP restant : ", end="")
                                print(hp_han)
                            if hp_chew>0 and calcul_distance(x_boba, y_boba, x_chew, y_chew) <=4:
                                print("[4] Chewbacca | HP restant : ", end="")
                                print(hp_chew)
                            print("[0] Retour en arrière")
                            print(" ")
                            reponse_attaque=int(input("-> "))
                            
                            if reponse_attaque==0:
                                print(" ")
                            if reponse_attaque==1 and calcul_distance(x_luke, y_boba, x_luke, y_boba) <=4:
                                
                                print(" ")
                                print("Attaque contre Luke Skywalker, puissance de ", stamina_boba, " Stamina...")
                                for i in range(stamina_boba):
                                    puissance_attaque=range(1, 11)
                                    hp_boba=hp_boba-choice(puissance_attaque)
                                    print(" ")
                                print("Luke Skywalker a désormais ", end="")
                                print(hp_luke, end=" ")
                                print("HP.")
                                stamina_boba=0
                            if reponse_attaque==2 and calcul_distance(x_boba, y_boba, x_leia, y_leia) <=4:
                                print(" ")
                                print("Attaque contre Princesse Leia, puissance de ", stamina_boba, " Stamina...")
                                for i in range(stamina_boba):
                                    puissance_attaque=range(1, 11)
                                    hp_leia=hp_leia-choice(puissance_attaque)
                                    print(" ")
                                print("Princesse Leia a désormais ", end="")
                                print(hp_leia, end=" ")
                                print("HP.")
                                stamina_boba=0
                            if reponse_attaque==3 and calcul_distance(x_boba, y_boba, x_han, y_han) <=4:
                                print(" ")
                                print("Attaque contre Han Solo, puissance de ", stamina_boba, " Stamina...")
                                for i in range(stamina_boba):
                                    puissance_attaque=range(1, 11)
                                    hp_han=hp_han-choice(puissance_attaque)
                                    print(" ")
                                print("Han Solo ont désormais ", end="")
                                print(hp_han, end=" ")
                                print("HP.")
                                stamina_boba=0
                            if reponse_attaque==4 and calcul_distance(x_boba, y_boba, x_chew, y_chew) <=4:
                                print(" ")
                                print("Attaque contre Chewbacca, puissance de ", stamina_boba, " Stamina...")
                                for i in range(stamina_boba):
                                    puissance_attaque=range(1, 11)
                                    hp_chew=hp_chew-choice(puissance_attaque)
                                    print(" ")
                                print("Chewbacca a désormais ", end="")
                                print(hp_chew, end=" ")
                                print("HP.")
                                stamina_boba=0

    #FIN DU TOUR DE JEU

        #CHECK MORTS
        #CHECK VICTOIRE


            if not en_jeu==True:
                print("")
                print("Partie terminée.")
                print("A bientôt!")


    #PARAMETRES

    if reponse==2:
        print("")
        print("Paramètres :")
        print("[1] Quitter ce menu")
        print("[2] Changer la game seed")
#        print("[3]")
        reponsesettings=int(input("-> "))
        if reponsesettings==2:
            random.seed(int(input("Entrer une nouvelle seed : ")))
            print("Ok!")
        if reponsesettings==1:
            print(" ")
    if reponse==3:
        programme==False