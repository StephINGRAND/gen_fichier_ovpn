import shutil
import os

def questions():

# effacement du dossier temporaire s'il existe
    if os.path.exists('tmp'):
        shutil.rmtree('tmp')

# creation d'un dossier temporaire pour stocker les fichiers tmp
    os.makedirs('tmp')
    
# demande des informations pour configurer le VPN    
    Nom = input("Nom de la personne : ")
    Prenom = input("Prénom de la personne : ")
    IP_serveur = input("Adresse ip du serveur OpenVPN : ")
    Port_serveur = input("Port du serveur OpenVPN : ")

# récap de la config si oui, on génère le fichier, si non on repose les questions
    print("\n", Nom,"\n", Prenom, "\n", IP_serveur, "\n", Port_serveur)
    Correct = input("Est-ce correct ? O/N : ")
    if Correct == "O":
        with open("client.ovpn", "r") as fichier1, open("tmp/ip_serveur.tmp", "w") as fichier2:
            texte = fichier1.read()
            fichier_modif = texte.replace("<serveur_vpn>", IP_serveur)
            fichier2.write(fichier_modif)
            fichier2.close

        with open("tmp/ip_serveur.tmp", "r") as fichier2, open("tmp/port_serveur.tmp", "w") as fichier3:
            texte2 = fichier2.read()
            fichier2_modif = texte2.replace("<port_srv>", Port_serveur)
            fichier3.write(fichier2_modif)
            fichier3.close
           
        with open("ca.crt", "r") as fichier4, open("tmp/port_serveur.tmp", "r") as fichier5, open("tmp/ca_cert.tmp", "w") as fichier6:
            texte3 = fichier4.read()
            texte4 = fichier5.read()
            fichier3_modif = texte4.replace("<ca_cert>", texte3)
            fichier6.write(fichier3_modif)
            fichier6.close

        with open("client.crt", "r") as fichier7, open("tmp/ca_cert.tmp", "r") as fichier8, open("tmp/client_crt.tmp", "w") as fichier9:
            texte5 = fichier7.read()
            texte6 = fichier8.read()
            fichier4_modif = texte6.replace("<cert_cert>", texte5)
            fichier9.write(fichier4_modif)
            fichier9.close


        with open("client.key", "r") as fichier10, open("tmp/client_crt.tmp", "r") as fichier11, open("tmp/client_key.tmp", "w") as fichier12:
            texte7 = fichier10.read()
            texte8 = fichier11.read()
            fichier5_modif = texte8.replace("<private_key>", texte7)
            fichier12.write(fichier5_modif)
            fichier12.close


        with open("ta.key", "r") as fichier13, open("tmp/client_key.tmp", "r") as fichier14, open("{}.ovpn".format(Nom+Prenom), "w") as fichier15:
            texte9 = fichier13.read()
            texte10 = fichier14.read()
            fichier6_modif = texte10.replace("<ta_key>", texte9)
            fichier15.write(fichier6_modif)
            fichier15.close

        shutil.rmtree('tmp')


            
    elif Correct == "N":
        questions()

    
        
  

        
questions()
