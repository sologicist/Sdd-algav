import math


class NoeudTasMin:

  def __init__(self, cle):
    self.cle = cle
    self.gauche = None
    self.droite = None
    self.parent = None
    self.taille = 1
    self.hauteur = 0

  def majhauteur(self):
    self.hauteur = 0 if not self.gauche and not self.droite else 1 + max(
        0 if not self.gauche else self.gauche.hauteur,
        0 if not self.droite else self.droite.hauteur)

  def get_hauteur(self):
    return int(math.log2(self.taille))

  def majNoeud(self):
    #maj parent
    if self.gauche:

      if self.gauche.cle < self.cle:
        self.cle, self.gauche.cle = self.gauche.cle, self.cle

      self.taille = 1 + self.gauche.taille
      self.gauche.parent = self

    if self.droite:

      if self.droite.cle < self.cle:
        self.cle, self.droite.cle = self.droite.cle, self.cle

      self.taille += self.droite.taille
      self.droite.parent = self


class TasMin:

  def __init__(self):

    self.racine = None
    self.last_node = []
    self.liste_feuille = []

  #Primitives
  def AjoutsIteratifs(self, liste):
    for i in liste:
      self.Ajout(i)

  def Ajout(self, cle):
    # Ajout d'un élément au tas
    nouveau_noeud = NoeudTasMin(cle)
    if not self.racine:
      self.racine = nouveau_noeud
    else:
      self.Rec_Ajout(self.racine, nouveau_noeud)

  def Rec_Ajout(self, parent, nouveau_noeud):
    # Fonction récursive pour ajouter un nœud dans le tas
    if not parent.gauche:
      parent.gauche = nouveau_noeud
      # Met à jour la référence du parent pour le nouveau_noeud
      nouveau_noeud.parent = parent
      # Met à jour la taille du noeud parent
      self.last_node.append(nouveau_noeud)
    elif not parent.droite:
      parent.droite = nouveau_noeud
      # Met à jour la référence du parent pour le nouveau_noeud
      nouveau_noeud.parent = parent
      # Met à jour la taille du noeud parent
      self.last_node.append(nouveau_noeud)
    else:
      # Ajoute le nœud à la branche appropriée
      if parent.gauche.get_hauteur() <= parent.droite.get_hauteur():
        if parent.gauche.taille == parent.droite.taille:
          self.Rec_Ajout(parent.gauche, nouveau_noeud)
        elif parent.gauche.taille % 2 != 0:
          self.Rec_Ajout(parent.droite, nouveau_noeud)
        else:
          self.Rec_Ajout(parent.gauche, nouveau_noeud)
      else:
        if parent.gauche.taille % 2 != 0 and parent.gauche.gauche.taille == parent.gauche.droite.taille:
          self.Rec_Ajout(parent.droite, nouveau_noeud)
        else:
          self.Rec_Ajout(parent.gauche, nouveau_noeud)

    # Réorganise le tas après l'ajout
    parent.majNoeud()

  def last_one(self, node):
    if not node:
      return

    if node.gauche and not node.droite:
      self.last_node.append(node.gauche)
      return

    elif not node.droite and not node.gauche:
      self.last_node.append(node)
      return

    #tas simple avec 3 elts
    elif node.droite and node.gauche and node.droite.taille == 1 and node.gauche.taille == 1:
      self.last_node.append(node.droite)
      return

    else:
      #si on la mm taille, on va à droite
      if node.gauche and node.droite and node.gauche.taille == node.droite.taille:
        self.last_one(node.droite)

      #si gauche rempli et droite vide on va gauche forcement
      elif node.gauche.taille == (2**(node.get_hauteur()) -
                                  1) and node.droite.taille == (
                                      2**(node.get_hauteur() - 1) - 1):
        self.last_one(node.gauche)

      #si gauche plein et droite pas vide go à droite
      elif node.gauche.taille == (
          2**(node.get_hauteur()) -
          1) and node.droite.taille > (2**(node.get_hauteur() - 1) - 1):
        self.last_one(node.droite)

      #si droite vide et gauche pas encore plein go gauche
      elif node.gauche.taille < (2**(node.get_hauteur()) -
                                 1) and node.droite.taille == (
                                     2**(node.get_hauteur() - 1) - 1):
        self.last_one(node.gauche)

  def SupprMin(self):
    if not self.racine:
      return

    if not self.racine.gauche and not self.racine.droite:
      r = self.racine.cle
      self.racine = None
      return r

    if len(self.last_node) == 0:
      self.last_one(self.racine)

    tmp = self.last_node[-1]
    #corps de supprmin dans tous les cas
    while (tmp.parent != self.racine):
      tmp.parent.taille -= 1
      tmp = tmp.parent

    # Échange avec le dernier élément
    dernier_noeud = self.last_node[-1]

    #switch
    r = self.racine.cle
    self.racine.cle, dernier_noeud.cle = dernier_noeud.cle, self.racine.cle
    self.last_node.pop()

    # Retire le dernier nœud (anciennement le nœud de clé minimale)
    if dernier_noeud.parent:
      if dernier_noeud.parent.gauche == dernier_noeud:
        dernier_noeud.parent.gauche = None
      else:
        dernier_noeud.parent.droite = None
    else:
      self.racine = None

    # Fait redescendre le premier élément pour maintenir la propriété du tas
    self.descendre(self.racine)
    return r

  def monter(self, noeud):
    # Fonction pour faire monter un nœud dans le tas
    #while noeud.parent and noeud.cle.inf(noeud.parent.cle):
    while noeud.parent and noeud.cle < noeud.parent.cle:
      noeud.cle, noeud.parent.cle = noeud.parent.cle, noeud.cle
      noeud = noeud.parent

  def descendre(self, noeud):
    # Fonction pour faire descendre un nœud dans le tas
    while True:
      if not noeud:
        break

      gauche = noeud.gauche
      droite = noeud.droite
      plus_petit = noeud

      #if gauche and gauche.cle.inf(plus_petit.cle):
      if gauche and gauche.cle < plus_petit.cle:
        plus_petit = gauche

      #if droite and droite.cle.inf(plus_petit.cle):
      if droite and droite.cle < plus_petit.cle:
        plus_petit = droite

      if plus_petit != noeud:
        # Échange l'élément avec le plus petit des enfants si nécessaire
        noeud.cle, plus_petit.cle = plus_petit.cle, noeud.cle
        noeud = plus_petit
      else:
        break

  def Constructionv2(self, gd=True, parent=None, taille=0):
    if taille == 0 or len(self.to_build) == 0:
      return
    res = self.calculNoeud(taille)
    if not parent:

      self.racine = NoeudTasMin(self.to_build.pop())
      self.Constructionv2(True, self.racine, res[1])
      self.Constructionv2(False, self.racine, res[2])
    else:
      if gd:
        parent.gauche = NoeudTasMin(self.to_build.pop())
        if res[1] != 0:
          self.Constructionv2(True, parent.gauche, res[1])
        if res[2] != 0:
          self.Constructionv2(False, parent.gauche, res[2])
        parent.taille = 1 + parent.gauche.taille
        parent.gauche.parent = parent

      else:
        parent.droite = NoeudTasMin(self.to_build.pop())
        if res[1] != 0:
          self.Constructionv2(True, parent.droite, res[1])
        if res[2] != 0:
          self.Constructionv2(False, parent.droite, res[2])
        parent.taille += parent.droite.taille
        parent.droite.parent = parent

    if not parent:
      return
    if parent.droite or parent.gauche:
      self.descendre(parent)

  def Construction(self, liste):
    if self.racine:
      return
    self.to_build = liste
    self.Constructionv2(True, None, len(liste))

  def calculNoeud(self, taille):
    if taille == 0:
      return

    h = int(math.log2(taille))
    if taille == (2**(h + 1) - 1):
      taille -= 1
      return [1, taille // 2, taille - taille // 2]

    else:

      reste = ((taille + 1) - ((2**h) - 1)) - 1
      liste_g = (taille - reste) // 2
      liste_d = (taille - reste) // 2

      if reste <= ((2**h) // 2):
        liste_g += reste
      else:

        liste_g += ((2**h) // 2)

        liste_d += reste - ((2**h) // 2)

      return [1, liste_g, liste_d]

  def Union(self, tas2):
    self.liste_feuille = []
    tas2.liste_feuille = []

    l1 = self.liste_feuilles(self.racine)
    l2 = tas2.liste_feuilles(tas2.racine)

    if l2 == []:
      return self
    if l1 == []:
      return tas2

    for i in l2:
      l1.append(i)

    tasres = TasMin()
    return tasres.Construction(l1)

  def liste_feuilles(self, noeud):
    if self.racine is None:
      return []
    if not noeud:
      return []

    self.liste_feuille.append(noeud.cle)

    if noeud.gauche:
      self.liste_feuilles(noeud.gauche)

    if noeud.droite:
      self.liste_feuilles(noeud.droite)

    return self.liste_feuille

  def afficher_arbre(self, noeud, prefixe="", est_dernier=True):
    if noeud:
      print(prefixe + ("└── " if est_dernier else "├── ") + str(noeud.cle))
      nouveaux_prefixe = prefixe + ("    " if est_dernier else "│   ")
      self.afficher_arbre(noeud.gauche, nouveaux_prefixe, not noeud.droite)
      self.afficher_arbre(noeud.droite, nouveaux_prefixe, True)
