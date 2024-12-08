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

        if reponse_action==1 and hp_vador<=39:
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
                        
