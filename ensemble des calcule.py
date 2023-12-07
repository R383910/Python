objectif = input("vous vouler calculer : pythagore(1), ax+b(2), ax+b=cx+d(3), aire(4) ")
objectif = int(objectif)
if objectif == 1: #pythagore
    from math import sqrt
    ab = input("quelle est la longeur du premier côté ? ")
    ac = input("quelle est la longeur du deuxième côté ? ")
    ab = float(ab)
    ac = float(ac)
    cb2 = ab**2+ac**2
    cb = sqrt(cb2)
    cb = round(cb)
    print("la longeur de l'hypoténuse est ",cb)
elif objectif == 2 : #ax+b
    a = input("a pour un équation de type ax+b ")
    a = float(a)
    b = input("b pour un équation de type ax+b ")
    b = float(b)
    r = input("résultat pour un équation de type ax+b ")
    r = float(r)
    s = r-b
    s = s/a
    print("une des solutions de l'équation est ",s)
elif objectif == 3: #ax+b=cx+d
    A = input("A pour une équation de type Ax+B=Cx+D ")
    A = float(A)
    B = input("B pour une équation de type Ax+B=Cx+D ")
    B = float(B)
    C = input("C pour une équation de type Ax+B=Cx+D ")
    C = float(C)
    D = input("D pour une équation de type Ax+B=Cx+D ")
    D = float(D)
    Q = A-C
    S = D-B
    if Q == 0:
        print("je ne peux pas résoudre cette équation, il faut que A soit différent de B.")
    else:
        S = S/Q
        print("une des solution de l'équation est ",S)
elif objectif == 4: #aire
    v = input("vous voulez l'aire d'un : carré(1), rectangle(2), triangle rectagle(3) ")
    v = float(v)
    if v == 1: #aire carré
        c = input("Quelle est la longeur du côté du carré ? (en cm) ")
        c = float(c)
        c = c**2
        print("l'aire du carré est ",c," cm ")
    elif v == 2: #aire réctangle
        l = input("Quelle est la largeur du réctangle? ")
        l = float(l)
        lo = input("Quelle est la longeur du rectangle? ")
        lo = float(lo)
        Ar = l*lo
        print("l'aire du réctangle fais : ",Ar," cm2 ")
    elif v == 3: #aire triangle rectangle
        c1 = input("combien mesure le premier côté? (en cm) ")
        c1 = float(c1)
        c2 = input("combien mesure le deusième côté? (en cm) ")
        c2 = float(c2)
        at = c1*c2/2
        print("l'aire du triangle mesure ",at," cm.")
else: #mauvais chiffre
    print("je ne connait pas se calcule.")