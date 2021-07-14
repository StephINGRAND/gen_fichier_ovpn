# gen_fichier_ovpn
Générateur de fichier .ovpn

Ce script a été créé dans le but de faciliter la génération du fichier .ovpn client afin de se connecter a un serveur OpenVpn.

Prérequis :

Les certificats ca.crt, client.crt, les clés client.key et ta.key, le fichier modele client.template et le script generateur_ovpn.py dans un meme dossier.

Les certificats sur le serveur OpenVpn doivent etre générés avec l'option nopass.

Ce script ne fonctionne qu'avec python 3.



Fonctionnement:

Pour générer le fichier .ovpn, lancer le script par la commande :

python3 generateur_ovpn.py

Répondre aux questions demandées, le fichier portant le nom suivi du prénom demandés lors de l'exécution du script sera généré avec l'extension .ovpn.

Il n'y a plus qu'a copier le fichier .ovpn généré dans le répertoire de config du client OpenVpn et la connexion peut etre établie.