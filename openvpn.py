

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


    
    var1 = ["<serveur_vpn>", "<port_srv>", "<ca_cert>", "<cert_cert>", "<private_key>", "<ta_key>"]
    var2 = [IP_serveur, Port_serveur, ca_crt, client_crt, client_key, ta_key]


# récap de la config si oui, on génère le fichier, si non on repose les questions

    print("\n", Nom,"\n", Prenom, "\n", IP_serveur, "\n", Port_serveur)
    Correct = input("Est-ce correct ? O/N : ")
    if Correct == "O":
        open("{}.ovpn".format(Nom+Prenom), "w")

        for x in var1:
            for y in var2:
                
                print("je remplace " + x + " par " + y)
                with open("client.ovpn", "r") as fichier1, open("{}.ovpn".format(Nom+Prenom), "r+") as fichier2:
                    texte = fichier1.read()
#                   texte = texte.replace(x, y) vu avec Fabien !

                    
#                    fichier_modif = texte.replace(x, y)
#                    fichier2.write(fichier_modif)
#                    fichier2.close

        
       
            
            
    elif Correct == "N":
        questions()

    
        
  

        
questions()
