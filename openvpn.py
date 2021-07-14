

def questions():


# demande des informations pour configurer le VPN

    Nom = input("Nom de la personne : ")
    Prenom = input("Prénom de la personne : ")
    IP_serveur = input("Adresse ip du serveur OpenVPN : ")
    Port_serveur = input("Port du serveur OpenVPN : ")

# lecture des fichiers contenants les certificats

    ca_crt = (open("ca.crt", "r")).read()
    client_crt = (open("client.crt", "r")).read()
    client_key = (open("client.key", "r")).read()
    ta_key = (open("ta.key", "r")).read()


# récap de la config si oui, on génère le fichier, si non on repose les questions

    print("\n", Nom,"\n", Prenom, "\n", IP_serveur, "\n", Port_serveur)
    Correct = input("Est-ce correct ? O/N : ")
    if Correct == "O":
        with open("client.ovpn", "r") as fichier1, open("{}.ovpn".format(Nom+Prenom), "w") as fichier2:
            texte = fichier1.read()
            fichier_modif = texte.replace("<serveur_vpn>", IP_serveur)
            fichier2.write(fichier_modif)
            fichier2.close

        with open("{}.ovpn".format(Nom+Prenom), "r") as fichier2, open("{}.ovpn".format(Nom+Prenom), "r+") as fichier3:
            texte2 = fichier2.read()
            fichier2_modif = texte2.replace("<port_srv>", Port_serveur)
            fichier3.write(fichier2_modif)
            fichier3.close


        with open("{}.ovpn".format(Nom+Prenom), "r") as fichier2, open("{}.ovpn".format(Nom+Prenom), "r+") as fichier3:
            texte2 = fichier2.read()
            fichier2_modif = texte2.replace("<ca_cert>", ca_crt)
            fichier3.write(fichier2_modif)
            fichier3.close

        with open("{}.ovpn".format(Nom+Prenom), "r") as fichier2, open("{}.ovpn".format(Nom+Prenom), "r+") as fichier3:
            texte2 = fichier2.read()
            fichier2_modif = texte2.replace("<cert_cert>", client_crt)
            fichier3.write(fichier2_modif)
            fichier3.close

        with open("{}.ovpn".format(Nom+Prenom), "r") as fichier2, open("{}.ovpn".format(Nom+Prenom), "r+") as fichier3:
            texte2 = fichier2.read()
            fichier2_modif = texte2.replace("<private_key>", client_key)
            fichier3.write(fichier2_modif)
            fichier3.close

        with open("{}.ovpn".format(Nom+Prenom), "r") as fichier2, open("{}.ovpn".format(Nom+Prenom), "r+") as fichier3:
            texte2 = fichier2.read()
            fichier2_modif = texte2.replace("<ta_key>", ta_key)
            fichier3.write(fichier2_modif)
            fichier3.close


            
            
    elif Correct == "N":
        questions()

    
        
  

        
questions()
