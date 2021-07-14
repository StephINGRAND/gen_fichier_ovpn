#/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

def questions():

# demande des informations pour configurer le VPN

    nom_admin = input("Nom de l'administrateur qui génère ce fichier de configuration : ")
    nom = input("Nom de la personne pour qui est le fichier de conf : ")
    prenom = input("Prénom de la personne pour qui est le fichier de conf : ")
    ip_serveur = input("Adresse ip du serveur OpenVPN : ")
    port_serveur = input("Port du serveur OpenVPN : ")

# lecture des fichiers contenants les données à mettre à jour

    certif1 = open("ca.crt", "r")
    ca_crt = certif1.read()
    certif2 = open("client.crt", "r")
    client_crt = certif2.read()
    certif3 = open("client.key", "r")
    client_key = certif3.read()
    certif4 = open("ta.key", "r")
    ta_key = certif4.read()
    date = str(datetime.now())

# dictionnaire
    dico = {"<la_date>" : date, "<admin_sys>" : nom_admin, "<votre_identifiant_vpn>" : (nom+prenom), "<serveur_vpn>" : ip_serveur, "<port_srv>" : port_serveur, "<ca_cert>" : ca_crt, "<cert_cert>" : client_crt, "<private_key>" : client_key, "<ta_key>" : ta_key}

# récap des informations

    print("\n","Nom de l'administrateur : " + nom_admin, "\n", "Nom personne fichier de conf : " + nom,"\n", "Prénom personne fichier de conf : " + prenom, "\n", "Adresse IP du serveur : " + ip_serveur, "\n", "Port du serveur : " + port_serveur, "\n")
    correct = input("Est-ce correct ? O/N : ")

# si Oui, j'ouvre mon fichier

    if correct == str("O") or correct== str("o"):
        with open("client.template", "r") as fichier1, open("{}.ovpn".format(nom+prenom), "w") as fichier2:
            texte = fichier1.read()

# boucle pour piocher dans mon dictionnaire et remplacer mes variables

            for var1 in dico:
                texte = texte.replace(var1, dico[var1])

# écriture dans mon fichier portant le nom+prénom de la personne

            fichier2.write(texte)
            fichier2.close

# fermeture des fichiers certificats

        fichier1.close()
        certif1.close()
        certif2.close()
        certif3.close()
        certif4.close()


# si Non, on redemande les informations

    elif correct == str("N") or str("n"):
        questions()

    
            
questions()
