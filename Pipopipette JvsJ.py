N = 0

O = 1

S = 2

E = 3



import matplotlib.pyplot as plt 



import matplotlib.patches as patches



def MatriceMurs(n):

    Murs = [[[False, False, False, False] for j in range(n)] for i in range(n)]

    for k in range(n):

        Murs[0][k][N] = True   # mur Nord de la première ligne

        Murs[n-1][k][S] = True # mur Sud de la dernière ligne

        Murs[k][0][O] = True   # mur Ouest de la première colonne

        Murs[k][n-1][E] = True # mur Est de la dernière colonne

    return Murs

    



def MatriceCases(n):

    Cases = [[0 for j in range(n)] for i in range(n)]

    return Cases



    

def Affichage(numJoueur, Cases, Murs):

    print('tour du joueur {} '.format(numJoueur))

  #  affichageplateau(Cases, Murs)



    print('mettre entre 0 et  n -1')

    colonne = input('colonne de la case : ')

    ligne = input('ligne de la case : ')

    direction = input('direction: N , O , S ou E : ')

    return int(colonne), int(ligne), eval(direction)  



    

def Joueur(n, numJoueur, Murs, Cases, cpt0):

    CptPtsTour = 0

    colonne, ligne, direction = Affichage(numJoueur, Cases, Murs)

    while colonne > n-1 or ligne > n-1 :

        print("")

        print('hors matrice: mettre entre 0 et {}'.format(n-1)) 

        colonne, ligne, direction = Affichage(numJoueur, Cases, Murs)

    while Murs[ligne][colonne][direction] : 

        print("")

        print('ce mur est déja pris')

        colonne, ligne, direction = Affichage(numJoueur, Cases, Murs)

    Murs[ligne][colonne][direction] = True

    if direction == N :

        Murs[ligne - 1][colonne][S] = True

    if direction == O :

        Murs[ligne][colonne - 1][E] = True

    if direction == S :

        Murs[ligne + 1][colonne][N] = True

    if direction == E :

        Murs[ligne][colonne + 1][O] = True

    for i in range(n) :

        for j in range(n) :

            if Murs[i][j] == 4*[True] and Cases[i][j] == 0 :

                Cases[i][j] = numJoueur

                CptPtsTour += 1

                cpt0 = cpt0 - 1

    affichageplateau(Cases, Murs)

    return(CptPtsTour, Murs, Cases, cpt0)

    



def affichageplateau(cases, murs):

    fig = plt.figure(1)

    plt.clf()

    n = len(cases)

    axes=fig.add_subplot(111)

    plt.axis('off')

    plt.axis('scaled')

    plt.xlim(-1, n+1)

    plt.ylim(-1,n+1)

    for i in range(n):

        for j in range(n):

            if cases[i][j] == 1:  # joueur 1 : case en bleu

                axes.add_patch(patches.Rectangle((j, n-i-1), 1, 1, color='blue'))

            if cases[i][j] == 2:  # joueur 2 : case en rouge

                axes.add_patch(patches.Rectangle((j, n-i-1), 1, 1, color='red'))            

    for i in range(n+1):

        plt.plot([0,n], [i,i], color='lightgrey')

        plt.plot([i,i], [0,n], color='lightgrey')

    for k in range(n):

        plt.text(-0.6,n-k-0.5, k, ha='center', va='center', color='r')

        plt.text(k+0.5,-0.6, k, ha='center', va='center', color='r')

    for i in range(n):

        for j in range(n):

            if murs[i][j][N]:

                plt.plot([j, j+1], [n-i, n-i],color='green', lw=3 )

            if murs[i][j][S]:

                plt.plot([j, j+1], [n-i-1, n-i-1],color='green', lw=3 )

            if murs[i][j][E]:

                plt.plot([j+1, j+1], [n-i, n-i-1],color='green', lw=3 )

            if murs[i][j][O]:

                plt.plot([j, j], [n-i, n-i-1],color='green', lw=3 )



    

    

def Jeu(n):

    Murs= MatriceMurs(n)

    Cases = MatriceCases(n)

    cpt0 = n**2

    numJoueur = 1

    affichageplateau(Cases, Murs)

    plt.show()

    while cpt0 != 0 :    # tant qu'il y a des cases libres

        affichageplateau(Cases, Murs)

        plt.pause(0.1)

        CptPtsTour, Murs, Cases, cpt0 = Joueur(n, numJoueur, Murs, Cases,cpt0)

        print("")

        while CptPtsTour > 0 and cpt0 != 0:    # tant que le joueur gagne des points

            print('vous avez gagné {} point(s), rejouez'.format(CptPtsTour))

            CptPtsTour, Murs, Cases, cpt0 = Joueur (n, numJoueur, Murs, Cases, cpt0)

            print("")

        if numJoueur == 1 :    # changement de joueur

            numJoueur = 2

        else:

            numJoueur = 1

    cptptsJ1 = 0

    cptptsJ2 = 0

    for i in range(n) :

        for j in range(n) :

            if Cases[i][j] == 1:

                cptptsJ1 += 1

            else:

                cptptsJ2 += 1

    if cptptsJ1 > cptptsJ2 :

        print ('Joueur 1 a gagné')

        print("{} à {}".format(cptptsJ1, cptptsJ2))

    elif cptptsJ1 < cptptsJ2 :

        print ('Joueur 2 a gagné')

        print("{} à {}".format(cptptsJ2, cptptsJ1))

    else :

        print ('égalité')

        print("{} à {}".format(cptptsJ1, cptptsJ2))

