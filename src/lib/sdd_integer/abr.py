class ABR:

  def __init__(self, cle):
    self.cle = cle
    self.gauche = None
    self.droite = None
    self.parent = None
    self.hauteur = 0

  def rotation(self):  #https://appliedgo.net/balancedtree/
    # Calculer le facteur d'équilibre
    facteur_equilibre = self.balance()

    # Cas de l'arbre déséquilibré à droite
    if facteur_equilibre > 1:
      # Cas de la rotation simple à droite
      if self.droite.balance() >= 0:
        self.RG()
      # Cas de la rotation gauche-droite
      else:
        self.droite.RD()
        self.RG()

    # Cas de l'arbre déséquilibré à gauche
    if facteur_equilibre < -1:
      # Cas de la rotation simple à gauche
      if self.gauche.balance() <= 0:
        self.RD()
      # Cas de la rotation droite-gauche
      else:
        self.gauche.RG()
        self.RD()

    if self.droite and self.cle > self.droite.cle:
      self.cle, self.droite.cle = self.droite.cle, self.cle

    if self.gauche and self.gauche.cle >= self.cle:
      self.cle, self.gauche.cle = self.gauche.cle, self.cle

    #print("cle : " + str(self.cle) + " hauteur : " + str(self.hauteur))

  def construction(self, liste):
    for i in range(0, len(liste)):
      self.insertion(liste[i])
    return

  def insertion(self, value):
    if self.cle is None:
      self.cle = value
    elif self.cle >= value:
      if self.gauche is None:
        self.gauche = ABR(value)
      else:
        self.gauche.insertion(value)

    else:
      if self.droite is None:
        self.droite = ABR(value)
      else:
        self.droite.insertion(value)

    self.hauteur = self.hauteurabr()

    self.rotation()

    return

  def recherche(self, cle):
    if self.cle == cle:
      return True
    elif self.cle > cle:
      if self.gauche is None:
        return False
      else:
        return self.gauche.recherche(cle)
    else:
      if self.droite is None:
        return False
      else:
        return self.droite.recherche(cle)

  def balance(self):
    """if self.gauche and self.droite:
      return self.droite.hauteur - self.gauche.hauteur
    elif not self.gauche and self.droite:
      return self.droite.hauteur + 1
    elif not self.droite and self.gauche:
      return self.gauche.hauteur + 1"""

    return (self.droite.hauteur + 1 if self.droite else
            0) - (self.gauche.hauteur + 1 if self.gauche else 0)

  def RD(self):
    """p = self.gauche.cle
      q = self.cle
      U = self.gauche.gauche
      V = self.gauche.droite
      W = self.droite"""

    self.cle, self.gauche.cle = self.gauche.cle, self.cle  # switch(p,q)
    self.droite, self.gauche.droite = self.gauche.droite, self.droite  # switch(V, W)
    self.droite, self.gauche.gauche = self.gauche.gauche, self.droite  # switch(U, V)
    self.gauche, self.droite = self.droite, self.gauche  #switch(ABR(q), U)

    self.droite.hauteur = self.droite.hauteurabr()

    if self.gauche:
      self.gauche.hauteur = self.gauche.hauteurabr()

    self.hauteur = self.hauteurabr()

  def RG(self):
    """p = self.cle
    q = self.droite.cle
    U = self.gauche
    V = self.droite.gauche
    W = self.droite.droite"""

    self.cle, self.droite.cle = self.droite.cle, self.cle  # switch(p,q)
    self.gauche, self.droite.droite = self.droite.droite, self.gauche  # switch(U, W)
    self.droite.gauche, self.droite.droite = self.droite.droite, self.droite.gauche  # switch(V, U)
    self.gauche, self.droite = self.droite, self.gauche  #switch(ABR(q), U)

    self.gauche.hauteur = self.gauche.hauteurabr()

    if self.droite:
      self.droite.hauteur = self.droite.hauteurabr()

    self.hauteur = self.hauteurabr()

  def hauteurabr(self):
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
      valstr = str(n[0].cle)
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
