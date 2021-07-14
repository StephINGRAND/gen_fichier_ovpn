

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
    rsa_sign = (open("rsasign.rsa", "r")).read()


# récap de la config si oui, on génère le fichier, si non on repose les questions

    print("\n", Nom,"\n", Prenom, "\n", IP_serveur, "\n", Port_serveur)
    Correct = input("Est-ce correct ? O/N : ")
    if Correct == "O":
        with open("client.ovpn", "r") as fichier1, open("{}.ovpn".format(Nom+Prenom), "w") as fichier2:
            texte = fichier1.read()
            texte = texte.replace("<serveur_vpn>", IP_serveur)
            texte = texte.replace("<port_srv>", Port_serveur)
            texte = texte.replace("<ca_cert>", ca_crt)
            texte = texte.replace("<cert_cert>", client_crt)
            texte = texte.replace("<private_key>", client_key)
            texte = texte.replace("<ta_key>", ta_key)
            texte = texte.replace("<rsa_sign>", rsa_sign)
            fichier2.write(texte)
            fichier2.close


            
            
    elif Correct == "N":
        questions()

    
        
  

        
questions()
