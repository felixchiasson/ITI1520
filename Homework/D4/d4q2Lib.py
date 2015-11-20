# Devoir 4
# Sofiane Bouabdallah et Félix Chiasson


def effaceTableau(tab):
    '''
    (list) -> None
    Cette fonction prepare le tableau de jeu (la matrice)
    en mettant '-' dans tous les elements.
    Elle ne crée pas une nouvelle matrice
    Preconditions: tab est une reference a une matrice n x n qui contient '-',
    'X' ou 'O'
    '''
    i = 0          # Variable pour les lignes
    while i < 3:   # Boucle qui traverse les lignes change les éléments à -
        j = 0      # Variable colonne
        while j < 3:    # Boucle qui traverse les colonnes
            tab[i][j] = '-'
            j += 1
        # Passer à la prochaine ligne
        i += 1


def verifieGagner(tab):
    '''
    (list) -> bool
    * Preconditions: tab est une reference a une matrice n x n qui contient
    '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!"
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas
    de gagnant
    '''

    if testLignes(tab) == "X" or testCols(tab) == "X" or testDiags(tab) == "X":
        print("Joueur X a gagné!")
        return True
    elif (testLignes(tab) == "O" or testCols(tab) == "O" or
          testDiags(tab) == "O"):
        print("Joueur O a gagné!")
        return True
    elif testMatchNul(tab) is True:
        print("Match Nul")
        return True

    else:
        return False


def testLignes(tab):
    '''
    (list) -> str
    Vérifie s'il y a une ligne ganante.
    Cherche trois 'X' ou trois 'O' dans une ligne.
    Si on trouve, le caractère 'X' ou 'O' est retourné, sinon on retourne '-'.
    Préconditions: tab est une référence à une matrice n x n qui contient '-',
    'X' ou 'O'.
    '''

    i = 0           # Variable pour les lignes
    while i < 3:    # Il y a 3 lignes à vérifier

        # On vérifie s'il y a une ligne contenant (O, O, O).
        if (tab[i][0] == "O" and tab[i][1] == "O" and
                tab[i][2] == "O"):
            return "O"    # Retourne 'O' si une ligne est gagnante.
        # On vérifie s'il y a une ligne contenant (X, X, X)
        elif (tab[i][0] == "X" and tab[i][1] == "X" and
              tab[i][2] == "X"):
            return "X"    # Retourne 'X' si une ligne est gagnante.
        else:
            i += 1        # Passe à la prochaine ligne

    return "-"


def testCols(tab):
    '''
    (list) -> str
    Vérifie s'il y aune colonne gagnante.
    Cherche trois 'X' ou trois 'O' dans une colonne.
    Si on trouve, le caractère 'X' ou 'O'est retourné, sinon on retourne '-'.
    Précondition: tab est une référence à une matrice n x n qui contient '-',
    'X' ou 'O'.
    '''

    i = 0            # Variable pour les colonnes
    while i < 3:
        # On vérifie si 'O' ou 'X' se retrouve 3 fois dans la même colonne
        if tab[0][i] == "O" and tab[1][i] == "O" and tab[2][i] == "O":
            return "O"
        elif tab[0][i] == "X" and tab[1][i] == "X" and tab[2][i] == "X":
            return "X"
        else:
            i += 1   # Passe à la prochaine colonne.

    return "-"


def testDiags(tab):
    ''' (list) ->  str
    * cherche trois 'X' ou trois 'O' dans une diagonale.
    * Si on trouve, le caractere 'X' ou 'O' et retourné
    * sinon '-' est retourné.
    * Preconditions: tab est une reference a une matrice n x n qui contient
    * '-', 'X' ou 'O'
    '''

    if (tab[0][0] == "O" and tab[1][1] == "O" and tab[2][2] == "O") or \
       (tab[0][2] == "O" and tab[1][1] == "O" and tab[2][0] == "O"):
        # on test s'il ya une diagonal gagnante [i][i]
        return "O"
    elif (tab[0][0] == "X" and tab[1][1] == "X" and tab[2][2] == "X") or \
         (tab[0][2] == "X" and tab[1][1] == "X" and tab[2][0] == "X"):
        # on test si l'autre diagonal est gagnante [i][i+2]
        return "X"
    else:
        return "-"


def testMatchNul(tab):
    ''' (list) ->  bool
    * verifie s’il y a un match nul
    * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.
    * Si on ne trouve pas de '-' dans la matrice, retourne True.
    * S'il y a de '-', retourne false.
    * Preconditions: tab est une reference a une matrice n x n qui contient '-'
    * 'X' ou 'O'
    '''

    i = 0
    while i < 3:        # Boucle pour traverser les lignes
        j = 0
        while j < 3:    # boucle pour traverser chaque case de la ligne
            # Si on trouve un seul élément '-', on retourne faux.
            # i.e. le jeu n'est pas finit
            if tab[i][j] == "-":
                return False
            # On regarde la case suivante si on ne trouve pas de '-'.
            else:
                j += 1
        # On retourne à la ligne suivante si on ne trouve pas de '-'.
        i += 1
    return True
