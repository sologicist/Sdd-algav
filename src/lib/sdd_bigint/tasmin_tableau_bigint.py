import lib.sdd_bigint.bigint as bi


def monter(Tas, pos):
  """
  Fonction pour faire monter un nœud dans le tas.

  Arguments:
      - Tas: Liste d'éléments représentant le tas binaire.
      - pos: Position dans la liste du nœud à faire monter.

  Description:
      - La fonction compare le nœud à son parent et les échange si nécessaire pour maintenir la propriété du tas.
      - Elle continue récursivement vers le haut jusqu'à la racine du tas si le parent n'est pas la racine.

  Retourne:
      - Aucun retour, les modifications sont faites directement sur la liste (Tas).
  """

  # position du pere
  pere = (pos - 1) // 2
  if Tas[pos].inf(Tas[pere]):
    # switch
    Tas[pere], Tas[pos] = Tas[pos], Tas[pere]

    if pere > 0:  # On continue de monter si le pere n'est pas à la racine du tas (pos = 0)
      monter(Tas, pere)


def SupprMin(Tas):
  """
  Suppression de la clé minimale dans un tas binaire.

  Arguments:
      - Tas: Liste représentant le tas binaire.

  Description:
      - La fonction supprime la clé minimale du tas en échangeant la racine avec le dernier élément de la liste, puis en le supprimant.
      - Elle vérifie ensuite que la structure est toujours un tas binaire en appelant la fonction de descente.

  Retourne:
      - La valeur minimale qui a été supprimée du tas.
  """
  if len(Tas) == 0:
    return None

  min_val = Tas[0]  # On garde l'elt minimal
  Tas[0], Tas[-1] = Tas[-1], Tas[0]  # On place le dernier élément en tête
  Tas.pop()  # On supprime le dernier élément
  descendre(
      Tas,
      0)  # On vérifie que la structure est toujours un tas depuis la racine

  return min_val


def Ajout(Tas, elt):
  """
  Ajout d'une clé dans un tas binaire.

  Arguments:
      - Tas: Liste représentant le tas binaire.
      - elt: Nouvelle clé à ajouter dans le tas.

  Description:
      - La fonction ajoute la nouvelle clé à la fin de la liste représentant le tas.
      - Ensuite, elle vérifie que la structure est toujours un tas binaire en appelant la fonction de montée.

  Retourne:
      - La liste mise à jour représentant le tas.
  """
  if isinstance(elt, bi.Cle128Bits):
    Tas.append(elt)
  else:
    Tas.append(bi.Cle128Bits(elt))
  monter(
      Tas,
      len(Tas) - 1
  )  # On vérifie que la structure est toujours un tas depuis le dernier élément

  return Tas


def AjoutsIteratifs(Tas, data):
  """
  Ajout itératif de plusieurs clés dans un tas binaire.
  
  Arguments:
      - Tas: Liste représentant le tas binaire.
      - data: Liste des clés à ajouter dans le tas.
  
  Description:
      - La fonction itère sur la liste 'data' et ajoute chaque clé dans le tas en utilisant la fonction Ajout.
      - Si la liste 'data' est vide, elle renvoie simplement le tas d'origine.
  
  Retourne:
      - La liste mise à jour représentant le tas.
  """
  if len(data) == 0:
    return Tas

  for i in range(len(data)):
    Ajout(Tas, data[i])

  return Tas


def descendre(Tas, pos):
  """
  Fonction pour faire descendre un nœud dans le tas.

  Arguments:
      - Tas: Liste d'éléments représentant le tas binaire.
      - pos: Position dans la liste du nœud à faire descendre.

  Description:
      - La fonction compare le nœud avec ses fils gauche et droit (s'il en a) et échange avec le plus petit des fils si nécessaire.
      - Elle continue récursivement vers le bas tant que les échanges sont nécessaires pour maintenir la propriété du tas.

  Retourne:
      - Aucun retour, les modifications sont faites directement sur la liste (Tas).
  """
  pere = pos
  fils_gauche = 2 * pos + 1
  fils_droit = 2 * (pos + 1)

  # Recherche des fils gauche et droit du nœud
  noeud = []
  if fils_droit < len(Tas):
    noeud = [Tas[pere], Tas[fils_gauche], Tas[fils_droit]]
  elif fils_gauche >= len(Tas):
    return
  else:
    noeud = [Tas[pere], Tas[fils_gauche]]

  min = 0
  # Trouver l'index du plus petit élément parmi le nœud et ses fils
  if len(noeud) == 2:
    min = 0 if noeud[0].inf(noeud[1]) else 1
  else:
    if noeud[0].inf(noeud[1]) and noeud[0].inf(noeud[2]):
      min = 0
    elif noeud[1].inf(noeud[0]) and noeud[1].inf(noeud[2]):
      min = 1
    elif noeud[2].inf(noeud[0]) and noeud[2].inf(noeud[1]):
      min = 2

  if min != 0:  # Teste si le parent est bien l'élément le plus petit, si différent de 0 alors
    # on doit échanger le père avec son plus petit fils
    index_min = 2 * pos + min
    Tas[pere], Tas[index_min] = Tas[index_min], Tas[pere]

    if (2 * index_min + 1) < len(
        Tas
    ):  # si le fils gauche est inférieur à la taille du tableau, on peut continuer
      descendre(Tas, index_min)


def Construction(liste_cle):
  """
  Construction d'un tas binaire à partir d'une liste de clés.
  
  Arguments:
      - liste_cle: Liste d'éléments à utiliser pour construire le tas binaire.
  
  Description:
      - La fonction prend une liste d'éléments en entrée et construit un tas binaire en utilisant l'algorithme de descente (descendre).
      - Elle commence à partir de la moitié de la liste (correspondant à la base du tas) et descend jusqu'à la racine, en équilibrant et appliquant la fonction de descente à chaque étape.
  
  Retourne:
      - La liste modifiée (Tas) qui représente le tas binaire.
  """
  Tas = []
  for x in liste_cle:
    if isinstance(x, bi.Cle128Bits):
      Tas.append(x)
    else:
      Tas.append(bi.Cle128Bits(x))  # Conversion de la clé en Clé128Bits

  for i in range(len(Tas) // 2, 0, -1):
    # On part de la base (n total/2^h, avec h=0 à la base)
    # pour remonter sur toute la hauteur du tas
    # Les derniers noeuds n'ayant pas de fils, on peut passer directement à leur racine
    # On équilibre puis on monte, ce qui revient à aller à l'élément précédent dans le tableau
    # Puis on réapplique la fonction de descente jusqu'à ce que le tas soit bien un tas min
    descendre(Tas, i - 1)
  return Tas


def Union(Tas1, Tas2):
  """
  Union de deux tas binaires.

  Arguments:
      - Tas1: Liste représentant le premier tas binaire.
      - Tas2: Liste représentant le deuxième tas binaire.

  Description:
      - La fonction prend deux tas binaires en entrée et les fusionne pour former un nouveau tas binaire.
      - Si les deux tas sont vides, elle renvoie None.
      - Si l'un des tas est vide, elle renvoie l'autre tas après l'avoir transformé en tas binaire.
      - Elle itère sur les éléments du deuxième tas et les ajoute au premier tas.
      - Enfin, elle applique la fonction de Construction pour s'assurer que le résultat est un tas binaire.

  Retourne:
      - La liste représentant le tas binaire résultant de l'union.
  """
  # Cas où les deux tas sont vides
  if len(Tas1) == 0 and len(Tas2) == 0:
    return None

  # Cas où le premier tas est vide
  if Tas1 == []:
    return Construction(Tas2)

  # Cas où le deuxième tas est vide
  if Tas2 == []:
    return Construction(Tas1)

  # Ajout des éléments du deuxième tas au premier tas
  for i in Tas2:
    Tas1.append(i)

  # Rééquilibrage du tas résultant de l'union
  Construction(Tas1)
  return Tas1


def Print(tab):
  for i in range(0, (len(tab) // 2)):
    if (2 * (i + 1) < len(tab) and (2 * i + 1) < len(tab)):
      print(" PARENT : " + tab[i].toString() + " LEFT CHILD : " +
            tab[2 * i + 1].toString() + " RIGHT CHILD : " +
            tab[2 * (i + 1)].toString())
    elif (2 * (i + 1)) < len(tab):
      print(" PARENT : " + tab[i].toString() + " LEFT CHILD : " +
            tab[2 * i + 1].toString())
    elif (2 * i + 1) < len(tab):
      print(" PARENT : " + tab[i].toString())


"""def list_to_list_bigint(liste): #PAS BESOIN
  res = []
  for x in liste:
    res.append(bi.Cle128Bits(x))
  return res"""
