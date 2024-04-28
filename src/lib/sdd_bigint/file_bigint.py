import lib.sdd_bigint.bigint as bi


class Tournoi:

  def __init__(self, cle):  # [racine, fils_g,..., fils_d]
    """
    Initialise un tournoi avec une clé donnée.

    Arguments:
        - cle: La clé initiale pour créer le tournoi.

    Attributs:
        - T: Liste représentant le tournoi avec la racine et les fils.
        - Deg: Degré du tournoi, qui est le nombre de fils de la racine.
    """
    if isinstance(cle, bi.Cle128Bits):
      self.T = [cle]
    else:
      self.T = [bi.Cle128Bits(cle)]
    self.Deg = 0

  def EstVide(self):
    """
    Vérifie si le tournoi est vide.

    Returns:
        - bool: True si le tournoi est vide, sinon False.
    """
    return len(self.T) == 0

  def Degre(self):
    """
    Renvoie le degré de la racine du tournoi.

    Returns:
        - int: Le degré de la racine du tournoi.
    """
    return self.Deg

  def Union2Tid(self, T2):
    """
    Renvoie l'union de deux tournois de même taille.

    Arguments:
        - T2 (TournoiB): Deuxième tournoi à fusionner.

    Returns:
        - TournoiB: Le tournoi résultant de l'union.
        - str: Message d'erreur si les tournois ne sont pas de même taille.
    """
    if self.Deg != T2.Deg:
      return "Les deux tournois ne sont pas de même taille"

    # On compare la racine des 2 tournois
    elif self.Racine().inf(T2.Racine()):
      self.T.append(
          T2
      )  # On ajoute le tournoi T2 à la fin du tournoi T : T1 = [racine, fils = T2]
      self.Deg += 1
      return self
    else:
      T2.T.append(
          self
      )  # On ajoute le tournoi T à la fin du tournoi T2 : T2 = [racine, fils = T1]
      T2.Deg += 1
      return T2

  def Racine(self):
    """
    Renvoie la racine du tournoi.

    Returns:
        - Cle128Bits: La clé de la racine du tournoi.
    """
    return self.T[0]

  def Decapite(self):
    """
    Renvoie la file binomiale obtenue en supprimant la racine
    du tournoi.
  
    Returns:
        - FileB: La file binomiale obtenue après suppression de la racine du tournoi : T_k = < T_{k −1} , T_{k −2} , ... , T_1 , T_0 >.
  
    Description:
        - Vérifie si le tournoi est vide ou s'il a seulement une racine (cas de base).
        - Initialise une nouvelle file binomiale (F).
        - Parcourt les racines du tournoi en ordre décroissant et les ajoute à la file (F).
        - Retourne la file binomiale (F) obtenue après suppression de la racine du tournoi.
  
    Remarque:
        - La file obtenue est décroissante car les racines sont ajoutées en sens inverse.
    """
    if self.EstVide() or len(self.T) == 1:
      return None

    F = File()
    for i in range(len(self.T) - 1, 0, -1):  # file décroissante
      F.AjoutMin(self.T[i])
    return F

  def File(self):
    """
    Renvoie une file binomiale réduite au tournoi T_k -> <T_k>.

    Returns:
        - FileB: La file binomiale réduite au tournoi actuel.

    Description:
        - Initialise une nouvelle file binomiale (file).
        - Ajoute le tournoi actuel (self) comme racine de la file.
        - Retourne la file binomiale réduite au tournoi actuel.

    Remarque:
        - La file binomiale réduite au tournoi actuel ne contient que ce tournoi comme élément.
    """
    file = File()
    file.AjoutMin(self)
    return file

  def str(self):
    """Renvoie le degre ainsi que la racine du tournoi"""
    return "(" + str(
        self.Deg) + "," + " racine : " + self.T[0].toString() + ")"


class File:

  def __init__(self):
    """
      Initialise une nouvelle file binomiale.

      Attributes:
          - LT (list): Liste des tournois binomiaux contenus dans la file.
          - MinDegreIndex (int or None): Index du tournoi de degré minimum dans la file.
                                         None si la file est vide.
          - taille (int): Taille de la file, représentant le nombre total de tournois binomiaux.

      Description:
          - Initialise une nouvelle file binomiale avec une liste vide de tournois (LT).
          - Le MinDegreIndex est initialisé à None si la liste de tournois est vide.
          - La taille est initialisée à 0.
      """
    self.LT = []
    self.MinDegreIndex = None if len(self.LT) == 0 else self.LT[-1].Deg
    self.taille = 0

  def EstVide(self):
    """ FileB −> booleen
    Renvoie vrai si la file est vide, sinon faux."""
    return len(self.LT) == 0

  def MinDeg(self):
    """ FileB −> TournoiB
    Renvoie le tournoi de degré minimal dans la file."""
    return self.LT[self.MinDegreIndex] if self.MinDegreIndex else None

  def Reste(self):
    """ FileB −> FileB
    Renvoie la file privée de son tournoi de degré minimal.

    Description:
        - Si la file n'est pas vide, elle retire le tournoi de degré minimal de la file.
        - La taille de la file est mise à jour en soustrayant 2^d où d est le degré du tournoi retiré.

    Retourne:
        - La file modifiée après la suppression du tournoi de degré minimal.
    """
    if not self.EstVide():
      tk = self.LT.pop(-1)
      self.taille -= 2**tk.Degre()
    return self

  def AjoutMin(self, Tk):
    """ Tournoi * FileB −> FileB
    Hypothèse : le tournoi est de degré inférieur au MinDeg de la file.
    Renvoie la file obtenue en ajoutant le tournoi comme tournoi de degré minimal de la file initiale.

    Description:
        - Ajoute le tournoi Tk à la file.
        - Met à jour l'indice du tournoi de degré minimal si Tk a un degré inférieur à celui du tournoi actuel de degré minimal.
        - Met à jour la taille de la file en ajoutant 2^d, où d est le degré de Tk.

    Retourne:
        - La file modifiée après l'ajout du tournoi comme tournoi de degré minimal.
    """
    self.LT.append(Tk)
    self.MinDegreIndex = -1
    self.taille += 2**Tk.Degre()
    return self

  def UnionFile(self, F2):
    """ FileB * FileB −> FileB
    Renvoie la file binomiale union des deux files F1 et F2.

    Description:
        - Utilise la méthode UFret pour réaliser l'union de deux files binomiales.

    Arguments:
        - F2: Deuxième file binomiale à unir avec la file courante.

    Retourne:
        - La file binomiale résultant de l'union de la file courante avec F2.
    """
    return self.UFret(F2, None)

  def UFret(self, F2, T):  # Fonction du cours
    """ FileB * FileB * TournoiB −> FileB
    Renvoie la file binomiale union de deux files et d’un tournoi.

    Arguments:
        - F2: Deuxième file binomiale à unir avec la file courante.
        - T: Tournoi en retenue.

    Retourne:
        - La file binomiale résultant de l'union de la file courante avec F2 et d'un tournoi en retenue.
    """
    if not T or T.EstVide():  # pas de tournoi en retenue

      if self.EstVide():
        return F2
      if F2.EstVide():
        return self

      T1 = self.MinDeg()
      T2 = F2.MinDeg()

      if T1 and T2 and T1.Degre() < T2.Degre():
        # Cas où le degré du tournoi de la file courante est inférieur à celui de F2
        return self.Reste().UnionFile(F2).AjoutMin(T1)
      if T1 and T2 and T2.Degre() < T1.Degre():
        # Cas où le degré du tournoi de F2 est inférieur à celui de la file courante
        return self.UnionFile(F2.Reste()).AjoutMin(T2)
      if T1 and T2 and T1.Degre() == T2.Degre():
        # Cas où les deux tournois ont le même degré
        return self.Reste().UFret(F2.Reste(), T1.Union2Tid(T2))
    else:  # T tournoi en retenue
      if self.EstVide():
        # Cas où la file courante est vide
        return T.File().UnionFile(F2)
      if F2.EstVide():
        # Cas où F2 est vide
        return self.UnionFile(T.File())

      T1 = self.MinDeg()
      T2 = F2.MinDeg()
      if T1 and T2 and T.Degre() < T1.Degre() and T.Degre() < T2.Degre():
        # Cas où le degré du tournoi de retenue est inférieur à celui de T1 et T2
        return self.UnionFile(F2).AjoutMin(T)
      if T1 and T2 and T.Degre() == T1.Degre() and T.Degre() == T2.Degre():
        # Cas où le degré de retenue est égal à celui de T1 et T2
        return self.Reste().UFret(F2.Reste(), T1.Union2Tid(T2)).AjoutMin(T)
      if T1 and T2 and T.Degre() == T1.Degre() and T.Degre() < T2.Degre():
        # Cas où le degré de retenue est égal à celui de T1 et inférieur à celui de T2
        return self.Reste().UFret(F2, T1.Union2Tid(T))
      if T1 and T2 and T.Degre() == T2.Degre() and T.Degre() < T1.Degre():
        # Cas où le degré de retenue est égal à celui de T2 et inférieur à celui de T1
        return self.UFret(F2.Reste(), T2.Union2Tid(T))

  def Construction(self, liste):
    """ liste * FileB −> FileB
    Renvoie la file binomiale construite à partir de la liste.

    Arguments:
        - liste: Liste de clés.

    Description:
        - Ajoute chaque clé de la liste à la file binomiale.

    Retourne:
        - La file binomiale construite.
    """
    for x in liste:
      self.Ajout(x)

  def Ajout(self, x):
    """ FileB * Entier −> None
    Ajoute une clé à la file binomiale.

    Arguments:
        - x: Clé à ajouter.

    Description:
        - Crée un tournoi avec la clé x.
        - Effectue l'union de la file actuelle avec le tournoi formé.
        - Met à jour les propriétés de la file.

    Retourne:
        - Aucun retour.
    """
    t = Tournoi(x)  # Conversion en bigint et création du tournoi
    res = self.UnionFile(t.File(
    ))  #Union de la file actuelle avec la file formée d'un seul tournoi
    self.LT = res.LT  # Maj de la file actuelle
    self.MinDegreIndex = res.MinDegreIndex

  def SupprMin(self):  # O(4*log(N)) -> O(log(n))
    """ FileB −> FileB
    Renvoie la file binomiale en supprimant la racine minimale de la file.

    Description:
        - Si la file est vide, retourne une file vide.
        - Recherche le tournoi de degré avec la racine minimale en parcourant la liste des tournois.
        - Supprime le tournoi de degré minimal de la liste.
        - Réduit la taille de la file.
        - Obtient la file résultant de la décapitation du tournoi de degré minimal.
        - Union de la file actuelle avec la file issue de la décapitation du tournoi.

    Retourne:
        - La file binomiale résultant de la suppression de la racine minimale.
    """
    if self.EstVide():
      return "Rien a supprimé"
    else:
      # Recherche du tournoi avec la racine minimale
      index = -1
      min = bi.Cle128Bits("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
      for i in range(len(
          self.LT)):  # O(log(n)) car il y'a log(n) éléments dans la liste
        tk = self.LT[i]
        if tk.T[0].inf(min):
          min = tk.T[0]
          index = i

      # Suppression du tournoi de degré minimal de la liste
      tksup = self.LT.pop(
          index)  # O(log(n)) car il y'a log(n) éléments dans la liste

      # Réduction de la taille de la file
      self.taille -= 1

      # Obtention de la file résultant de la décapitation du tournoi de degré minimal
      r = tksup.Racine()
      F = tksup.Decapite()  # O(log(n))

      # Union de la file actuelle avec la file résultante
      if F:
        res = self.UnionFile(
            F)  # O(log(n)) avec n la taille de la nouvelle file
        self.LT = res.LT

      return r

  def get_taille(self):  # O(log(n))
    """
    Met à jour la taille de la file binomiale.

    Description:
        - Si la file est vide, la taille est mise à 0.
        - Sinon, la taille est calculée comme la somme des puissances de 2 correspondant
          aux degrés des tournois présents dans la file.

    Note:
        Cette fonction doit être appelée pour maintenir la propriété de la taille de la file
        après des opérations telles que l'ajout, la suppression, etc.

    """
    self.taille = 0 if len(self.LT) == 0 else sum([(2**t.Degre())
                                                   for t in self.LT])
    return self.taille

  def afficheFile(self):
    """
    Affiche le contenu de la file binomiale.
  
    Description:
        - Affiche la taille de la file.
        - Affiche les tournois présents dans la file via un tuple (degre, racine)
  
    """
    print("File" + str(self.get_taille()) + " = ", end=" "),
    for i in range(len(self.LT)):
      print(self.LT[i].str(), end=" "),
    print(" ")
