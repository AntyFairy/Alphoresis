try:
    from random import *
    from math import *

    programme=True
    debug_mode=False

    def calcul_distance(x1, y1, x2, y2):
        ys=y1-y2
        xs=x1-x2
        distance=sqrt(ys*ys+xs*xs)
        return(distance)

    print("###")
    print("Project Alphoresis")
    print("Version 0.1.4  |  State : indev/ pre-release  |  Made with Python 3.11.1")
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
            print("[2] 1vE Combat de boss - Jabba's Rancor")
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
                        luke_en_vie=True
                        print("Vous avez choisi : Luke Skywalker!")
                    if unite_choisie==2:
                        hp_leia=40
                        leia_en_vie=True
                        print("Vous avez choisi : Princesse Leia!")
                    if unite_choisie==3:
                        hp_han=60
                        han_en_vie=True
                        print("Vous avez choisi : Han Solo!")
                    if unite_choisie==4:
                        hp_chew=60
                        chew_en_vie=True
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
                        vador_en_vie=True
                        print("Vous avez choisi : Dark Vador!")
                    if unite_choisie==2:
                        hp_storm=40
                        storm_en_vie=True
                        print("Vous avez choisi : Stormtroopers!")
                    if unite_choisie==3:
                        hp_snow=60
                        snow_en_vie=True
                        print("Vous avez choisi : Snowtroopers!")
                    if unite_choisie==4:
                        hp_boba=60
                        boba_en_vie=True
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
                                    brulure=range(1,3)
                                    if choice(brulure)==1:
                                        print(" ", "Activation de la capacité spéciale : Brûlure !", " ", " -3 HP !")
                                        hp_vador=hp_vador-3
                                    else:
                                        print(" ", "Échec de la capacité spéciale (Brûlure)...", " ")
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
                                    brulure=range(1,3)
                                    if choice(brulure)==1:
                                        print(" ", "Activation de la capacité spéciale : Brûlure !", " ", " -3 HP !")
                                        hp_storm=hp_storm-3
                                    else:
                                        print(" ", "Échec de la capacité spéciale (Brûlure)...", " ")
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
                                    brulure=range(1,3)
                                    if choice(brulure)==1:
                                        print(" ", "Activation de la capacité spéciale : Brûlure !", " ", " -3 HP !")
                                        hp_snow=hp_snow-3
                                    else:
                                        print(" ", "Échec de la capacité spéciale (Brûlure)...", " ")
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
                                    brulure=range(1,3)
                                    if choice(brulure)==1:
                                        print(" ", "Activation de la capacité spéciale : Brûlure !", " ", " -3 HP !")
                                        hp_boba=hp_boba-3
                                    else:
                                        print(" ", "Échec de la capacité spéciale (Brûlure)...", " ")
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

                    if hp_luke<1 and hp_leia<1 and hp_han<1 and hp_chew<1:
                        print(" ", "***", " ", "Fin de la partie ! Victoire de l'empire !", " ", "***", " ",)
                        en_jeu==False
                    if hp_vador<1 and hp_storm<1 and hp_snow<1 and hp_boba<1:
                        print(" ", "***", " ", "Fin de la partie ! Victoire des rebelles !", " ", "***", " ",)
                        en_jeu==False

                    if vador_en_vie==True and hp_vador<1:
                        vador_en_vie=False
                        print("Dark Vador a été éliminé !")
                    if storm_en_vie==True and hp_storm<1:
                        storm_en_vie=False
                        print("Stormtroopers ont été éliminés !")
                    if snow_en_vie==True and hp_snow<1:
                        snow_en_vie=False
                        print("Snowtroopers ont été éliminés !")
                    if boba_en_vie==True and hp_boba<1:
                        boba_en_vie=False
                        print("Boba Fett a été éliminé !")



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
                                if hp_vador>0 and calcul_distance(x_vador, y_vador, x_luke, y_luke) <=2:
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
                                if reponse_attaque==1 and calcul_distance(x_luke, y_luke, x_vador, y_vador) <=2:

                                    print(" ")
                                    print("Attaque contre Luke Skywalker, puissance de ", stamina_vador, " Stamina...")
                                    for i in range(stamina_vador):
                                        puissance_attaque=range(1, 11)
                                        hp_vador=hp_vador-choice(puissance_attaque)
                                        print(" ")
                                    brulure=range(1,3)
                                    if choice(brulure)==1:
                                        print(" ", "Activation de la capacité spéciale : Brûlure !", " ", " -3 HP !")
                                        hp_luke=hp_vador-3
                                    else:
                                        print(" ", "Échec de la capacité spéciale (Brûlure)...", " ")
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
                                    brulure=range(1,3)
                                    if choice(brulure)==1:
                                        print(" ", "Activation de la capacité spéciale : Brûlure !", " ", " -3 HP !")
                                        hp_leia=hp_leia-3
                                    else:
                                        print(" ", "Échec de la capacité spéciale (Brûlure)...", " ")
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
                                    brulure=range(1,3)
                                    if choice(brulure)==1:
                                        print(" ", "Activation de la capacité spéciale : Brûlure !", " ", " -3 HP !")
                                        hp_han=hp_han-3
                                    else:
                                        print(" ", "Échec de la capacité spéciale (Brûlure)...", " ")
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
                                    brulure=range(1,3)
                                    if choice(brulure)==1:
                                        print(" ", "Activation de la capacité spéciale : Brûlure !", " ", " -3 HP !")
                                        hp_chew=hp_chew-3
                                    else:
                                        print(" ", "Échec de la capacité spéciale (Brûlure)...", " ")
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

            #CHECK MORTS REBELLES
                    if luke_en_vie==True and hp_luke<1:
                        luke_en_vie=False
                        print("Luke Skywalker a été éliminé !")
                    if leia_en_vie==True and hp_leia<1:
                        leia_en_vie=False
                        print("Princesse Leia a été éliminée !")
                    if han_en_vie==True and hp_han<1:
                        han_en_vie=False
                        print("Han Solo a été éliminé !")
                    if chew_en_vie==True and hp_chew<1:
                        chew_en_vie=False
                        print("Chewbacca a été éliminé !")
                        print(" ")
                        print("Activation de la capacité spéciale Cri !")
                        print(" -3 HP à toutes les unités adverses !")
                        hp_boba=hp_boba-3
                        hp_vador=hp_vador-3
                        hp_snow=hp_snow-3
                        hp_storm=hp_storm-3
                        print(" ")
            #CHECK VICTOIRE

                    if hp_luke<1 and hp_leia<1 and hp_han<1 and hp_chew<1:
                        print(" ", "***", " ", "Fin de la partie ! Victoire de l'empire !", " ", "***", " ",)
                        en_jeu==False
                    if hp_vador<1 and hp_storm<1 and hp_snow<1 and hp_boba<1:
                        print(" ", "***", " ", "Fin de la partie ! Victoire des rebelles !", " ", "***", " ",)
                        en_jeu==False


                if not en_jeu==True:
                    print("")
                    print("Partie terminée.")
                    print("A bientôt!")

            if choix_mode_de_jeu==2:
                print(" ")
                print("1vE Combat de boss - Jabba's Rancor | Partie lancée !")
                print(" ")
                en_jeu=True
                print("---")
                print(" ")
                #choix des unités
                print("Choix des 3 unités :")
                print(" ")
                print("[1] Luke Skywalker | HP: 60 | Stamina: 4 | Portée: Corps-à-corps")
                print("[2] Princesse Leia | HP: 40 | Stamina: 4 | Portée: à distance")
                print("[3] Han Solo       | HP: 60 | Stamina: 3 | Portée: à distance")
                print("[4] Chewbacca      | HP: 60 | Stamina: 2 | Portée: à distance")
                print("[5] Dark Vador     | HP: 60 | Stamina: 4 | Portée: Corps-à-corps")
                print("[6] Stormtroopers  | HP: 40 | Stamina: 4 | Portée: à distance")
                print("[7] Snowtroopers   | HP: 60 | Stamina: 3 | Portée: à distance")
                print("[8] Boba Fett      | HP: 60 | Stamina: 2 | Portée: à distance")
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
                        hp_luke=60
                        luke_en_vie=True
                        print("Vous avez choisi : Luke Skywalker!")
                    if unite_choisie==2:
                        hp_leia=40
                        leia_en_vie=True
                        print("Vous avez choisi : Princesse Leia!")
                    if unite_choisie==3:
                        hp_han=60
                        han_en_vie=True
                        print("Vous avez choisi : Han Solo!")
                    if unite_choisie==4:
                        hp_chew=60
                        chew_en_vie=True
                        print("Vous avez choisi : Chewbacca!")
                    if unite_choisie==5:
                        hp_vador=60
                        vador_en_vie=True
                        print("Vous avez choisi : Dark Vador!")
                    if unite_choisie==6:
                        hp_storm=40
                        storm_en_vie=True
                        print("Vous avez choisi : Stormtroopers!")
                    if unite_choisie==7:
                        hp_snow=60
                        snow_en_vie=True
                        print("Vous avez choisi : Snowtroopers!")
                    if unite_choisie==8:
                        hp_boba=60
                        boba_en_vie=True
                        print("Vous avez choisi : Boba Fett!")

                hp_rancor=110
                x_rancor=5
                y_rancor=5
                RancorSuperAttackCooldown=3
                DistanceUnitBossLaPlusFaible=100
                UnitPlusProcheDuBoss=1

                #début tour de jeu
                while en_jeu==True:
                    #infos en direct+calcul des distances unit/boss
                    print(" ")
                    print(" [BOSS] Jabba's Rancor | HP restants : ", hp_rancor, " | X=4 ; Y=4")
                    print(" ")
                    if hp_luke>0:
                        print("~ Luke Skywalker   | HP restants : ", hp_luke, " | X=", x_luke, " ; Y=", y_luke)
                        if calcul_distance(x_rancor, y_rancor, x_luke, y_luke) < DistanceUnitBossLaPlusFaible:
                            DistanceUnitBossLaPlusFaible=calcul_distance(x_rancor, y_rancor, x_luke, y_luke)
                            UnitPlusProcheDuBoss=1
                    if hp_leia>0:
                        print("~ Princesse Leia   | HP restants : ", hp_leia, " | X=", x_leia, " ; Y=", y_leia)
                        if calcul_distance(x_rancor, y_rancor, x_leia, y_leia) < DistanceUnitBossLaPlusFaible:
                            DistanceUnitBossLaPlusFaible=calcul_distance(x_rancor, y_rancor, x_leia, y_leia)
                            UnitPlusProcheDuBoss=2
                    if hp_han>0:
                        print("~ Han Solo         | HP restants : ", hp_han, " | X=", x_han, " ; Y=", y_han)
                        if calcul_distance(x_rancor, y_rancor, x_han, y_han) < DistanceUnitBossLaPlusFaible:
                            DistanceUnitBossLaPlusFaible=calcul_distance(x_rancor, y_rancor, x_han, y_han)
                            UnitPlusProcheDuBoss=3
                    if hp_chew>0:
                        print("~ Chewbacca        | HP restants : ", hp_chew, " | X=", x_chew, " ; Y=", y_chew)
                        if calcul_distance(x_rancor, y_rancor, x_chew, y_chew) < DistanceUnitBossLaPlusFaible:
                            DistanceUnitBossLaPlusFaible=calcul_distance(x_rancor, y_rancor, x_luke, y_luke)
                            UnitPlusProcheDuBoss=4
                    if hp_vador>0:
                        print("~ Dark Vador       | HP restants : ", hp_vador, " | X=", x_vador, " ; Y=", y_vador)
                        if calcul_distance(x_rancor, y_rancor, x_vador, y_vador) < DistanceUnitBossLaPlusFaible:
                            DistanceUnitBossLaPlusFaible=calcul_distance(x_rancor, y_rancor, x_vador, y_vador)
                            UnitPlusProcheDuBoss=5
                    if hp_storm>0:
                        print("~ Stormtroopers    | HP restants : ", hp_storm, " | X=", x_storm, " ; Y=", y_storm)
                        if calcul_distance(x_rancor, y_rancor, x_storm, y_storm) < DistanceUnitBossLaPlusFaible:
                            DistanceUnitBossLaPlusFaible=calcul_distance(x_rancor, y_rancor, x_storm, y_storm)
                            UnitPlusProcheDuBoss=6
                    if hp_snow>0:
                        print("~ Snowtroopers     | HP restants : ", hp_snow, " | X=", x_snow, " ; Y=", y_snow)
                        if calcul_distance(x_rancor, y_rancor, x_snow, y_snow) < DistanceUnitBossLaPlusFaible:
                            DistanceUnitBossLaPlusFaible=calcul_distance(x_rancor, y_rancor, x_snow, y_snow)
                            UnitPlusProcheDuBoss=7
                    if hp_boba>0:
                        print("~ Boba Fett        | HP restants : ", hp_boba, " | X=", x_boba, " ; Y=", y_boba)
                        if calcul_distance(x_rancor, y_rancor, x_boba, y_boba) < DistanceUnitBossLaPlusFaible:
                            DistanceUnitBossLaPlusFaible=calcul_distance(x_rancor, y_rancor, x_boba, y_boba)
                            UnitPlusProcheDuBoss=8
                    print("")

                    #attaque du joueur

                    print(" ")
                    print("Choisissez une unité à utiliser !")
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

                    reponse_unite_choisie=int(input("-> "))

                    if reponse_unite_choisie==1 and hp_luke>0:
                        stamina_luke=4
                        while stamina_luke>0:

                            print("-> Luke Skywalker | Stamina : ", stamina_luke, " | Voulez vous :")
                            if hp_luke<60:
                                print("[1] Soin (10 HP)")
                            if calcul_distance(x_rancor, y_rancor, x_luke, y_luke)<=2:

                                print("[2] Attaquer le boss")
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

                            if reponse_unite_choisie==2 and hp_leia>0:
                                stamina_leia=4
                                while stamina_leia>0:

                                    print("-> La Princesse Leia | Stamina : ", stamina_leia, " | Voulez vous :")
                                    if hp_leia<40:
                                        print("[1] Soin (10 HP)")
                                    if calcul_distance(x_rancor, y_rancor, x_leia, y_leia)<=4:

                                        print("[2] Attaquer le boss")
                                    print("[3] Déplacement")
                                    print("[4] Passer le tour")
                                    print(" ")

                                    reponse_action=int(input("-> "))

                                #SOIN: OK

                                    if reponse_action==1 and hp_leia<=39:
                                        if hp_leia>30:
                                            hp_leia=40
                                        else:
                                            hp_leia=hp_leia+10
                                        print(" ")
                                        print("La Princesse Leia a désormais ", end="")
                                        print(hp_leia, end="")
                                        print(" HP.")
                                        stamina_leia=0

                                #ATTAQUE:

                                    if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_leia, y_leia)<=4:
                                        print(" ")
                                        puissance_attaque=range(1, 11)
                                        hp_rancor=hp_rancor-choice(puissance_attaque)
                                        print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
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
                                            print("La Princesse Leia est désormais en X=", end=" ")
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
                                stamina_han=3
                                while stamina_han>0:

                                    print("-> Han Solo | Stamina : ", stamina_han, " | Voulez vous :")
                                    if hp_han<60:
                                        print("[1] Soin (10 HP)")
                                    if calcul_distance(x_rancor, y_rancor, x_han, y_han)<=4:

                                        print("[2] Attaquer le boss")
                                    print("[3] Déplacement")
                                    print("[4] Passer le tour")
                                    print(" ")

                                    reponse_action=int(input("-> "))

                                #SOIN: OK

                                    if reponse_action==1 and hp_han<=39:
                                        if hp_han>49:
                                            hp_han=60
                                        else:
                                            hp_han=hp_han+10
                                        print(" ")
                                        print("Han Solo a désormais ", end="")
                                        print(hp_han, end="")
                                        print(" HP.")
                                        stamina_han=0

                                #ATTAQUE:

                                    if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_han, y_han)<=4:
                                        print(" ")
                                        puissance_attaque=range(1, 11)
                                        hp_rancor=hp_rancor-choice(puissance_attaque)
                                        print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
                                        stamina_han=0


                                #DÉPLACEMENT: OK

                                    if reponse_action==3:
                                        print(" ")
                                        print("Déplacement (3 cases par stamina)")
                                        print(" ")
                                        x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                                        y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                                        print(" ")
                                        distance_entre_voulue_et_actuelle=calcul_distance(x_han, y_han, x_deplacement_voulu, y_deplacement_voulu)
                                        if  distance_entre_voulue_et_actuelle <= 3*stamina_han:
                                            if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                                x_han=x_deplacement_voulu
                                                y_han=y_deplacement_voulu
                                                stamina_han=stamina_han - 1
                                            if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                                x_han=x_deplacement_voulu
                                                y_han=y_deplacement_voulu
                                                stamina_han=stamina_han - 2
                                            if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                                x_han=x_deplacement_voulu
                                                y_han=y_deplacement_voulu
                                                stamina_han=stamina_han - 3
                                            if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                                x_han=x_deplacement_voulu
                                                y_han=y_deplacement_voulu
                                                stamina_han=stamina_han - 4
                                            print("Han Solo est désormais en X=", end=" ")
                                            print(x_han)
                                            print(", Y=", end=" ")
                                            print(y_han)
                                        else:
                                            print(" ")
                                            print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                                #PASSER LE TOUR: OK
                                    if reponse_action==4:
                                        stamina_han=0

                            if reponse_unite_choisie==4 and hp_chew>0:
                                stamina_chew=2
                                while stamina_chew>0:

                                    print("-> Chewbacca | Stamina : ", stamina_chew, " | Voulez vous :")
                                    if hp_chew<60:
                                        print("[1] Soin (10 HP)")
                                    if calcul_distance(x_rancor, y_rancor, x_chew, y_chew)<=4:

                                        print("[2] Attaquer le boss")
                                    print("[3] Déplacement")
                                    print("[4] Passer le tour")
                                    print(" ")

                                    reponse_action=int(input("-> "))

                                #SOIN: OK

                                    if reponse_action==1 and hp_chew<=39:
                                        if hp_chew>49:
                                            hp_chew=60
                                        else:
                                            hp_chew=hp_chew+10
                                        print(" ")
                                        print("Chewbacca a désormais ", end="")
                                        print(hp_chew, end="")
                                        print(" HP.")
                                        stamina_chew=0

                                #ATTAQUE:

                                    if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_chew, y_chew)<=4:
                                        print(" ")
                                        puissance_attaque=range(1, 11)
                                        hp_rancor=hp_rancor-choice(puissance_attaque)
                                        print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
                                        stamina_chew=0


                                #DÉPLACEMENT: OK

                                    if reponse_action==3:
                                        print(" ")
                                        print("Déplacement (3 cases par stamina)")
                                        print(" ")
                                        x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                                        y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                                        print(" ")
                                        distance_entre_voulue_et_actuelle=calcul_distance(x_chew, y_chew, x_deplacement_voulu, y_deplacement_voulu)
                                        if  distance_entre_voulue_et_actuelle <= 3*stamina_chew:
                                            if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                                x_chew=x_deplacement_voulu
                                                y_chew=y_deplacement_voulu
                                                stamina_chew=stamina_chew - 1
                                            if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                                x_chew=x_deplacement_voulu
                                                y_chew=y_deplacement_voulu
                                                stamina_chew=stamina_chew - 2
                                            if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                                x_chew=x_deplacement_voulu
                                                y_chew=y_deplacement_voulu
                                                stamina_chew=stamina_chew - 3
                                            if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                                x_chew=x_deplacement_voulu
                                                y_chew=y_deplacement_voulu
                                                stamina_chew=stamina_chew - 4
                                            print("Chewbacca est désormais en X=", end=" ")
                                            print(x_chew)
                                            print(", Y=", end=" ")
                                            print(y_chew)
                                        else:
                                            print(" ")
                                            print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                                #PASSER LE TOUR: OK
                                    if reponse_action==4:
                                        stamina_chew=0



                        #ATTAQUE:


                            if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_luke, y_luke)<=2:
                                print(" ")
                                puissance_attaque=range(1, 11)
                                hp_rancor=hp_rancor-choice(puissance_attaque)
                                print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
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
                        stamina_leia=4
                        while stamina_leia>0:

                            print("-> Princesse Leia | Stamina : ", stamina_leia, " | Voulez vous :")
                            if hp_leia<40:
                                print("[1] Soin (10 HP)")
                            if calcul_distance(x_rancor, y_rancor, x_leia, y_leia)<=4:
                                    
                                print("[2] Attaquer le boss")
                            print("[3] Déplacement")
                            print("[4] Passer le tour")
                            print(" ")

                            reponse_action=int(input("-> "))

                        #SOIN: OK

                            if reponse_action==1 and hp_leia<=39:
                                if hp_leia>29:
                                    hp_leia=40
                                else:
                                    hp_leia=hp_leia+10
                                print(" ")
                                print("Princesse Leia a désormais ", end="")
                                print(hp_leia, end="")
                                print(" HP.")
                                stamina_leia=0

                        #ATTAQUE:

                            if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_leia, y_leia)<=4:
                                print(" ")
                                puissance_attaque=range(1, 11)
                                hp_rancor=hp_rancor-choice(puissance_attaque)
                                print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
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
                                    print("Princesse Leia est désormais en X=", end=" ")
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
                        stamina_han=3
                        while stamina_han>0:

                            print("-> Han Solo | Stamina : ", stamina_han, " | Voulez vous :")
                            if hp_han<60:
                                print("[1] Soin (10 HP)")
                            if calcul_distance(x_rancor, y_rancor, x_han, y_han)<=4:
                                    
                                print("[2] Attaquer le boss")
                            print("[3] Déplacement")
                            print("[4] Passer le tour")
                            print(" ")

                            reponse_action=int(input("-> "))

                        #SOIN: OK

                            if reponse_action==1 and hp_han<=59:
                                if hp_han>49:
                                    hp_han=60
                                else:
                                    hp_han=hp_han+10
                                print(" ")
                                print("Han Solo a désormais ", end="")
                                print(hp_han, end="")
                                print(" HP.")
                                stamina_han=0

                        #ATTAQUE:

                            if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_han, y_han)<=4:
                                print(" ")
                                puissance_attaque=range(1, 11)
                                hp_rancor=hp_rancor-choice(puissance_attaque)
                                print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
                                stamina_han=0
                                
                        
                        #DÉPLACEMENT: OK

                            if reponse_action==3:
                                print(" ")
                                print("Déplacement (3 cases par stamina)")
                                print(" ")
                                x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                                y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                                print(" ")
                                distance_entre_voulue_et_actuelle=calcul_distance(x_han, y_han, x_deplacement_voulu, y_deplacement_voulu)
                                if  distance_entre_voulue_et_actuelle <= 3*stamina_han:
                                    if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                        x_han=x_deplacement_voulu
                                        y_han=y_deplacement_voulu
                                        stamina_han=stamina_han - 1
                                    if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                        x_han=x_deplacement_voulu
                                        y_han=y_deplacement_voulu
                                        stamina_han=stamina_han - 2
                                    if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                        x_han=x_deplacement_voulu
                                        y_han=y_deplacement_voulu
                                        stamina_han=stamina_han - 3
                                    if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                        x_han=x_deplacement_voulu
                                        y_han=y_deplacement_voulu
                                        stamina_han=stamina_han - 4
                                    print("Han Solo est désormais en X=", end=" ")
                                    print(x_han)
                                    print(", Y=", end=" ")
                                    print(y_han)
                                else:
                                    print(" ")
                                    print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                        #PASSER LE TOUR: OK
                            if reponse_action==4:
                                stamina_han=0

                    if reponse_unite_choisie==4 and hp_chew>0:

                        stamina_chew=2
                        while stamina_chew>0:

                            print("-> Chewbacca | Stamina : ", stamina_chew, " | Voulez vous :")
                            if hp_chew<60:
                                print("[1] Soin (10 HP)")
                            if calcul_distance(x_rancor, y_rancor, x_chew, y_chew)<=4:
                                    
                                print("[2] Attaquer le boss")
                            print("[3] Déplacement")
                            print("[4] Passer le tour")
                            print(" ")

                            reponse_action=int(input("-> "))

                        #SOIN: OK

                            if reponse_action==1 and hp_chew<=59:
                                if hp_chew>49:
                                    hp_chew=60
                                else:
                                    hp_chew=hp_chew+10
                                print(" ")
                                print("Chewbacca a désormais ", end="")
                                print(hp_chew, end="")
                                print(" HP.")
                                stamina_chew=0

                        #ATTAQUE:

                            if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_chew, y_chew)<=4:
                                print(" ")
                                puissance_attaque=range(1, 11)
                                hp_rancor=hp_rancor-choice(puissance_attaque)
                                print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
                                stamina_chew=0
                                
                        
                        #DÉPLACEMENT: OK

                            if reponse_action==3:
                                print(" ")
                                print("Déplacement (3 cases par stamina)")
                                print(" ")
                                x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                                y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                                print(" ")
                                distance_entre_voulue_et_actuelle=calcul_distance(x_chew, y_chew, x_deplacement_voulu, y_deplacement_voulu)
                                if  distance_entre_voulue_et_actuelle <= 3*stamina_chew:
                                    if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                        x_chew=x_deplacement_voulu
                                        y_chew=y_deplacement_voulu
                                        stamina_chew=stamina_chew - 1
                                    if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                        x_chew=x_deplacement_voulu
                                        y_chew=y_deplacement_voulu
                                        stamina_chew=stamina_chew - 2
                                    if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                        x_chew=x_deplacement_voulu
                                        y_chew=y_deplacement_voulu
                                        stamina_chew=stamina_chew - 3
                                    if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                        x_chew=x_deplacement_voulu
                                        y_chew=y_deplacement_voulu
                                        stamina_chew=stamina_chew - 4
                                    print("Chewbacca est désormais en X=", end=" ")
                                    print(x_chew)
                                    print(", Y=", end=" ")
                                    print(y_chew)
                                else:
                                    print(" ")
                                    print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                        #PASSER LE TOUR: OK
                            if reponse_action==4:
                                stamina_chew=0

                    if reponse_unite_choisie==5 and hp_vador>0:
                        stamina_vador=4
                        while stamina_vador>0:

                            print("-> Dark Vador | Stamina : ", stamina_vador, " | Voulez vous :")
                            if hp_vador<60:
                                print("[1] Soin (10 HP)")
                            if calcul_distance(x_rancor, y_rancor, x_vador, y_vador)<=2:
                                    
                                print("[2] Attaquer le boss")
                            print("[3] Déplacement")
                            print("[4] Passer le tour")
                            print(" ")

                            reponse_action=int(input("-> "))

                        #SOIN: OK

                            if reponse_action==1 and hp_vador<=59:
                                if hp_vador>49:
                                    hp_vador=60
                                else:
                                    hp_vador=hp_vador+10
                                print(" ")
                                print("Dark Vador a désormais ", end="")
                                print(hp_vador, end="")
                                print(" HP.")
                                stamina_vador=0

                        #ATTAQUE:

                            if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_vador, y_vador)<=2:
                                print(" ")
                                puissance_attaque=range(1, 11)
                                hp_rancor=hp_rancor-choice(puissance_attaque)
                                print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
                                stamina_vador=0
                                
                        
                        #DÉPLACEMENT: OK

                            if reponse_action==3:
                                print(" ")
                                print("Déplacement (3 cases par stamina)")
                                print(" ")
                                x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                                y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                                print(" ")
                                distance_entre_voulue_et_actuelle=calcul_distance(x_vador, y_vador, x_deplacement_voulu, y_deplacement_voulu)
                                if  distance_entre_voulue_et_actuelle <= 3*stamina_vador:
                                    if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                        x_vador=x_deplacement_voulu
                                        y_vador=y_deplacement_voulu
                                        stamina_vador=stamina_vador - 1
                                    if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                        x_vador=x_deplacement_voulu
                                        y_vador=y_deplacement_voulu
                                        stamina_vador=stamina_vador - 2
                                    if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                        x_vador=x_deplacement_voulu
                                        y_vador=y_deplacement_voulu
                                        stamina_vador=stamina_vador - 3
                                    if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                        x_vador=x_deplacement_voulu
                                        y_vador=y_deplacement_voulu
                                        stamina_vador=stamina_vador - 4
                                    print("Dark Vador est désormais en X=", end=" ")
                                    print(x_vador)
                                    print(", Y=", end=" ")
                                    print(y_vador)
                                else:
                                    print(" ")
                                    print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                        #PASSER LE TOUR: OK
                            if reponse_action==4:
                                stamina_vador=0

                    if reponse_unite_choisie==6 and hp_storm>0:
                        stamina_storm=4
                        while stamina_storm>0:

                            print("-> Stormtroopers | Stamina : ", stamina_storm, " | Voulez vous :")
                            if hp_storm<40:
                                print("[1] Soin (10 HP)")
                            if calcul_distance(x_rancor, y_rancor, x_storm, y_storm)<=4:
                                    
                                print("[2] Attaquer le boss")
                            print("[3] Déplacement")
                            print("[4] Passer le tour")
                            print(" ")

                            reponse_action=int(input("-> "))

                        #SOIN: OK

                            if reponse_action==1 and hp_storm<=39:
                                if hp_storm>29:
                                    hp_storm=40
                                else:
                                    hp_storm=hp_storm+10
                                print(" ")
                                print("Stormtroopers a désormais ", end="")
                                print(hp_storm, end="")
                                print(" HP.")
                                stamina_storm=0

                        #ATTAQUE:

                            if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_storm, y_storm)<=4:
                                print(" ")
                                puissance_attaque=range(1, 11)
                                hp_rancor=hp_rancor-choice(puissance_attaque)
                                print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
                                stamina_storm=0
                                
                        
                        #DÉPLACEMENT: OK

                            if reponse_action==3:
                                print(" ")
                                print("Déplacement (3 cases par stamina)")
                                print(" ")
                                x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                                y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                                print(" ")
                                distance_entre_voulue_et_actuelle=calcul_distance(x_storm, y_storm, x_deplacement_voulu, y_deplacement_voulu)
                                if  distance_entre_voulue_et_actuelle <= 3*stamina_storm:
                                    if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                        x_storm=x_deplacement_voulu
                                        y_storm=y_deplacement_voulu
                                        stamina_storm=stamina_storm - 1
                                    if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                        x_storm=x_deplacement_voulu
                                        y_storm=y_deplacement_voulu
                                        stamina_storm=stamina_storm - 2
                                    if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                        x_storm=x_deplacement_voulu
                                        y_storm=y_deplacement_voulu
                                        stamina_storm=stamina_storm - 3
                                    if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                        x_storm=x_deplacement_voulu
                                        y_storm=y_deplacement_voulu
                                        stamina_storm=stamina_storm - 4
                                    print("Stormtroopers est désormais en X=", end=" ")
                                    print(x_storm)
                                    print(", Y=", end=" ")
                                    print(y_storm)
                                else:
                                    print(" ")
                                    print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                        #PASSER LE TOUR: OK
                            if reponse_action==4:
                                stamina_storm=0


                        stamina_storm=3
                        while stamina_storm>0:

                            print("-> Stormtroopers | Stamina : ", stamina_storm, " | Voulez vous :")
                            if hp_storm<60:
                                print("[1] Soin (10 HP)")
                            if calcul_distance(x_rancor, y_rancor, x_storm, y_storm)<=4:
                                    
                                print("[2] Attaquer le boss")
                            print("[3] Déplacement")
                            print("[4] Passer le tour")
                            print(" ")

                            reponse_action=int(input("-> "))

                        #SOIN: OK

                            if reponse_action==1 and hp_storm<=59:
                                if hp_storm>49:
                                    hp_storm=60
                                else:
                                    hp_storm=hp_storm+10
                                print(" ")
                                print("Stormtroopers a désormais ", end="")
                                print(hp_storm, end="")
                                print(" HP.")
                                stamina_storm=0

                        #ATTAQUE:

                            if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_storm, y_storm)<=4:
                                print(" ")
                                puissance_attaque=range(1, 11)
                                hp_rancor=hp_rancor-choice(puissance_attaque)
                                print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
                                stamina_storm=0
                                
                        
                        #DÉPLACEMENT: OK

                            if reponse_action==3:
                                print(" ")
                                print("Déplacement (3 cases par stamina)")
                                print(" ")
                                x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                                y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                                print(" ")
                                distance_entre_voulue_et_actuelle=calcul_distance(x_storm, y_storm, x_deplacement_voulu, y_deplacement_voulu)
                                if  distance_entre_voulue_et_actuelle <= 3*stamina_storm:
                                    if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                        x_storm=x_deplacement_voulu
                                        y_storm=y_deplacement_voulu
                                        stamina_storm=stamina_storm - 1
                                    if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                        x_storm=x_deplacement_voulu
                                        y_storm=y_deplacement_voulu
                                        stamina_storm=stamina_storm - 2
                                    if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                        x_storm=x_deplacement_voulu
                                        y_storm=y_deplacement_voulu
                                        stamina_storm=stamina_storm - 3
                                    if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                        x_storm=x_deplacement_voulu
                                        y_storm=y_deplacement_voulu
                                        stamina_storm=stamina_storm - 4
                                    print("Stormtroopers est désormais en X=", end=" ")
                                    print(x_storm)
                                    print(", Y=", end=" ")
                                    print(y_storm)
                                else:
                                    print(" ")
                                    print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                        #PASSER LE TOUR: OK
                            if reponse_action==4:
                                stamina_storm=0

                    if reponse_unite_choisie==7 and hp_snow>0:
                        stamina_snow=3
                        while stamina_snow>0:

                            print("-> Snowtroopers | Stamina : ", stamina_snow, " | Voulez vous :")
                            if hp_snow<60:
                                print("[1] Soin (10 HP)")
                            if calcul_distance(x_rancor, y_rancor, x_snow, y_snow)<=4:
                                    
                                print("[2] Attaquer le boss")
                            print("[3] Déplacement")
                            print("[4] Passer le tour")
                            print(" ")

                            reponse_action=int(input("-> "))

                        #SOIN: OK

                            if reponse_action==1 and hp_snow<=59:
                                if hp_snow>49:
                                    hp_snow=60
                                else:
                                    hp_snow=hp_snow+10
                                print(" ")
                                print("Snowtroopers a désormais ", end="")
                                print(hp_snow, end="")
                                print(" HP.")
                                stamina_snow=0

                        #ATTAQUE:

                            if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_snow, y_snow)<=4:
                                print(" ")
                                puissance_attaque=range(1, 11)
                                hp_rancor=hp_rancor-choice(puissance_attaque)
                                print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
                                stamina_snow=0
                                
                        
                        #DÉPLACEMENT: OK

                            if reponse_action==3:
                                print(" ")
                                print("Déplacement (3 cases par stamina)")
                                print(" ")
                                x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                                y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                                print(" ")
                                distance_entre_voulue_et_actuelle=calcul_distance(x_snow, y_snow, x_deplacement_voulu, y_deplacement_voulu)
                                if  distance_entre_voulue_et_actuelle <= 3*stamina_snow:
                                    if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                        x_snow=x_deplacement_voulu
                                        y_snow=y_deplacement_voulu
                                        stamina_snow=stamina_snow - 1
                                    if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                        x_snow=x_deplacement_voulu
                                        y_snow=y_deplacement_voulu
                                        stamina_snow=stamina_snow - 2
                                    if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                        x_snow=x_deplacement_voulu
                                        y_snow=y_deplacement_voulu
                                        stamina_snow=stamina_snow - 3
                                    if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                        x_snow=x_deplacement_voulu
                                        y_snow=y_deplacement_voulu
                                        stamina_snow=stamina_snow - 4
                                    print("Snowtroopers est désormais en X=", end=" ")
                                    print(x_snow)
                                    print(", Y=", end=" ")
                                    print(y_snow)
                                else:
                                    print(" ")
                                    print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                        #PASSER LE TOUR: OK
                            if reponse_action==4:
                                stamina_snow=0

                    if reponse_unite_choisie==8 and hp_boba>0:
                        stamina_boba=2
                        while stamina_boba>0:

                            print("-> Boba Fett | Stamina : ", stamina_boba, " | Voulez vous :")
                            if hp_boba<60:
                                print("[1] Soin (10 HP)")
                            if calcul_distance(x_rancor, y_rancor, x_boba, y_boba)<=4:
                                    
                                print("[2] Attaquer le boss")
                            print("[3] Déplacement")
                            print("[4] Passer le tour")
                            print(" ")

                            reponse_action=int(input("-> "))

                        #SOIN: OK

                            if reponse_action==1 and hp_boba<=59:
                                if hp_boba>49:
                                    hp_boba=60
                                else:
                                    hp_boba=hp_boba+10
                                print(" ")
                                print("Boba Fett a désormais ", end="")
                                print(hp_boba, end="")
                                print(" HP.")
                                stamina_boba=0

                        #ATTAQUE:

                            if reponse_action==2 and calcul_distance(x_rancor, y_rancor, x_boba, y_boba)<=4:
                                print(" ")
                                puissance_attaque=range(1, 11)
                                hp_rancor=hp_rancor-choice(puissance_attaque)
                                print("Le boss a bien été attaqué ! HP restants : ", hp_rancor)
                                stamina_boba=0
                                
                        
                        #DÉPLACEMENT: OK

                            if reponse_action==3:
                                print(" ")
                                print("Déplacement (3 cases par stamina)")
                                print(" ")
                                x_deplacement_voulu=int(input("Indiquer la coordonnée X choisie -> "))
                                y_deplacement_voulu=int(input("Indiquer la coordonnée Y choisie -> "))
                                print(" ")
                                distance_entre_voulue_et_actuelle=calcul_distance(x_boba, y_boba, x_deplacement_voulu, y_deplacement_voulu)
                                if  distance_entre_voulue_et_actuelle <= 3*stamina_boba:
                                    if distance_entre_voulue_et_actuelle <=3 and distance_entre_voulue_et_actuelle > 0:
                                        x_boba=x_deplacement_voulu
                                        y_boba=y_deplacement_voulu
                                        stamina_boba=stamina_boba - 1
                                    if distance_entre_voulue_et_actuelle <=6 and distance_entre_voulue_et_actuelle > 3:
                                        x_boba=x_deplacement_voulu
                                        y_boba=y_deplacement_voulu
                                        stamina_boba=stamina_boba - 2
                                    if distance_entre_voulue_et_actuelle <=9 and distance_entre_voulue_et_actuelle > 6:
                                        x_boba=x_deplacement_voulu
                                        y_boba=y_deplacement_voulu
                                        stamina_boba=stamina_boba - 3
                                    if distance_entre_voulue_et_actuelle <=12 and distance_entre_voulue_et_actuelle > 9:
                                        x_boba=x_deplacement_voulu
                                        y_boba=y_deplacement_voulu
                                        stamina_boba=stamina_boba - 4
                                    print("Boba Fett est désormais en X=", end=" ")
                                    print(x_boba)
                                    print(", Y=", end=" ")
                                    print(y_boba)
                                else:
                                    print(" ")
                                    print("Il y a eu un problème. La distance est probablement trop élevée pour le stamina restant de cette unité.")


                        #PASSER LE TOUR: OK
                            if reponse_action==4:
                                stamina_boba=0

                    print(" ")
                    #rancor's attack
                    if RancorSuperAttackCooldown==0:
                        ("Le Rancor utilise son attaque spéciale et inflige 10 HP à toutes les unités !")
                        print(" ")
                        RancorSuperAttackCooldown=3
                        hp_luke -=10
                        hp_leia -=10
                        hp_han -=10
                        hp_chew -=10
                        hp_vador -=10
                        hp_storm -=10
                        hp_snow -=10
                        hp_boba -=10

                    elif UnitPlusProcheDuBoss==1:
                        RancorSuperAttackCooldown=RancorSuperAttackCooldown-1
                        print("Le Rancor attaque Luke Skywalker ! -15 HP !")
                        print(" ")
                        hp_luke -=15
                    elif UnitPlusProcheDuBoss==2:
                        RancorSuperAttackCooldown=RancorSuperAttackCooldown-1
                        print("Le Rancor attaque la Princesse Leia ! -15 HP !")
                        print(" ")
                        hp_leia -=15
                    elif UnitPlusProcheDuBoss==3:
                        RancorSuperAttackCooldown=RancorSuperAttackCooldown-1
                        print("Le Rancor attaque Han Solo ! -15 HP !")
                        print(" ")
                        hp_han -=15
                    elif UnitPlusProcheDuBoss==4:
                        RancorSuperAttackCooldown=RancorSuperAttackCooldown-1
                        print("Le Rancor attaque Chewbacca ! -15 HP !")
                        print(" ")
                        hp_chew -=15
                    elif UnitPlusProcheDuBoss==5:
                        RancorSuperAttackCooldown=RancorSuperAttackCooldown-1
                        print("Le Rancor attaque Dark Vador ! -15 HP !")
                        print(" ")
                        hp_vador -=15
                    elif UnitPlusProcheDuBoss==6:
                        RancorSuperAttackCooldown=RancorSuperAttackCooldown-1
                        print("Le Rancor attaque les Stormtroopers ! -15 HP !")
                        print(" ")
                        hp_storm -=15
                    elif UnitPlusProcheDuBoss==7:
                        RancorSuperAttackCooldown=RancorSuperAttackCooldown-1
                        print("Le Rancor attaque les Snowtroopers ! -15 HP !")
                        print(" ")
                        hp_snow -=15
                    elif UnitPlusProcheDuBoss==8:
                        RancorSuperAttackCooldown=RancorSuperAttackCooldown-1
                        print("Le Rancor attaque Boba Fett ! -15 HP !")
                        print(" ")
                        hp_boba -=15

                    #check fin du jeu
                    if hp_rancor<1:
                        en_jeu==False
                        print(" ")
                        print("Victoire du joueur ! Le boss, Jabba's Rancor, a été abattu !")
                        print(" ")
                        print("Retour au menu principal...")
                        print(" ")
                    elif hp_luke<1 and hp_leia<1 and hp_han<1 and hp_chew<1 and hp_vador<1 and hp_storm<1 and hp_snow<1 and hp_boba<1 <1:
                        print(" ")
                        print("Défaite : toutes les unités ont été éliminées !")
                        print("Retour au menu principal...")
                        print(" ")

        #PARAMETRES

        if reponse==2:
            print("")
            print("Paramètres :")
            print("[1] Quitter ce menu")
            print("[2] Changer la game seed")
            print("[3] Toggle debug mode")
            reponsesettings=int(input("-> "))
            if reponsesettings==2:
                random.seed(int(input("Entrer une nouvelle seed : ")))
                print("Ok!")
            if reponsesettings==1:
                print(" ")

            if reponsesettings==3:
                if debug_mode==True:
                    debug_mode=False
                if debug_mode==False:
                    debug_mode=True
                print("Debug mode state: ", debug_mode)

        if reponse==3:
            programme==False

        if not reponse==1 or not reponse==2 or not reponse==3:
            print(" ")
            print("Erreur : Commande non disponible.")
            print(" ")

except FileNotFoundError:
    print("Erreur : Un ou plusieurs fichiers n'ont pas été trouvés.")
except PermissionError:
    print("Erreur : Aucune permission d'accès au fichier. Vérifiez vos permissions.")
except Exception as e:
    print("Erreur : ", str(e))