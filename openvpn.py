
def questions():
    Nom = input("Nom de la personne : ")
    Prenom = input("Prénom de la personne : ")
    IP_serveur = input("Adresse ip du serveur OpenVPN : ")
    Port_serveur = input("Port du serveur OpenVPN : ")
    print("\n", Nom,"\n", Prenom, "\n", IP_serveur, "\n", Port_serveur)
    Correct = input("Est-ce correct ? O/N : ")
    if Correct == "O":
        adresseip = "remote ", IP_serveur
        portsrv = "port ", Port_serveur
        fichier = open("{}.ovpn".format(Nom+Prenom), "a")
        fichier.close()
    elif Correct == "N":
        questions()      
        
  

    vpn = """
# Automatically generated OpenVPN client config file
# Generated on <la_date> by <un_serveur_du_prestataire_vpn>
# Note: this config file contains inline private keys
#       and therefore should be kept confidential!
# Note: this configuration is user-locked to the username below
# OVPN_ACCESS_SERVER_USERNAME=<votre_identifiant_vpn>
# Define the profile name of this particular configuration file
# OVPN_ACCESS_SERVER_PROFILE=<votre_identifiant_vpn>@<serveur_vpn>
# OVPN_ACCESS_SERVER_WSHOST=<serveur_vpn>:<port>
# OVPN_ACCESS_SERVER_WEB_CA_BUNDLE_START
# -----BEGIN CERTIFICATE-----
# <ici un certificat>
# -----END CERTIFICATE-----
# OVPN_ACCESS_SERVER_WEB_CA_BUNDLE_STOP
# OVPN_ACCESS_SERVER_IS_OPENVPN_WEB_CA=1
client
proto udp
nobind"""
    remote = "remote " + IP_serveur
    port = "port " + Port_serveur
    vpn2 = """
dev tun
dev-type tun
ns-cert-type server
reneg-sec 86400
auth-user-pass
auth-retry interact
comp-lzo yes
verb 3

<ca>
-----BEGIN CERTIFICATE-----"""
    with open("ca.crt", "r") as ca:
        ca_cert = ca.read()
    vpn3 = """
 <ca_cert>
-----END CERTIFICATE-----
</ca>

<cert>
-----BEGIN CERTIFICATE-----
 <cert_cert>
-----END CERTIFICATE-----
</cert>

<key>
-----BEGIN RSA PRIVATE KEY-----
 <private_key>
-----END RSA PRIVATE KEY-----
</key>

key-direction 1
<tls-auth>
#
# 2048 bit OpenVPN static key (Server Agent)
#
-----BEGIN OpenVPN Static key V1-----
 <ta_key>
-----END OpenVPN Static key V1-----
</tls-auth>

# -----BEGIN RSA SIGNATURE-----
 <rsa_sign>
# -----END RSA SIGNATURE-----"""
    fichier = open("{}.ovpn".format(Nom+Prenom), "a")
    fichier.write(vpn + "\n" + remote + "\n" + port + vpn2 + "\n" + str(ca_cert) + vpn3)
    fichier.close()

    
questions()