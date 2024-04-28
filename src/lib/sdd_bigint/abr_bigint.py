import lib.sdd_bigint.bigint as bi


class ABR:
  # Attribut de classe partagé par toutes les instances de la classe permettant de stocker les clés qui entrent en collision
  liste_collision = {}

  def __init__(self, cle):
    """
      Initialisation d'un nœud d'arbre binaire de recherche.
  
      Arguments:
          - cle: Clé du nœud.
  
      Attributs:
          - cle: Clé du nœud.
          - gauche: Référence vers le sous-arbre gauche.
          - droite: Référence vers le sous-arbre droit.
          - parent: Référence vers le parent du nœud.
          - hauteur: Hauteur du nœud dans l'arbre.
      """
    self.cle = bi.Cle128Bits(cle)  #Converion en cle128bits
    self.gauche = None
    self.droite = None
    self.parent = None
    self.hauteur = 0

  def rotation(self):
    """
    Effectue les rotations nécessaires pour équilibrer l'arbre après une opération d'insertion et assure également que le nœud avec la clé maximale est à droite et le nœud avec la clé minimale est à gauche.

    Remarque: Les rotations dépendent du facteur d'équilibre du nœud et de ses sous-arbres.

    Source: https://appliedgo.net/balancedtree/
    """
    facteur_equilibre = self.balance()

    # Cas de l'arbre déséquilibré à droite
    if facteur_equilibre > 1:
      # Cas de la rotation simple à gauche
      if self.droite.balance() >= 0:
        self.RG()
      # Cas de la rotation droite-gauche
      else:
        self.droite.RD()
        self.RG()

    # Cas de l'arbre déséquilibré à gauche
    if facteur_equilibre < -1:
      # Cas de la rotation simple à droite
      if self.gauche.balance() <= 0:
        self.RD()
      # Cas de la rotation gauche-droite
      else:
        self.gauche.RG()
        self.RD()

    # Assure que le nœud avec la clé maximale est à droite
    if self.droite and self.cle.sup(self.droite.cle):
      self.cle, self.droite.cle = self.droite.cle, self.cle

    # Assure que le nœud avec la clé minimale est à gauche
    if self.gauche and (self.gauche.cle.sup(self.cle)
                        or self.gauche.cle.eq(self.cle)):
      self.cle, self.gauche.cle = self.gauche.cle, self.cle

  def construction(self, liste):
    """
    Construit un arbre AVL à partir d'une liste de clés.

    Arguments:
        - liste: Liste des clés à insérer dans l'arbre AVL.

    Note: Cette fonction utilise la méthode d'insertion (insertion) pour ajouter chaque clé de la liste dans l'arbre AVL.

    Retourne:
        Aucune valeur de retour explicite (None).
    """
    for i in range(0, len(liste)):
      self.insertion(liste[i])
    return self

  def insertion(self, value):
    """
    Insère une valeur dans l'arbre AVL.

    Arguments:
        - value: La valeur à insérer dans l'arbre AVL.

    Note: Cette fonction prend en charge l'insertion d'une valeur dans un arbre AVL, ajuste les hauteurs et effectue des rotations
    pour maintenir l'équilibre de l'arbre.

    Retourne:
        Aucune valeur de retour explicite (None).
    """
    # Cas où le nœud actuel est vide
    if self.cle is None:
      self.cle = bi.Cle128Bits(value)
    # Cas où la valeur à insérer est inférieure à la valeur du nœud actuel ou égale à la valeur du nœud actuel
    elif bi.Cle128Bits(value).inf(self.cle) or bi.Cle128Bits(value).eq(
        self.cle):
      
      # Gestion des collisions si les valeurs sont égales
      if bi.Cle128Bits(value).eq(self.cle) and value in ABR.liste_collision:
        ABR.liste_collision[value] += 1
      else:
        ABR.liste_collision[value] = 1
      # Si le sous-arbre gauche est vide, crée un nouveau nœud gauche avec la valeur
      if self.gauche is None:
        self.gauche = ABR(value)
      else:
        # Sinon, récursion pour insérer la valeur dans le sous-arbre gauche
        self.gauche.insertion(value)
    else:
    # Cas où la valeur à insérer est supérieure 
      # Si le sous-arbre droit est vide, crée un nouveau nœud droit avec la valeur
      if self.droite is None:
        self.droite = ABR(value)
      else:
        # Sinon, récursion pour insérer la valeur dans le sous-arbre droit
        self.droite.insertion(value)

    # Met à jour la hauteur du nœud
    self.hauteur = self.hauteurabr()

    # Applique les rotations pour maintenir l'équilibre de l'arbre AVL
    self.rotation()

    return

  def recherche(self, cle):
    """
    Recherche une clé dans l'arbre AVL.

    Arguments:
        - cle: La clé à rechercher dans l'arbre AVL, elle doit etre une instance de la classe Cle128Bits.

    Retourne:
        True si la clé est présente dans l'arbre, False sinon.
    """
    if not isinstance(cle, bi.Cle128Bits):
      cle = bi.Cle128Bits(cle)
    # Cas où la clé du nœud actuel est égale à la clé recherchée
    if self.cle.eq(cle):
      return True
    # Cas où la clé recherchée est inférieure à la clé du nœud actuel
    elif cle.inf(self.cle):
      # Si le sous-arbre gauche est vide, la clé n'est pas présente
      if self.gauche is None:
        return False
      else:
        # Sinon, récursion pour rechercher la clé dans le sous-arbre gauche
        return self.gauche.recherche(cle)
    else:
      # Cas où la clé recherchée est supérieure à la clé du nœud actuel
      # Si le sous-arbre droit est vide, la clé n'est pas présente
      if self.droite is None:
        return False
      else:
        # Sinon, récursion pour rechercher la clé dans le sous-arbre droit
        return self.droite.recherche(cle)

  def balance(self):
    """
    Calcul de la balance du nœud, définie comme la différence entre les hauteurs
    du sous-arbre droit et du sous-arbre gauche.

    Retourne:
        - Valeur de la balance du nœud.
    """
    return (self.droite.hauteur + 1 if self.droite else
            0) - (self.gauche.hauteur + 1 if self.gauche else 0)

  def RD(self):
    """
    Effectue une rotation à droite sur le nœud actuel dans un arbre AVL.

    Description:
        - La fonction effectue une rotation à droite pour rééquilibrer l'arbre AVL.
        - Les sous-arbres et les clés des nœuds sont réorganisés selon le schéma de rotation à droite.

    Remarque:
        - Cette opération est effectuée dans le contexte d'un arbre AVL pour maintenir la propriété d'équilibre.

    """
    #p = self.gauche.cle
    #q = self.cle
    #U = self.gauche.gauche
    #V = self.gauche.droite
    #W = self.droite

    self.cle, self.gauche.cle = self.gauche.cle, self.cle  # switch(p,q)
    self.droite, self.gauche.droite = self.gauche.droite, self.droite  # switch(V, W)
    self.droite, self.gauche.gauche = self.gauche.gauche, self.droite  # switch(U, V)
    self.gauche, self.droite = self.droite, self.gauche  #switch(ABR(q), U)

    # Maj de la hauteur des sous-arbres
    self.droite.hauteur = self.droite.hauteurabr()

    if self.gauche:
      self.gauche.hauteur = self.gauche.hauteurabr()

    self.hauteur = self.hauteurabr()

  def RG(self):
    """
    Effectue une rotation à gauche sur le nœud actuel dans un arbre AVL.

    Description:
        - La fonction effectue une rotation à gauche pour rééquilibrer l'arbre AVL.
        - Les sous-arbres et les clés des nœuds sont réorganisés selon le schéma de rotation à gauche.

    Remarque:
        - Cette opération est effectuée dans le contexte d'un arbre AVL pour maintenir la propriété d'équilibre.
    """

    #p = self.cle
    #q = self.droite.cle
    #U = self.gauche
    #V = self.droite.gauche
    #W = self.droite.droite

    #Switch des clés et éléments de l'arbre
    self.cle, self.droite.cle = self.droite.cle, self.cle  # switch(p,q)
    self.gauche, self.droite.droite = self.droite.droite, self.gauche  # switch(U, W)
    self.droite.gauche, self.droite.droite = self.droite.droite, self.droite.gauche  # switch(V, U)
    self.gauche, self.droite = self.droite, self.gauche  #switch(ABR(q), U)

    # Maj des hauteurs des sous-arbres
    self.gauche.hauteur = self.gauche.hauteurabr()

    if self.droite:
      self.droite.hauteur = self.droite.hauteurabr()

    self.hauteur = self.hauteurabr()

  def hauteurabr(self):
    """
    Calcule la hauteur de l'arbre AVL à partir du nœud actuel.
  
    Retourne:
        La hauteur de l'arbre AVL à partir du nœud actuel.
    """
    # La hauteur d'un nœud est égale à 1 plus la hauteur maximale entre le sous-arbre gauche et le sous-arbre droit
    hauteur = 0 if not self.gauche and not self.droite else 1 + max(
        0 if not self.gauche else self.gauche.hauteurabr(),
        0 if not self.droite else self.droite.hauteurabr())
    return hauteur


def PrintTree(root):

  def height(root):
    return 1 + max(root.gauche.hauteur if root.gauche else 0,
                   root.droite.hauteur if root.droite else 0) if root else -1

  nlevels = root.hauteur
  width = pow(2, nlevels + 1)

  q = [(root, 0, width, 'c')]
  levels = []

  while (q):
    node, level, x, align = q.pop(0)
    if node:
      if len(levels) <= level:
        levels.append([])

      levels[level].append([node, level, x, align])
      seg = width // (pow(2, level + 1))
      q.append((node.gauche, level + 1, x - seg, 'l'))
      q.append((node.droite, level + 1, x + seg, 'r'))

  for i, l in enumerate(levels):
    pre = 0
    preline = 0
    linestr = ''
    pstr = ''
    seg = width // (pow(2, i + 1))
    for n in l:
      valstr = str(n[0].cle.toStringSimplified())
      if n[3] == 'r':
        linestr += ' ' * (n[2] - preline - 1 - seg -
                          seg // 2) + '¯' * (seg + seg // 2) + '\\'
        preline = n[2]
      if n[3] == 'l':
        linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
        preline = n[2] + seg + seg // 2
      pstr += ' ' * (n[2] - pre - len(
          valstr)) + valstr  #correct the potition acording to the number size
      pre = n[2]
    print(linestr)
    print(pstr)
