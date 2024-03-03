#!/usr/bin/env python
"""mapper.py"""

import sys
import csv

# Créez un lecteur CSV pour gérer les données
csv_reader = csv.reader(sys.stdin)

# Ignorer la première ligne (en-tête)
next(csv_reader, None)

# Parcourez les lignes du CSV
for row in csv_reader:
    # Extraire les champs du CSV
    cpcli, codcde, datcde, timbrecde, Nbcolis, qte, points = (
        row[4],
        row[6],
        row[7],
        row[9],
        row[10],
        row[15],
        row[20],
    )
    print('%s;%s;%s;%s;%s;%s;%s' %(cpcli, codcde, datcde, timbrecde, Nbcolis, qte, points))
    '''
    Code à réaliser avec le print à la fin de votre traitement de votre boucle
    '''
