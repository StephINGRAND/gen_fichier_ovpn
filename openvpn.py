#/usr/bin/python


def questions():


# demande des informations pour configurer le VPN

    Nom = input("Nom de la personne : ")
    Prenom = input("Prénom de la personne : ")
    IP_serveur = input("Adresse ip du serveur OpenVPN : ")
    Port_serveur = input("Port du serveur OpenVPN : ")

# lecture des fichiers contenants les données à mettre à jour

    ca_crt = (open("ca.crt", "r")).read()
    client_crt = (open("client.crt", "r")).read()
    client_key = (open("client.key", "r")).read()
    ta_key = (open("ta.key", "r")).read()
    rsa_sign = (open("rsasign.rsa", "r")).read()

# dictionnaire
    dico = {"<serveur_vpn>" : IP_serveur, "<port_srv>" : Port_serveur, "<ca_cert>" : ca_crt, "<cert_cert>" : client_crt, "<private_key>" : client_key, "<ta_key>" : ta_key, "<rsa_sign>" : rsa_sign}

# récap des informations

    print("\n", "Nom : " + Nom,"\n", "Prénom : " + Prenom, "\n", "Adresse IP du serveur : " + IP_serveur, "\n", "Port du serveur : " + Port_serveur, "\n")
    Correct = input("Est-ce correct ? O/N : ")

# si Oui, j'ouvre mon fichier
    if Correct == "O" or "o":
        with open("client.template", "r") as fichier1, open("{}.ovpn".format(Nom+Prenom), "w") as fichier2:
            texte = fichier1.read()

# boucle pour piocher dans mon dictionnaire et remplacer mes variables

            for var1 in dico:
                texte = texte.replace(var1, dico[var1])

# écriture dans mon fichier portant le nom+prénom de la personne

            fichier2.write(texte)
            fichier2.close

# si Non, on redemande les informations

    elif Correct == "N" or "n":
        questions()

    
            
questions()
