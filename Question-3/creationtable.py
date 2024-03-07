import happybase

# Connexion à HBase
connection = happybase.Connection('node176250-env-1839015-etudiant37.sh1.hidora.com', 11775) #VM 37 à changer par user
# Ouvrir la connexion
connection.open()

connection.create_table(
            "ma_table",
            {
                'codcli': dict(),
                'genrecli': dict(),
                'nomcli': dict(),
                'prenomcli': dict(),
                'cpcli': dict(),
                'villecli': dict(),
                'codcde': dict(),
                'datcde': dict(),
                'timbrecli': dict(),
                'timbrecde': dict(),
                'Nbcolis': dict(),
                'cheqcli': dict(),
                'barchive': dict(),
                'bstock': dict(),
                'codobj': dict(),
                'qte': dict(),
                'Colis': dict(),
                'libobj': dict(),
                'Tailleobj': dict(),
                'Poidsobj': dict(),
                'points': dict(),
                'indispobj': dict(),
                'libcondit': dict(),
                'prixcond': dict(),
                'puobj': dict()
            }
)
connection.close()            