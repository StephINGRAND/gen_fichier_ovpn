
def questions():
    Nom = input("Nom de la personne : ")
    Prenom = input("Prénom de la personne : ")
    IP_serveur = input("Adresse ip du serveur OpenVPN : ")
    Port_serveur = input("Port du serveur OpenVPN : ")
    print("\n", Nom,"\n", Prenom, "\n", IP_serveur, "\n", Port_serveur)
    Correct = input("Est-ce correct ? O/N : ")
    if Correct == "O":
        with open("client.ovpn", "r") as fichier1, open("ip_serveur.tmp", "w") as fichier2:
            texte = fichier1.read()
            fichier_modif = texte.replace("<serveur_vpn>", IP_serveur)
            fichier2.write(fichier_modif)
            fichier2.close
        with open("ip_serveur.tmp", "r") as fichier2, open("{}.ovpn".format(Nom+Prenom), "w") as fichier3:
            texte2 = fichier2.read()
            fichier2_modif = texte2.replace("<port_srv>", Port_serveur)
            fichier3.write(fichier2_modif)
            fichier3.close
           


#           open("{}.ovpn".format(Nom+Prenom), "a")

            
    elif Correct == "N":
        questions()

    
        
  

        
questions()
